import os
import re
import json
import time
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
    algo: Literal["dpo", "sft", "lcdpo"] = "dpo"
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
    wandb_project: Optional[str] = None


@dataclass
class EvalArguments:
    algo: Literal["dpo", "sft"] = "dpo"
    num_prompts: int = 9999999
    num_negative_prompts: int = 9999999
    num_general_prompts: int = 9999999


class PeftSavingCallback(TrainerCallback):
    def on_save(self, args, state, control, **kwargs):
        checkpoint_path = os.path.join(args.output_dir, f"checkpoint-{state.global_step}")
        kwargs["model"].save_pretrained(checkpoint_path)

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


def get_train_file_name(training_args: TrainingArguments) -> str:
    file_name = training_args.algo
    if training_args.algo == "dpo" or training_args.algo == "lcdpo":
        file_name += f"-{training_args.dpo_beta}-beta"
    if training_args.algo == "lcdpo":
        file_name += f"-{training_args.lcdpo_temp}-temp"
        file_name += f"-{training_args.lcdpo_lambda}-lambda"
        file_name += f"-{training_args.lcdpo_sigma_soft}-sigma_soft"
        file_name += f"-{training_args.lcdpo_sigma_hard}-sigma_hard"
    if training_args.algo != "lcdpo":
        file_name += f"-{training_args.negative_prompt_ratio}-negatives"
        file_name += f"-{training_args.general_prompt_ratio}-general"
    file_name += f"-{training_args.learning_rate}-lr"
    if training_args.lora_enable:
        file_name += f"-{training_args.lora_r}-r"
        file_name += f"-{training_args.lora_alpha}-alpha"
    file_name += f"-{training_args.num_train_epochs}-epochs"
    return file_name
