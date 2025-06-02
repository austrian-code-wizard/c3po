import os
import re
import json
import time
import copy
import hashlib
import threading
from functools import wraps
from typing import Optional, Literal, Any
from dataclasses import field, dataclass, asdict

import torch
from transformers import TrainingArguments as TransformerTrainingArguments, TrainerCallback, HfArgumentParser

from src.logger import logger
from src.dataset.feedback_utils import Scope, Type


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


DTYPES = {
    "bf16": torch.bfloat16,
    "f16": torch.float16,
    "f32": torch.float32
}


@dataclass
class ModelArguments:
    dtype: Optional[Literal["bf16", "f16", "f32"]] = "bf16"
    load_in_4bit: Optional[bool] = False
    load_in_8bit: Optional[bool] = False
    model_name_or_path: Optional[str] = "adept/fuyu-8b"
    platform: Optional[Literal["openai", "together", "huggingface"]] = "huggingface"


@dataclass
class PipelineModelsArguments:
   category_model: Optional[ModelArguments] = field(default_factory=ModelArguments)
   prompt_model: Optional[ModelArguments] = field(default_factory=ModelArguments)
   completion_model: Optional[ModelArguments] = field(default_factory=ModelArguments)
   train_model: Optional[ModelArguments] = field(default_factory=ModelArguments)
   qualitative_eval_model: Optional[ModelArguments] = field(default_factory=ModelArguments)
   
   def __post_init__(self):
        # TODO: figure out a way to not parse separately and preserve types
        self.category_model = ModelArguments(**self.category_model)
        self.prompt_model = ModelArguments(**self.prompt_model)
        self.completion_model = ModelArguments(**self.completion_model)
        self.train_model = ModelArguments(**self.train_model)
        self.qualitative_eval_model = ModelArguments(**self.qualitative_eval_model)


@dataclass
class SampleArguments:
    scope: Optional[list[Scope]] = field(default_factory= lambda: ["global_", "regional", "local"])
    type: Optional[list[Type]] = field(default_factory=lambda: ["quantitative", "qualitative"])
    train_test_split: float = 0.2 # percentage of data used for test set
    num_feedbacks: Optional[int] = 1
    prompts_per_category: Optional[int] = 16
    num_prompts: Optional[int] = 32
    num_negative_prompts: Optional[int] = 32
    num_general_prompts: Optional[int] = 32
    overwrite: Optional[bool] = False

    def __post_init__(self):
        # TODO: figure out a way to not parse separately and preserve types
        self.scope = [Scope[scope] for scope in self.scope]
        self.type = [Type[type] for type in self.type]


@dataclass
class TrainingArguments(TransformerTrainingArguments):
    algo: Literal["dpo", "sft", "sft_weighted", "lcdpo"] = "dpo"
    max_prompts: Optional[int] = None
    negative_prompt_ratio: float = 0.2
    general_prompt_ratio: float = 0.2
    filter_relevant_feedback: bool = False
    lora_enable: bool = False
    lora_r: int = 16
    lora_alpha: int = 32
    lora_dropout: float = 0.05
    lora_bias: str = "none"
    lora_exclude: list[str] = field(default_factory=list)
    dpo_beta: float = 0.1
    lcdpo_temp: float = 5
    lcdpo_lambda: float = 0.5
    lcdpo_sigma_soft: float = 0.3
    lcdpo_sigma_hard: float = 0.3
    lcdpo_avg_kl: bool = False
    lcdpo_l2: bool = False
    lcdpo_custom_sft_loss: bool = False
    wandb_project: Optional[str] = None
    eval_split: float = 0.05
    multi_feedback_training: bool = False
    use_base_prefix: Optional[str] = None


@dataclass
class EvalArguments:
    method: Literal["trained", "in_context", "cot", "revised"] = "trained"
    num_prompts: Optional[int] = None
    num_negative_prompts: Optional[int] = None
    num_general_prompts: Optional[int] = None
    eval_answer_quality: bool = True


class PeftSavingCallback(TrainerCallback):
    def on_save(self, args, state, control, **kwargs):
        checkpoint_path = os.path.join(args.output_dir, f"checkpoint-{state.global_step}")
        kwargs["model"].save_pretrained(checkpoint_path)


class TrainingLoggingCallback(TrainerCallback):
    def __init__(self):
        self.start_time = None
        self.step_start_time = None
        
    def on_train_begin(self, args, state, control, **kwargs):
        import time
        self.start_time = time.time()
        
        logger.info("=" * 60)
        logger.info("TRAINING STARTED")
        logger.info("=" * 60)
        logger.info(f"Algorithm: {args.algo}")
        logger.info(f"Model: {getattr(args, 'model_name_or_path', 'Unknown')}")
        logger.info(f"Total epochs: {args.num_train_epochs}")
        logger.info(f"Max steps: {state.max_steps}")
        logger.info(f"Batch size per device: {args.per_device_train_batch_size}")
        logger.info(f"Gradient accumulation steps: {args.gradient_accumulation_steps}")
        logger.info(f"Learning rate: {args.learning_rate}")
        logger.info(f"Logging steps: {args.logging_steps}")
        logger.info(f"Save steps: {args.save_steps}")
        if hasattr(args, 'eval_steps') and args.eval_steps:
            logger.info(f"Eval steps: {args.eval_steps}")
        logger.info("=" * 60)
        
    def on_epoch_begin(self, args, state, control, **kwargs):
        logger.info(f"Starting Epoch {state.epoch:.2f}/{args.num_train_epochs}")
        
    def on_step_begin(self, args, state, control, **kwargs):
        import time
        self.step_start_time = time.time()
        
    def on_step_end(self, args, state, control, **kwargs):
        if self.step_start_time and state.global_step % args.logging_steps == 0:
            import time
            step_time = time.time() - self.step_start_time
            progress_pct = (state.global_step / state.max_steps) * 100 if state.max_steps > 0 else 0
            
            logger.info(f"Step {state.global_step}/{state.max_steps} "
                       f"({progress_pct:.1f}%) - "
                       f"Epoch {state.epoch:.2f} - "
                       f"Step time: {step_time:.2f}s")
                       
    def on_log(self, args, state, control, logs=None, **kwargs):
        if logs is None:
            return
            
        filtered_logs = {}
        for key, value in logs.items():
            if key in ['loss', 'learning_rate', 'epoch', 'grad_norm']:
                filtered_logs[key] = value
            elif 'loss' in key.lower():
                filtered_logs[key] = value
                
        if filtered_logs:
            log_str = " | ".join([f"{k}: {v:.6f}" if isinstance(v, float) else f"{k}: {v}" 
                                 for k, v in filtered_logs.items()])
            logger.info(f"Metrics - {log_str}")
            
        if hasattr(args, 'algo'):
            if args.algo == 'lcdpo' and any('kd_loss' in key for key in logs.keys()):
                kd_losses = {k: v for k, v in logs.items() if 'kd_loss' in k or 'target_loss' in k or 'dpo_loss' in k}
                if kd_losses:
                    kd_str = " | ".join([f"{k}: {v:.6f}" for k, v in kd_losses.items()])
                    logger.info(f"LCDPO Losses - {kd_str}")
                    
    def on_evaluate(self, args, state, control, **kwargs):
        logger.info(f"Running evaluation at step {state.global_step}")
        
    def on_save(self, args, state, control, **kwargs):
        logger.info(f"Saving checkpoint at step {state.global_step}")
        
    def on_epoch_end(self, args, state, control, **kwargs):
        logger.info(f"Completed Epoch {state.epoch:.2f}")
        
    def on_train_end(self, args, state, control, **kwargs):
        import time
        if self.start_time:
            total_time = time.time() - self.start_time
            hours = int(total_time // 3600)
            minutes = int((total_time % 3600) // 60)
            seconds = int(total_time % 60)
            
            logger.info("=" * 60)
            logger.info("TRAINING COMPLETED")
            logger.info("=" * 60)
            logger.info(f"Total training time: {hours:02d}:{minutes:02d}:{seconds:02d}")
            logger.info(f"Total steps completed: {state.global_step}")
            logger.info(f"Final epoch: {state.epoch:.2f}")
            if state.best_metric is not None:
                logger.info(f"Best metric: {state.best_metric:.6f}")
            logger.info("=" * 60)

        if "pytorch_model.bin" in os.listdir(checkpoint_path):
            os.remove(os.path.join(checkpoint_path, "pytorch_model.bin"))


def dump_arg_dicts(arg_dicts: dict[str, dict[str, Any]], output_dir: str, filename: str = "arg_dict.json"):
    arg_dict = {name: asdict(arg) for name, arg in arg_dicts.items()}

    # Create output dir if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, filename), "w") as f:
        json.dump(arg_dict, f, indent=2)


def get_args(arg_dict: dict[str, Any]) -> tuple[PipelineModelsArguments, SampleArguments, TrainingArguments, EvalArguments]:
    modal_arg_dict = arg_dict["model_args"]
    sample_arg_dict = arg_dict["sample_args"]
    training_arg_dict = arg_dict["training_args"]
    eval_arg_dict = arg_dict["eval_args"]

    # TODO: figure out a way to not parse separately and preserve types
    model_arg_parser = HfArgumentParser(PipelineModelsArguments)
    model_args: PipelineModelsArguments = model_arg_parser.parse_dict(modal_arg_dict)[0]
    sample_arg_parser = HfArgumentParser(SampleArguments)
    sample_args: SampleArguments = sample_arg_parser.parse_dict(sample_arg_dict)[0]
    training_arg_parser = HfArgumentParser(TrainingArguments)
    training_args: TrainingArguments = training_arg_parser.parse_dict(training_arg_dict)[0]
    eval_arg_parser = HfArgumentParser(EvalArguments)
    eval_args: EvalArguments = eval_arg_parser.parse_dict(eval_arg_dict)[0]
    return model_args, sample_args, training_args, eval_args


def find_all_linear_names(model, exclude: list[str]):
    """Finds all linear layer names in a model."""
    cls = torch.nn.Linear
    lora_module_names = set()
    for name, module in model.named_modules():
        if any(keyword in name for keyword in exclude):
            continue
        if isinstance(module, cls):
            names = name.split('.')
            lora_module_names.add(names[-1])
    return list(lora_module_names)


def format_messages(batch: list[list[str]]) -> list[list[dict[str, str]]]:
    """Assumes batch is a list of lists of strings, where each inner list is a list of chat messages that alternate between user and assistant."""
    return [[{
        "role": "user" if i % 2 == 0 else "assistant",
        "content": m
    } for i, m in enumerate(b)] for b in batch]


def split_numbered_list(text: str) -> list[str]:
    """Splits a numbered list into a list of strings, where each string is a numbered item in the list."""
    text = '\n' + text
    regex = r"\n[0-9]+. "
    return [t.strip() for t in re.split(regex, text) if t.strip()]


def throttle(lock: threading.Lock, rqi: int, last_requests: list[float], interval: int = 60) -> None:
    """Decorator to throttle the number of requests per interval.

    Args:
    lock: Lock to make checking the limit and sending requests thread-safe
    rqi: Requests per interval limit
    last_requests: List to store timestamps of the last requests
    interval: Interval in seconds to check the number of requests
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_requests
            while True:
                with lock:
                    # Remove timestamps older than 60 seconds
                    now = time.time()
                    last_requests = [req for req in last_requests if now - req < interval]
                    # If the number of requests in the last minute is less than the limit, send a new request
                    if len(last_requests) < rqi:
                        last_requests.append(now)
                        break
                    # Otherwise, wait for some time and try again
                    minimum = min([now - req for req in last_requests])
                time.sleep(minimum)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def catch_error_return_none(func):
    """Decorator to log a warning if an error occurs but catches the error and returns None."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.warning(f"An error occurred in {func.__name__}: {e}")
            return None
    return wrapper


defaults = {
    "beta": 0.1,
    "sigma_soft": 0.2,
    "sigma_hard": 0.1,
    "hard": 0.2,
    "soft": 0.1,
    "lr": 5e-5,
    "r": 32,
    "alpha": 64,
    "epochs": 1,
    "max_prompts": None,
    "multi_feedback_training": False,
    "model_name_or_path": "mistralai/Mistral-7B-Instruct-v0.2",
    "use_base_prefix": None
}

def get_train_file_name(training_args: TrainingArguments, model_args: ModelArguments) -> str:
    file_name_parts = [training_args.algo]
    
    def append_if_different(arg_value, key):
        if arg_value != defaults[key]:
            arg_value = str(arg_value).replace("/", "-")
            file_name_parts.append(f"-{arg_value}-{key}")

    if training_args.algo in ["dpo", "lcdpo"]:
        append_if_different(training_args.dpo_beta, "beta")
    if training_args.algo == "lcdpo":
        append_if_different(training_args.lcdpo_sigma_soft, "sigma_soft")
        append_if_different(training_args.lcdpo_sigma_hard, "sigma_hard")
    else:
        append_if_different(training_args.negative_prompt_ratio, "hard")
        append_if_different(training_args.general_prompt_ratio, "soft")
    
    append_if_different(training_args.learning_rate, "lr")
    
    if training_args.lora_enable:
        append_if_different(training_args.lora_r, "r")
        append_if_different(training_args.lora_alpha, "alpha")
    
    append_if_different(training_args.num_train_epochs, "epochs")
    append_if_different(model_args.model_name_or_path, "model_name_or_path")
    append_if_different(training_args.use_base_prefix, "use_base_prefix")
    
    if training_args.multi_feedback_training:
        file_name_parts.append("-multi")

    if training_args.filter_relevant_feedback:
        file_name_parts.append("-filtered")

    if training_args.lcdpo_avg_kl:
        file_name_parts.append("-avgkl")
    
    append_if_different(training_args.max_prompts, "max_prompts")
    
    # Serialize training_args and generate a short hash to ensure any parameter changes are reflected in the file name
    args_copy = copy.deepcopy(training_args)
    del args_copy.logging_dir
    short_hash = hashlib.sha1(args_copy.to_json_string().encode()).hexdigest()[:8]
    file_name_parts.append(f"-{short_hash}")
    
    return ''.join(file_name_parts)


def print_num_trainable_params(model):
    trainable_params = sum(p.numel()
                           for p in model.parameters() if p.requires_grad)
    all_params = sum(p.numel() for p in model.parameters())
    logger.info(f"Trainable params: {trainable_params}/{all_params} ({trainable_params/all_params:.2%})")


def find_file_with_prefix(path: str, prefix: str) -> str:
    """Finds the file in the directory with the given prefix."""
    for file in os.listdir(path):
        if file.startswith(prefix):
            return file
    raise FileNotFoundError(f"No file with prefix {prefix} found in {path}")
