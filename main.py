import os
import re
import json
import torch
import logging
from tqdm import tqdm
from modal import Mount
from common import stub, VOLUME_CONFIG, gpu


from prompts import (
    SAMPLE_PROMPTS,
    GET_COMPLETION,
    POSITIVE_COMPLETION,
    SAMPLE_PROMPTS_CONFIG,
    GET_COMPLETION_CONFIG,
    POSITIVE_COMPLETION_CONFIG,
    REFERENCE_TASK_PROMPTS,
    REFERENCE_TASK_PROMPTS_CONFIG,
    SAMPLE_PROMPT_CATEGORIES,
    SAMPLE_PROMPT_CATEGORIES_CONFIG
)
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
from utils import ModelArguments, PeftSavingCallback, DTYPES, get_args, dump_arg_dicts


logging.basicConfig(level=logging.INFO)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
# Increase timeout to prevent wandb errors
os.environ["WANDB__SERVICE_WAIT"] = "300"
# turn off watch to log faster
os.environ["WANDB_WATCH"]="false"
# Setting to parallelism to true
os.environ["TOKENIZERS_PARALLELISM"] = "True"


with stub.image.imports():
    import wandb
    from openai import OpenAI
    from peft import LoraConfig
    from datasets import Dataset
    from datasets.combine import concatenate_datasets
    from trl import DPOTrainer, SFTTrainer, DataCollatorForCompletionOnlyLM

def rank0_log_info(*args):
    logging.info(*args)


def get_openai_model(api_key: str = None):
    if api_key is None:
        api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)


def get_model(model_args: ModelArguments, adapter_path: str = None) -> AutoModelForCausalLM:
    assert not (model_args.load_in_4bit and model_args.load_in_8bit)

    args = {
        "attn_implementation": "flash_attention_2"
    }

    if model_args.load_in_4bit:
        args["load_in_4bit"] = True
    if model_args.load_in_8bit:
        args["load_in_8bit"] = True
    
    args["torch_dtype"] = DTYPES[model_args.dtype]
    args["device_map"] = DEVICE
    model = AutoModelForCausalLM.from_pretrained(
        model_args.model_name_or_path, **args
    )
    rank0_log_info(f"Loaded model from {model_args.model_name_or_path}")
    if adapter_path is not None:
        model.load_adapter(adapter_path)
        rank0_log_info(f"Loaded adapter from {adapter_path}")
    return model


def get_responses(batch: list[list[str]], model: AutoModelForCausalLM, tokenizer: AutoTokenizer, batch_size: int = 8, gen_config: dict = {}) -> list[str]:
    """Assumes batch is a list of lists of strings, where each inner list is a list of chat messages that alternate between user and assistant."""
    batch = [[{
        "role": "user" if i % 2 == 0 else "assistant",
        "content": m
    } for i, m in enumerate(b)] for b in batch]
    batch = [tokenizer.apply_chat_template(b, tokenize=False) for b in batch]

    generation_config = GenerationConfig(
        max_new_tokens=512,
        **gen_config
    )
    model.config.use_cache = True
    model.use_cache = True
    model.eval()

    responses = []
    for i in tqdm(range(0, len(batch), batch_size)):
        inputs = tokenizer(batch[i:i+batch_size], add_special_tokens=False, return_tensors="pt", padding=True, truncation=True)
        outputs = model.generate(
            **inputs.to(DEVICE),
            generation_config=generation_config,
            pad_token_id=tokenizer.eos_token_id
        )
        outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        outputs = [o.split("[/INST]")[-1].strip() for o in outputs]
        responses.extend(outputs)
    return responses


def get_responses_openai(batch: list[list[str]], model: OpenAI, temperature=0.9) -> list[str]:
    batch = [[{
        "role": "user" if i % 2 == 0 else "assistant",
        "content": m
    } for i, m in enumerate(b)] for b in batch]
    responses = [model.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=b,
        max_tokens=512,
        temperature=temperature,
    ) for b in tqdm(batch)]
    return [r.choices[0].message.content.strip() for r in responses]


def construct_dpo_dataset(run_id: str, tokenizer: AutoTokenizer, is_positive: bool = True) -> Dataset:
    with open(f"/results/{run_id}/data.json") as f:
        dataset = json.load(f)
    dataset = dataset.copy()
    for k in list(dataset.keys()):
        if k not in ["prompt", "completion", "positive_completion"]:
            del dataset[k]

    dataset = Dataset.from_dict(dataset)
    dataset = dataset.map(lambda x: {
        "prompt": [{
            "role": "user" if i % 2 == 0 else "assistant",
            "content": m.format(prompt=x["prompt"]) if i == len(GET_COMPLETION) - 1 else m
        } for i, m in enumerate(GET_COMPLETION)],
        "chosen": x["positive_completion" if is_positive else "completion"],
        "rejected": x["completion" if is_positive else "positive_completion"]
    })
    dataset = dataset.map(lambda x: {
        "prompt": tokenizer.apply_chat_template(x["prompt"], tokenize=False),
        "chosen": x["chosen"],
        "rejected": x["rejected"]
    })
    return dataset


def construct_sft_dataset(run_id: str, tokenizer: AutoTokenizer, is_positive: bool = True) -> Dataset:
    with open(f"/results/{run_id}/data.json") as f:
        dataset = json.load(f)
    dataset = dataset.copy()
    for k in list(dataset.keys()):
        if k not in ["prompt", "positive_completion" if is_positive else "completion"]:
            del dataset[k]
    dataset = Dataset.from_dict(dataset)
    dataset = dataset.map(lambda x: {
        "text": [{
            "role": "user" if i % 2 == 0 else "assistant",
            "content": m.format(prompt=x["prompt"]) if i == len(GET_COMPLETION) - 1 else m
        } for i, m in enumerate(GET_COMPLETION)] + [{
            "role": "assistant",
            "content": x["positive_completion" if is_positive else "completion"]
        }],
    })
    dataset = dataset.map(lambda x: {
        "text": tokenizer.apply_chat_template(x["text"], tokenize=False)
    })
    return dataset


def find_all_linear_names(model, exclude: list[str]):
    cls = torch.nn.Linear
    lora_module_names = set()
    for name, module in model.named_modules():
        if any(keyword in name for keyword in exclude):
            continue
        if isinstance(module, cls):
            names = name.split('.')
            lora_module_names.add(names[-1])
    return list(lora_module_names)


@stub.function(
    volumes=VOLUME_CONFIG,
    cpu=4.0,
    gpu=gpu.A100(count=1),
    timeout=3600 * 12,
    mounts=[
        Mount.from_local_dir("configs", remote_path="/root/configs")
    ]
)
def train(arg_file: str, run_id: str, negative_run_ids: list[str] = []):
    """Returns path to model params"""

    # Parse args
    model_args, data_args, training_args = get_args(arg_file)
    assert training_args.algo in ["dpo", "sft"], f"Unknown algorithm {training_args.algo}"

    # Load model
    model = get_model(model_args)
    rank0_log_info("Loaded model")
    tokenizer = AutoTokenizer.from_pretrained(model_args.model_name_or_path, model_max_length=8000, padding_side="left")
    tokenizer.pad_token = tokenizer.eos_token
    rank0_log_info("Loaded tokenizer")
    stub.pretrained_volume.commit()

    # Construct dataset
    dataset_constructor = construct_dpo_dataset if training_args.algo == "dpo" else construct_sft_dataset
    dataset = dataset_constructor(run_id, tokenizer, is_positive=True)
    for neg_run_id in negative_run_ids:
        dataset = concatenate_datasets([dataset, dataset_constructor(neg_run_id, tokenizer, is_positive=False)])
    dataset = dataset.shuffle(seed=42)
    
    # Add LoRA config
    if training_args.lora_enable:
        peft_config = LoraConfig(
            r=training_args.lora_r, 
            lora_alpha=training_args.lora_alpha, 
            target_modules = find_all_linear_names(model, training_args.lora_exclude),
            lora_dropout=training_args.lora_dropout, 
            bias=training_args.lora_bias,
            task_type="CAUSAL_LM"
        )
    else: peft_config = None

    output_path = f"/results/{run_id}"
    if training_args.algo == "sft":
        output_path += "-sft"
    training_args.output_dir = output_path
    os.makedirs(output_path, exist_ok=True)
    dump_arg_dicts({
            "model_args": model_args,
            "data_args": data_args,
            "training_args": training_args
        }, output_path)
    training_args.run_name = run_id
    # Deactivate cache
    model.config.use_cache = False

    if training_args.algo == "dpo":
        trainer = DPOTrainer(
            model=model,
            args=training_args,
            beta=training_args.dpo_beta,
            train_dataset=dataset,
            tokenizer=tokenizer,
            peft_config=peft_config,
            callbacks=[PeftSavingCallback] if training_args.lora_enable else None
        )
    elif training_args.algo == "sft":
        response_template = "[/INST]"
        collator = DataCollatorForCompletionOnlyLM(response_template, tokenizer=tokenizer)
        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=dataset,
            tokenizer=tokenizer,
            dataset_text_field="text",
            data_collator=collator,
            max_seq_length=2048,
            peft_config=peft_config,
            callbacks=[PeftSavingCallback] if training_args.lora_enable else None
        )
    else:
        raise ValueError(f"Unknown algorithm {training_args.algo}")

    trainer.train()
    trainer.save_model()

    if training_args.report_to == "wandb":
        wandb.finish()

    # Deleting dataset to ensure there are no open files:
    del dataset

    stub.results_volume.commit()


@stub.function(
    volumes=VOLUME_CONFIG,
    cpu=4.0,
    gpu=gpu.L4(count=1),
    timeout=3600 * 12,
    mounts=[
        Mount.from_local_dir("configs", remote_path="/root/configs")
    ]
)
def sample_gpt4(arg_file: str, feedback: str, run_id: str):
    """Returns dataset as dict"""
    # Parse args
    _, data_args, _ = get_args(arg_file)

    # Load model
    model = get_openai_model()
    rank0_log_info("Loaded model")

    # Generate dataset
    prompts = get_responses_openai([SAMPLE_PROMPTS[:-1] + [SAMPLE_PROMPTS[-1].format(feedback=feedback)]] * data_args.train_samples, model)
    rank0_log_info(f"Generated prompts ([{', '.join(prompts[:3])}, ..])")
    completions = get_responses_openai([GET_COMPLETION[:-1] + [GET_COMPLETION[-1].format(prompt=p)] for p in prompts], model)
    rank0_log_info(f"Generated completions ([{', '.join(completions[:3])}, ..])")
    positive_completions = get_responses_openai([
        POSITIVE_COMPLETION[:-1] + [POSITIVE_COMPLETION[-1].format(prompt=p, completion=c, feedback=feedback)] for p, c in zip(prompts, completions)
    ], model)
    rank0_log_info(f"Generated positive completions ([{', '.join(positive_completions[:3])}, ..])")

    # Save dataset as json
    dataset = {
        "prompt": prompts,
        "completion": completions,
        "positive_completion": positive_completions
    }
    os.makedirs(f"/results/{run_id}", exist_ok=True)
    with open(f"/results/{run_id}/data.json", "w+") as f:
        json.dump(dataset, f)
    rank0_log_info(f"Saved dataset to /results/{run_id}/data.json")

    stub.results_volume.commit()


@stub.function(
    volumes=VOLUME_CONFIG,
    cpu=4.0,
    gpu=gpu.L4(count=1),
    timeout=3600 * 12,
    mounts=[
        Mount.from_local_dir("configs", remote_path="/root/configs")
    ]
)
def sample(arg_file: str, feedback: str, run_id: str):
    """Returns dataset as dict"""
    # Parse args
    model_args, data_args, _ = get_args(arg_file)

    # Load model
    model = get_model(model_args)
    rank0_log_info("Loaded model")
    tokenizer = AutoTokenizer.from_pretrained(model_args.model_name_or_path, model_max_length=8000, padding_side="left")
    tokenizer.pad_token = tokenizer.eos_token
    rank0_log_info("Loaded tokenizer")
    stub.pretrained_volume.commit()

    # Generate dataset
    categories = get_responses(
        [SAMPLE_PROMPT_CATEGORIES[:-1] + [SAMPLE_PROMPT_CATEGORIES[-1].format(feedback=feedback, count=max(data_args.train_samples // 8, 1))]],
        model,
        tokenizer,
        gen_config=SAMPLE_PROMPT_CATEGORIES_CONFIG)[0]
    
    # Need to add start of response included in prompt back in for parsing
    categories = [re.sub(r'[0-9]+. ', '', c).strip() for c in categories.split("\n") if c.strip() != ""]

    # Sample prompts
    prompts = get_responses(
        [SAMPLE_PROMPTS[:-1] + [SAMPLE_PROMPTS[-1].format(feedback=feedback, category=c, count=8)] for c in categories],
        model,
        tokenizer,
        gen_config=SAMPLE_PROMPTS_CONFIG)
    prompts = [[re.sub(r'[0-9]+. ', '', p).strip() for p in pr.split("\n") if p.strip() != ""] for pr in prompts]
    # Flatten & cutoff to just prompt
    prompts = [p.split("\n\n")[0] for pr in prompts for p in pr][:data_args.train_samples]
    rank0_log_info(f"Generated prompts ([{', '.join(prompts[:3])}, ..])")

    # Now generate baseline completions
    completions = get_responses(
        [GET_COMPLETION[:-1] + [GET_COMPLETION[-1].format(prompt=p)] for p in prompts],
        model,
        tokenizer,
        gen_config=GET_COMPLETION_CONFIG)
    rank0_log_info(f"Generated completions ([{', '.join(completions[:3])}, ..])")

    # Now generate improved completions
    positive_completions = get_responses(
        [POSITIVE_COMPLETION[:-1] + [POSITIVE_COMPLETION[-1].format(prompt=p, completion=c, feedback=feedback)] for p, c in zip(prompts, completions)],
        model,
        tokenizer,
        gen_config=POSITIVE_COMPLETION_CONFIG)
    rank0_log_info(f"Generated positive completions ([{', '.join(positive_completions[:3])}, ..])")

    # Save dataset as json
    dataset = {
        "categories": categories,
        "prompt": prompts,
        "completion": completions,
        "positive_completion": positive_completions
    }
    os.makedirs(f"/results/{run_id}", exist_ok=True)
    with open(f"/results/{run_id}/data.json", "w+") as f:
        json.dump(dataset, f)
    rank0_log_info(f"Saved dataset to /results/{run_id}/data.json")

    stub.results_volume.commit()


@stub.function(
    volumes=VOLUME_CONFIG,
    cpu=4.0,
    gpu=gpu.L4(count=1),
    timeout=3600 * 12,
    mounts=[
        Mount.from_local_dir("configs", remote_path="/root/configs")
    ]
)
def eval(arg_file: str, feedback: str, run_id: str) -> dict:
    # Parse args
    model_args, data_args, _ = get_args(arg_file)

    # Load model
    model = get_model(model_args)
    rank0_log_info("Loaded model")
    tokenizer = AutoTokenizer.from_pretrained(model_args.model_name_or_path, model_max_length=8000, padding_side="left")
    tokenizer.pad_token = tokenizer.eos_token
    rank0_log_info("Loaded tokenizer")
    stub.pretrained_volume.commit()

    # Generate dataset
    categories = get_responses(
        [SAMPLE_PROMPT_CATEGORIES[:-1] + [SAMPLE_PROMPT_CATEGORIES[-1].format(feedback=feedback, count=max(data_args.eval_samples // 8, 1))]],
        model,
        tokenizer,
        gen_config=SAMPLE_PROMPT_CATEGORIES_CONFIG)[0]
    
    # Need to add start of response included in prompt back in for parsing
    categories = [re.sub(r'[0-9]+. ', '', c).strip() for c in categories.split("\n") if c.strip() != ""]

    # Sample prompts
    prompts = get_responses(
        [SAMPLE_PROMPTS[:-1] + [SAMPLE_PROMPTS[-1].format(feedback=feedback, category=c, count=8)] for c in categories],
        model,
        tokenizer,
        gen_config=SAMPLE_PROMPTS_CONFIG)
    prompts = [[re.sub(r'[0-9]+. ', '', p).strip() for p in pr.split("\n") if p.strip() != ""] for pr in prompts]
    # Flatten & cutoff to just prompt
    eval_prompts = [p.split("\n\n")[0] for pr in prompts for p in pr][:data_args.eval_samples]
    rank0_log_info(f"Generated prompts ([{', '.join(eval_prompts[:3])}, ..])")

    # Now eval the baseline model
    eval_baseline_completions = get_responses(
        [GET_COMPLETION[:-1] + [GET_COMPLETION[-1].format(prompt=p)] for p in eval_prompts],
        model,
        tokenizer,
        gen_config=GET_COMPLETION_CONFIG)
    eval_baseline_reference_task_completions = get_responses(
        [GET_COMPLETION[:-1] + [GET_COMPLETION[-1].format(prompt=p)] for p in REFERENCE_TASK_PROMPTS],
        model,
        tokenizer,
        gen_config=REFERENCE_TASK_PROMPTS_CONFIG)
    rank0_log_info(f"Generated baseline completions ([{', '.join(eval_prompts[:3])}, ..])")

    # Now eval the trained model
    adapter_path = f"/results/{run_id}"
    model.load_adapter(adapter_path)
    eval_completions = get_responses(
        [GET_COMPLETION[:-1] + [GET_COMPLETION[-1].format(prompt=p)] for p in eval_prompts],
        model,
        tokenizer,
        gen_config=GET_COMPLETION_CONFIG)
    eval_reference_task_completions = get_responses(
        [GET_COMPLETION[:-1] + [GET_COMPLETION[-1].format(prompt=p)] for p in REFERENCE_TASK_PROMPTS],
        model,
        tokenizer,
        gen_config=REFERENCE_TASK_PROMPTS_CONFIG)
    rank0_log_info(f"Generated completions ([{', '.join(eval_prompts[:3])}, ..])")

    eval_dataset = {
        "prompt": eval_prompts,
        "completion": eval_completions,
        "baseline_completion": eval_baseline_completions,
        "reference_prompts": REFERENCE_TASK_PROMPTS,
        "reference_completion": eval_reference_task_completions,
        "baseline_reference_completion": eval_baseline_reference_task_completions
    }
    with open(f"/results/{run_id}/eval.json", "w+") as f:
        json.dump(eval_dataset, f)

    stub.results_volume.commit()


@stub.local_entrypoint()  # Runs locally to kick off remote training job.
def main(
    arg_file: str,
    feedback: str,
    run_id: str = "test",
    negative_run_id1: str = None,
    negative_run_id2: str = None,
    do_sample: bool = False,
    do_train: bool = False,
    do_eval: bool = False,
    use_openai: bool = False
):
    print(f"Welcome to Modal Feedback fine-tuning.")

    print(f"Beginning run {run_id=}.")
    if use_openai:
        run_id = f"openai-{run_id}"

    if do_sample and not use_openai:
        print("Sampling dataset.")
        sample.remote(arg_file, feedback, run_id)
    elif do_sample and use_openai:
        print("Sampling dataset.")
        sample_gpt4.remote(arg_file, feedback, run_id)
    if do_train:
        print("Training model.")
        negative_run_ids = []
        if negative_run_id1 is not None:
            negative_run_ids.append(negative_run_id1)
        if negative_run_id2 is not None:
            negative_run_ids.append(negative_run_id2)
        train.remote(arg_file, run_id, negative_run_ids)
    if do_eval:
        print("Evaluating model.")
        eval.remote(arg_file, feedback, run_id)
    print(f"Run completed {run_id=}.")
