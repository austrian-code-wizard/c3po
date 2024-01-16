import os
import argparse
from time import sleep

import wandb
from peft import LoraConfig
from trl import DPOTrainer, SFTTrainer, DataCollatorForCompletionOnlyLM

from src.logger import logger
from src.models import get_model
from src.dataset.format import to_dpo, to_sft
from src.dataset.feedback import Feedback, all_feedback
from src.utils import get_args, find_all_linear_names, dump_arg_dicts, PeftSavingCallback


def train(arg_file: str, run_id: str, data_dir: str, feedback: Feedback) -> None:
    model_args, _, training_args, _ = get_args(arg_file)
    
    # Load feedback
    run_dir = os.path.join(data_dir, run_id, "sample")
    logger.info(f"Training using data for run {run_id}, stored in {run_dir}")
    if not feedback.can_load_dataset(run_dir):
        raise ValueError(f"Feedback \"{feedback.content}\" has not been sampled yet")
    feedback.load_dataset(run_dir)
    logger.info(f"Loaded feedback \"{feedback.content}\"")

    run_dir = os.path.join(data_dir, run_id, "train")
    assert training_args.algo in ["dpo", "sft"], f"Unknown algorithm {training_args.algo}"
    run_dir = os.path.join(run_dir, training_args.algo)
    run_dir = run_dir + ("-negatives" if training_args.num_negative_prompts > 0 else "-no_negatives")

    # Load model
    assert model_args.train_model.platform == "huggingface", "Only HuggingFace models are supported for training"
    model = get_model(model_args.train_model)
    logger.info("Loaded model")


    # Construct dataset
    dataset_constructor = to_dpo if training_args.algo == "dpo" else to_sft
    dataset = dataset_constructor(
        model.tokenizer,
        feedback.prompts["train"].shuffle(seed=42).select(range(training_args.num_prompts)),
        feedback.negative_prompts["train"].shuffle(seed=42).select(range(training_args.num_negative_prompts)) if training_args.num_negative_prompts > 0 else None)
    dataset = dataset.shuffle(seed=42)
    
    # Add LoRA config
    assert training_args.lora_enable, "Currently only LoRA training is supported"
    if training_args.lora_enable:
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

    if training_args.algo == "dpo":
        trainer = DPOTrainer(
            model=model.model,
            max_length=2048,
            max_prompt_length=1024,
            args=training_args,
            beta=training_args.dpo_beta,
            train_dataset=dataset,
            tokenizer=model.tokenizer,
            peft_config=peft_config,
            callbacks=[PeftSavingCallback] if training_args.lora_enable else None
        )
    elif training_args.algo == "sft":
        model.tokenizer.padding_side = 'right'
        response_template = "[/INST]"
        collator = DataCollatorForCompletionOnlyLM(response_template, tokenizer=model.tokenizer)
        trainer = SFTTrainer(
            model=model.model,
            args=training_args,
            train_dataset=dataset,
            tokenizer=model.tokenizer,
            dataset_text_field="text",
            data_collator=collator,
            max_seq_length=2048,
            peft_config=peft_config,
            callbacks=[PeftSavingCallback] if training_args.lora_enable else None
        )
    else:
        raise ValueError(f"Unknown algorithm {training_args.algo}")

    trainer.train()
    trainer.save_model(run_dir)
    logger.info(f"Saved model for run {run_id}, to {run_dir}")

    if training_args.report_to == "wandb":
        wandb.finish()
    
    # Sometimes Wandb needs more time to close resources
    sleep(2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("arg_file", type=str)
    parser.add_argument("run_id", type=str)
    parser.add_argument("--data_dir", type=str, default="./data")
    parser.add_argument("--feedback_prefix", type=str, default=None)
    args = parser.parse_args()

    feedback = all_feedback
    if args.feedback_prefix is not None:
        feedback = [f for f in feedback if f.content.startswith(args.feedback_prefix)]
    train(args.arg_file, args.run_id, args.data_dir, feedback)
