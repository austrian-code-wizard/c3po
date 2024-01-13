from common import stub, VOLUME_CONFIG, N_GPUS, GPU_MEM
from modal import gpu

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"

@stub.function(
    volumes=VOLUME_CONFIG,
    cpu=8.0,
    gpu=gpu.A100(count=N_GPUS, memory=GPU_MEM),
    timeout=3600 * 12
)
def load():
    import torch
    from datasets import load_dataset
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

    load_dataset("meta-math/MetaMathQA", split="train")
    AutoTokenizer.from_pretrained(
        MODEL_ID)
    AutoModelForCausalLM.from_pretrained(MODEL_ID, load_in_4bit=True, torch_dtype=torch.float16, use_flash_attention_2=True)

    stub.pretrained_volume.commit()
    

@stub.function(
    volumes=VOLUME_CONFIG,
    cpu=8.0,
    gpu=gpu.A100(count=N_GPUS, memory=GPU_MEM),
    timeout=3600 * 12
)
def generate_preferences(num_rows: int, output_path: str, quant: str = None):
    import torch
    from typing import Dict
    from datasets import load_dataset
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

    dataset = load_dataset("meta-math/MetaMathQA", split="train")
    dataset = dataset.shuffle(seed=42)

    if num_rows is not None:
        dataset = dataset.select(range(num_rows))

    def extract_answer(sample) -> Dict[str, str]:
        return {
            "query": f'{sample["query"]}. Think step-by-step.',
            "type": sample["type"],
            "response": sample["response"],
            "answer": sample["response"].split("The answer is: ")[-1].strip()
        }

    dataset = dataset.map(extract_answer, num_proc=8)
    dataset = dataset.filter(lambda x: x["answer"].isnumeric(), num_proc=8)
    dataset = dataset.map(lambda x: {"chat": [{"role": "user", "content": x["query"]}]}, num_proc=8)

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_ID,
        model_max_length=2048,
        padding_side="left",
        add_eos_token=True,
        add_bos_token=True)

    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "left"

    dataset = dataset.map(lambda x: {"formatted_chat": tokenizer.apply_chat_template(x["chat"], tokenize=False, add_generation_prompt=True)}, num_proc=10)

    device = "cuda" # the device to load the model onto
    batch_size = 2

    model_args = {
        "use_flash_attention_2": True,
        "device_map": device,
        "torch_dtype": torch.float16
    }

    if quant == "8bit":
        model_args["load_in_8bit"] = True
    elif quant == "4bit":
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16
        )
        model_args["quantization_config"] = bnb_config
    

    model = AutoModelForCausalLM.from_pretrained(MODEL_ID, **model_args)
    model.config.use_cache = True

    for i in range(len(dataset)):
        batch = dataset.select([i for _ in range(batch_size)])
        print(f"--Inputs:")
        for j in range(len(batch["formatted_chat"])):
            print(f"\t{j}: {batch['formatted_chat'][j]}")

        model_inputs = tokenizer(batch["formatted_chat"], padding=True, truncation=True, add_special_tokens=False, return_tensors="pt").to(device)

        generated_ids = model.generate(**model_inputs, max_new_tokens=1000, do_sample=True, temperature=1.2)
        decoded = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        decoded = list(map(lambda x: x.split("[/INST]")[-1].strip(), decoded))
        print(f"--Outputs:")
        for j in range(len(decoded)):
            print(f"\t{j}: {decoded[j]}")

        model_inputs = map(lambda msgs, answer, resp: msgs + [
            {"role": "assistant", "content": resp},
            {"role": "user", "content": "Taking into account the reasoning above but also correcting reasoning errors, provide your final answer as a single number."},
            {"role": "assistant", "content": answer}], batch["chat"], batch["answer"], decoded)
        model_inputs = list(map(lambda msgs: tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True), model_inputs))
        print(f"--Final inputs:")
        for j in range(len(model_inputs)):
            print(f"\t{j}: {model_inputs[j]}")
        model_inputs = tokenizer(model_inputs, padding=True, truncation=True, return_tensors="pt").to(device)

        outputs = model(**model_inputs)
        logits = outputs.logits

        # Calculate the probability of the correct answer.
        eos_token_id = tokenizer.eos_token_id
        eoi_token_id = 28793

        # Find index of last occurence of eoi_token_id for each batch
        mask = model_inputs["input_ids"] == eoi_token_id
        indices = torch.arange(model_inputs["input_ids"].shape[1]).unsqueeze(0).expand_as(model_inputs["input_ids"]).to(device)
        masked_indices = torch.where(mask, indices, torch.tensor(-1))
        start_indices = torch.max(masked_indices, dim=1).values + 1

        mask = model_inputs["input_ids"] == eos_token_id
        indices = torch.arange(model_inputs["input_ids"].shape[1]).unsqueeze(0).expand_as(model_inputs["input_ids"]).to(device)
        masked_indices = torch.where(mask, indices, torch.tensor(-1))
        end_indices = torch.max(masked_indices, dim=1).values - 2

        logits = torch.stack([logits[i, start:end,:] for i, (start, end) in enumerate(zip(start_indices, end_indices))])
        logits = torch.nn.functional.softmax(logits, dim=-1)

        answer_tokens = tokenizer(batch["answer"], add_special_tokens=False, return_tensors="pt").to(device)

        # Calculate the probability of the correct answer.
        print(f"Checking alignment of answers... Decoded answer: {tokenizer.decode(model_inputs['input_ids'][0, start_indices[0]:end_indices[0]])}; Actual answer: {tokenizer.decode(answer_tokens['input_ids'][0,1:])}")
        answer_prob = torch.gather(logits, 2, answer_tokens["input_ids"][:,1:].unsqueeze(-1)).squeeze()
        answer_prob = torch.sum(answer_prob.log(), dim=1).detach().cpu()
        print(f"--Answer probabilities:")
        for j in range(len(answer_prob)):
            print(f"\t{j}: {answer_prob[j]}")



@stub.local_entrypoint()
def main(num_rows: int = None, output_path: str = "metarlaif_preferences", quant: str = "fp16"):
    generate_preferences.remote(num_rows, quant, output_path)