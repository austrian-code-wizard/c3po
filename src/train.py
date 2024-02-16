import os
import json
import argparse
from time import sleep
from typing import Any, Tuple

import wandb
from peft import LoraConfig, PeftModel
from datasets import Dataset, concatenate_datasets
from trl import DPOTrainer, SFTTrainer, DataCollatorForCompletionOnlyLM

from src.logger import logger
from src.models import get_model
from src.dataset.feedback_utils import Feedback, Type
from src.lcdpo import LocallyConstrainedDPOTrainer
from src.sft_weighted import WeightedSFTTrainer
from src.dataset.format import to_dpo, to_sft, to_lcdpo, to_sft_weighted
from src.feedback import manual_feedback as all_feedback
from src.utils import get_args, find_all_linear_names, dump_arg_dicts, PeftSavingCallback, get_train_file_name, print_num_trainable_params, TrainingArguments, find_file_with_prefix


def filter_relevant_feedback(feedback: Feedback, prompts: Dataset | None) -> Dataset | None:
    """Filter out prompts where the revision is not better than the baseline"""
    if prompts is None:
        return None
    
    # TODO: enable this for quantitative feedback
    # TODO: add support to define "better" using a margin rather than just binary comparison
    if isinstance(feedback.metric, list):
        metric = lambda x: all([f(x, v) for f, v in zip(feedback.metric, feedback.metric_value)])
    else:
        metric = lambda x: feedback.metric(x, feedback.metric_value)
    return prompts.filter(lambda x: feedback.comparison(
        metric(x["baseline_response"]),
        metric(x["revised_response"])
    ))


def get_prompts(feedback: Feedback, training_args: TrainingArguments) -> Tuple[Dataset, Dataset, Dataset]:
    # Fetch dataset
    prompts = feedback.prompts["train"].shuffle(seed=42)
    negative_prompts = feedback.negative_prompts["train"].shuffle(seed=42)
    general_prompts = feedback.general_prompts["train"].shuffle(seed=42)

    # Filter out prompts where the revision is not better than the baseline
    if training_args.filter_relevant_feedback:
        assert feedback.type == Type.quantitative, "Filtering relevant feedback is currently only supported for quantitative feedback"
        prompts = filter_relevant_feedback(feedback, prompts)
        negative_prompts = filter_relevant_feedback(feedback, negative_prompts)
        general_prompts = filter_relevant_feedback(feedback, general_prompts)

    if training_args.max_prompts is not None:
        prompts = prompts.select(range(min(training_args.max_prompts, len(prompts))))
        logger.info(f"Using {len(prompts)} prompts")

    if training_args.negative_prompt_ratio > 0 and training_args.algo != "lcdpo" and training_args.algo != "sft_weighted":
        num_negative_prompts = int(training_args.negative_prompt_ratio * len(prompts))
        negative_prompts = negative_prompts.select(range(num_negative_prompts))
        logger.info(f"Using {len(negative_prompts)} negative prompts")

    if training_args.general_prompt_ratio > 0 and training_args.algo != "lcdpo" and training_args.algo != "sft_weighted":
        num_general_prompts = int(training_args.general_prompt_ratio * len(prompts))
        general_prompts = general_prompts.select(range(num_general_prompts))
        logger.info(f"Using {len(general_prompts)} general prompts")

    return prompts, negative_prompts, general_prompts


def train(arg_dict: dict[str, Any], run_id: str, data_dir: str, feedback: Feedback, second_feedback: Feedback = None) -> None:
    model_args, _, training_args, _ = get_args(arg_dict)
    
    # Load feedback
    run_dir = os.path.join(data_dir, run_id, "sample")
    logger.info(f"Training using data for run {run_id}, stored in {run_dir}")
    if not feedback.can_load_dataset(run_dir):
        raise ValueError(f"Feedback \"{feedback.content}\" has not been sampled yet")
    feedback.load_dataset(run_dir)
    logger.info(f"Loaded feedback \"{feedback.content}\"")

    # Load second feedback if given
    if second_feedback is not None:
        assert training_args.multi_feedback_training, "Must set multi_feedback_training to True when providing a second feedback"
        if not second_feedback.can_load_dataset(run_dir):
            raise ValueError(f"Feedback \"{second_feedback.content}\" has not been sampled yet")
        second_feedback.load_dataset(run_dir)
    elif training_args.multi_feedback_training and second_feedback is None:
        raise ValueError("Must provide a second feedback when multi_feedback_training is True")

    run_dir = os.path.join(data_dir, run_id, "train")
    assert training_args.algo in ["dpo", "sft", "lcdpo", "sft_weighted"], f"Unknown algorithm {training_args.algo}"
    train_dir = get_train_file_name(training_args, model_args.train_model)
    run_dir = os.path.join(run_dir, feedback.file_name)

    # If training on multiple feedbacks, reflect that in the run directory
    if training_args.multi_feedback_training:
        run_dir = os.path.join(run_dir, second_feedback.file_name)
    run_dir = os.path.join(run_dir, train_dir)

    # Load model
    assert model_args.train_model.platform == "huggingface", "Only HuggingFace models are supported for training"
    model = get_model(model_args.train_model)
    logger.info("Loaded model")

    prompts, negative_prompts, general_prompts = get_prompts(feedback, training_args)
    if training_args.multi_feedback_training:
        prompts2, negative_prompts2, general_prompts2 = get_prompts(second_feedback, training_args)
        prompts = concatenate_datasets([prompts, prompts2])
        negative_prompts = concatenate_datasets([negative_prompts, negative_prompts2])
        general_prompts = concatenate_datasets([general_prompts, general_prompts2])
        logger.info(f"Using {len(prompts)} combined prompts")

    # Format dataset for specific training algorithm
    if training_args.algo == "dpo":
        dataset_constructor = to_dpo
    elif training_args.algo == "sft":
        dataset_constructor = to_sft
    elif training_args.algo == "lcdpo":
        dataset_constructor = to_lcdpo
    elif training_args.algo == "sft_weighted":
        dataset_constructor = to_sft_weighted
    else:
        raise ValueError(f"Unknown algorithm {training_args.algo}")

    dataset = dataset_constructor(
        prompts,
        negative_prompts if (training_args.negative_prompt_ratio > 0 or training_args.algo == "lcdpo" or training_args.algo == "sft_weighted") else None,
        general_prompts if (training_args.negative_prompt_ratio > 0 or training_args.algo == "lcdpo" or training_args.algo == "sft_weighted") else None,
        model_args.train_model.model_name_or_path)
    

        # Load base training arg adapter if given
    if training_args.use_base_prefix is not None:
        base_run_dir = os.path.join(data_dir, run_id, "train", feedback.file_name)
        adapter_name = find_file_with_prefix(base_run_dir, training_args.use_base_prefix)
        model.model = PeftModel.from_pretrained(model.model, os.path.join(base_run_dir, adapter_name), is_trainable=True)
        logger.info(f"Loaded base training model from {base_run_dir}")
    
    # Add LoRA config
    assert training_args.lora_enable, "Currently only LoRA training is supported"
    if training_args.lora_enable and training_args.use_base_prefix is None:
        peft_config = LoraConfig(
            r=training_args.lora_r, 
            lora_alpha=training_args.lora_alpha, 
            target_modules = find_all_linear_names(model.model, training_args.lora_exclude),
            lora_dropout=training_args.lora_dropout, 
            bias=training_args.lora_bias,
            task_type="CAUSAL_LM"
        )
    else: peft_config = None

    training_args.output_dir = run_dir
    os.makedirs(run_dir, exist_ok=True)
    # TODO: add dummping args dict

    # Generating run name as feedback + feedback_id + algo + use_negatives
    training_args.run_name = "-".join(run_dir.split("/")[-2:])

    # Deactivate cache
    model.model.config.use_cache = False

    # Create eval dataset
    dataset = dataset.train_test_split(test_size=training_args.eval_split, seed=42, shuffle=True)
    eval_dataset = dataset["test"]
    dataset = dataset["train"]

    logger.info(f"Training on {len(dataset)} prompts, evaluating on {len(eval_dataset)} prompts for feedback \"{feedback.content}\"")

    # TODO: hacky, remove
    if model_args.train_model.model_name_or_path in ["tiiuae/falcon-7b-instruct", "01-ai/Yi-6B-Chat", "Qwen/Qwen-7B-Chat"]:
        response_template = "<|im_start|>assistant\n"
    elif model_args.train_model.model_name_or_path == "NousResearch/Nous-Hermes-llama-2-7b":
        response_template = "Response:\n"
    else:
        response_template = "[/INST]"

    if training_args.algo == "dpo":
        model.tokenizer.padding_side = 'left'
        trainer = DPOTrainer(
            model=model.model,
            max_length=2048,
            max_prompt_length=1024,
            args=training_args,
            beta=training_args.dpo_beta,
            train_dataset=dataset,
            eval_dataset=eval_dataset,
            tokenizer=model.tokenizer,
            peft_config=peft_config,
            callbacks=[PeftSavingCallback] if training_args.lora_enable else None
        )
    elif training_args.algo == "lcdpo":
        model.tokenizer.padding_side = 'left'
        trainer = LocallyConstrainedDPOTrainer(
            model=model.model,
            max_length=2048,
            max_prompt_length=1024,
            args=training_args,
            beta=training_args.dpo_beta,
            kd_lambda=training_args.lcdpo_lambda,
            kd_temperature=training_args.lcdpo_temp,
            sigma_soft=training_args.lcdpo_sigma_soft,
            sigma_hard=training_args.lcdpo_sigma_hard,
            use_avg_kl=training_args.lcdpo_avg_kl,
            custom_sft_loss=training_args.lcdpo_custom_sft_loss,
            train_dataset=dataset,
            eval_dataset=eval_dataset,
            tokenizer=model.tokenizer,
            response_template=response_template,
            peft_config=peft_config,
            callbacks=[PeftSavingCallback] if training_args.lora_enable else None
        )
    elif training_args.algo == "sft":
        model.tokenizer.padding_side = 'right'
        collator = DataCollatorForCompletionOnlyLM(response_template, tokenizer=model.tokenizer)
        trainer = SFTTrainer(
            model=model.model,
            args=training_args,
            train_dataset=dataset,
            eval_dataset=eval_dataset,
            tokenizer=model.tokenizer,
            data_collator=collator,
            max_seq_length=2048,
            peft_config=peft_config,
            callbacks=[PeftSavingCallback] if training_args.lora_enable else None
        )
    elif training_args.algo == "sft_weighted":
        model.tokenizer.padding_side = 'right'
        collator = DataCollatorForCompletionOnlyLM(response_template, tokenizer=model.tokenizer)
        training_args.evaluation_strategy = "no" # TODO: getting error during eval
        trainer = WeightedSFTTrainer(
            model=model.model,
            args=training_args,
            train_dataset=dataset,
            # eval_dataset=eval_dataset, # TODO: getting error during eval
            dataset_text_field="text",
            tokenizer=model.tokenizer,
            data_collator=collator,
            max_seq_length=2048,
            sigma_soft=training_args.lcdpo_sigma_soft,
            sigma_hard=training_args.lcdpo_sigma_hard,
            peft_config=peft_config,
            callbacks=[PeftSavingCallback] if training_args.lora_enable else None
        )
    else:
        raise ValueError(f"Unknown algorithm {training_args.algo}")

    print_num_trainable_params(trainer.model)
    trainer.train()
    trainer.save_model(run_dir)
    logger.info(f"Saved model for run {run_id}, to {run_dir}")

    if training_args.report_to == "wandb":
        wandb.finish()
    
    # Sometimes Wandb needs more time to close resources
    sleep(2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg_file", type=str)
    parser.add_argument("--run_id", type=str)
    parser.add_argument("--data_dir", type=str, default="./data")
    parser.add_argument("--feedback_prefix", type=str, default=None)
    args = parser.parse_args()

    with open(args.arg_file, "r") as f:
        arg_dict = json.load(f)

    feedback = all_feedback
    if args.feedback_prefix is not None:
        feedback = [f for f in feedback if f.content.startswith(args.feedback_prefix)]
    
    for f in feedback:
        train(arg_dict, args.run_id, args.data_dir, f)
