import os
import json
import argparse
from typing import Any, Literal

import numpy as np
from datasets import Dataset, DatasetDict
np.random.seed(42)

from src.logger import logger
from src.models import get_model
from src.dataset.feedback_utils import Feedback
from src.feedback import manual_feedback as all_feedback
from src.dataset.general_prompts import GeneralPromptDataset
from src.utils import get_args, split_numbered_list, ModelArguments
from src.dataset.prompts import (
    SAMPLE_PROMPT_CATEGORIES,
    SAMPLE_PROMPT_CATEGORIES_CONFIG,
    SAMPLE_PROMPTS,
    SAMPLE_PROMPTS_CONFIG,
    SAMPLE_NEGATIVE_PROMPTS,
    SAMPLE_NEGATIVE_PROMPTS_CONFIG,
    GET_BASELINE_COMPLETION,
    GET_BASELINE_COMPLETION_CONFIG,
    GET_IN_CONTEXT_COMPLETION,
    GET_IN_CONTEXT_COMPLETION_CONFIG,
    GET_COMPLETION_REVISED,
    GET_COMPLETION_REVISED_CONFIG,
    GET_COT_COMPLETION,
    GET_COT_COMPLETION_CONFIG,
)


def sample_categories(feedback: list[Feedback], model_args: ModelArguments, num_categories: int):
    """Sample categories for feedback and update feedback in-place"""
    category_model = get_model(model_args)
    responses = category_model.get_responses(
        [[SAMPLE_PROMPT_CATEGORIES.format(count=num_categories, topic=f.domain)] for f in feedback],
        SAMPLE_PROMPT_CATEGORIES_CONFIG
    )

    # We cannot tolerate failed API calls here
    assert all([r is not None for r in responses]), "Category generation failed"

    responses = [r.split("REVISED_CATEGORIES:")[-1].strip() for r in responses]
    responses = [split_numbered_list(r) for r in responses]
    assert all([len(r) == num_categories for r in responses]), "Category generation failed"
    for f, r in zip(feedback, responses):
        f.categories = r


def sample_prompts(feedback: list[Feedback], model_args: ModelArguments, num_prompts: int, prompts_per_category: int, negative: bool = False):
    """Sample prompts for feedback and update feedback in-place"""
    prompt = SAMPLE_PROMPTS if not negative else SAMPLE_NEGATIVE_PROMPTS
    prompt_config = SAMPLE_PROMPTS_CONFIG if not negative else SAMPLE_NEGATIVE_PROMPTS_CONFIG

    prompt_model = get_model(model_args)

    # Get responses for flattened list of prompts
    responses = prompt_model.get_responses(
        [[prompt.format(count=prompts_per_category, domain=f.domain, category=c)]
         for f in feedback for c in f.categories],
    prompt_config)

    # We cannot tolerate failed API calls here
    assert all([r is not None for r in responses]), "Prompt generation failed"

    if negative:
        # We are using revisions in our prompting format to make negative examples more robust
        responses = [r.split("REVISED_PROMPTS:")[-1].strip() for r in responses]

    # Num responses (= num feedbacks x num categories) x num prompts per category
    responses = [prompt for r in responses for prompt in split_numbered_list(r)]

    # Split responses into lists of prompts for each feedback
    responses = np.array_split(responses, len(feedback))
    responses = [r.tolist()[:num_prompts] for r in responses]
    assert all([len(r) == num_prompts for r in responses]), "Prompt generation failed"

    for f, r in zip(feedback, responses):
        dataset = Dataset.from_dict({
            "prompt": r
        })
        if not negative:
            f.prompts = dataset
        else:
            f.negative_prompts = dataset


def add_general_prompts(feedback: list[Feedback], data_dir: str, num_prompts: int):
    """Add general prompts to feedback and update feedback in-place"""
    for f in feedback:
        f.general_prompts = GeneralPromptDataset.load(data_dir, num_prompts)


def sample_completions(feedback: list[Feedback], model_args: ModelArguments, prompt_type: Literal["prompts", "negative_prompts", "general_prompts"]):
    """Sample completions for feedback and update feedback in-place"""

    completion_model = get_model(model_args)

    if prompt_type == "prompts":
        datasets = [f.prompts for f in feedback]
    elif prompt_type == "negative_prompts":
        datasets = [f.negative_prompts for f in feedback]
    elif prompt_type == "general_prompts":
        datasets = [f.general_prompts for f in feedback]
    else:
        raise ValueError(f"Invalid prompt type: {prompt_type} (must be one of 'prompts', 'negative_prompts', 'general_prompts')")

    num_prompts = [len(dataset) for dataset in datasets]
    all_domains = [f.domain for f, num in zip(feedback, num_prompts) for _ in range(num)]
    all_effect = [f.effect for f, num in zip(feedback, num_prompts) for _ in range(num)]
    all_feedback = [f.content for f, num in zip(feedback, num_prompts) for _ in range(num)]
    all_prompts = [prompt for dataset in datasets for prompt in dataset["prompt"]]

    # Get completions for flattened list of prompts
    # Dict to hold all responses
    all_responses = {}
    all_responses['baseline_response'] = completion_model.get_responses([
        [GET_BASELINE_COMPLETION.format(domain=d, prompt=p)] for d, p in zip(all_domains, all_prompts)
    ], GET_BASELINE_COMPLETION_CONFIG)

    # Get revised completions for flattened list of prompts
    all_responses['revised_response'] = completion_model.get_responses([
        [GET_COMPLETION_REVISED.format(prompt=p, feedback=c, response=r)] for p, c, r in zip(all_prompts, all_effect, all_responses['baseline_response'])
    ], GET_COMPLETION_REVISED_CONFIG)
    all_responses['revised_response'] = [r.split("IMPROVED_RESPONSE:")[-1].strip() if r is not None else r for r in all_responses['revised_response']]

    # Get responses where feedback is applied in-context
    all_responses['in_context_response'] = completion_model.get_responses([
        [GET_IN_CONTEXT_COMPLETION.format(prompt=p, feedback=c)] for p, c in zip(all_prompts, all_feedback)
    ], GET_IN_CONTEXT_COMPLETION_CONFIG)

    # Get responses where feedback is applied in-context
    all_responses['cot_response'] = completion_model.get_responses([
        [GET_COT_COMPLETION.format(prompt=p, feedback=c)] for p, c in zip(all_prompts, all_feedback)
    ], GET_COT_COMPLETION_CONFIG)
    all_responses['cot_response'] = [r.split("RESPONSE:")[-1].strip() for r in all_responses['cot_response']]
        
    # Split responses into lists of prompts for each feedback
    for key in all_responses:
        all_responses[key] = np.array_split(all_responses[key], np.cumsum(num_prompts)[:-1])

    for i, f in enumerate(feedback):
        dataset = datasets[i]
        num_prompt = num_prompts[i]
        for key in all_responses:
            completions = all_responses[key][i]
            assert len(completions) == num_prompt, f"Completion generation failed for {key} (got {len(completions)}, expected: {num_prompt})"
            dataset = dataset.add_column(key, completions)

        # Filter out instances where any of the responses is None
        len_pre_filter = len(dataset)
        dataset = dataset.filter(lambda x: x['baseline_response'] is not None and x['revised_response'] is not None and x['in_context_response'] is not None)
        if len(dataset) < len_pre_filter:
            logger.warning(f"Filtered out {len_pre_filter - len(dataset)} instances where the completion API failed")

        if prompt_type == "prompts":
            f.prompts = dataset
        elif prompt_type == "negative_prompts":
            f.negative_prompts = dataset
        elif prompt_type == "general_prompts":
            f.general_prompts = dataset


def sample(arg_dict: dict[str, Any], run_id: str, data_dir: str, feedback: list[Feedback]) -> None:
    model_args, sample_args, _, _ = get_args(arg_dict)
    run_dir = os.path.join(data_dir, run_id, "sample")
    logger.info(f"Sampling data for run {run_id}, stored in {run_dir}")

    # Filter and load feedback
    feedback = [f for f in feedback if f.scope in sample_args.scope and f.type in sample_args.type]
    # Skip feedback that was already sampled if we don't want to overwrite
    if not sample_args.overwrite:
        feedback = [f for f in feedback if not f.can_load_dataset(run_dir)]
    feedback = feedback[:sample_args.num_feedbacks]
    logger.info(f"Loaded {len(feedback)} feedbacks")

    # Sample categories where necessary
    num_categories = np.ceil((max(sample_args.num_prompts, sample_args.num_general_prompts)) / sample_args.prompts_per_category)

    sample_categories(feedback, model_args.category_model, num_categories)
    logger.info(f"Sampled categories.")

    sample_prompts(feedback, model_args.prompt_model, sample_args.num_prompts, sample_args.prompts_per_category)
    logger.info(f"Sampled prompts.")

    # Sample prompts outside the feedback domain for non-global feedback
    sample_prompts(feedback, model_args.prompt_model, sample_args.num_negative_prompts, sample_args.prompts_per_category, negative=True)
    logger.info(f"Sampled negative prompts.")

    # Add prompts from general prompt dataset
    if feedback[0].general_prompts_available(run_dir) is None:
        add_general_prompts(feedback, data_dir, sample_args.num_general_prompts)
        sample_completions(feedback, model_args.completion_model, prompt_type="general_prompts")
        logger.info(f"Sampled general prompt completions.")
    else:
        _ = [f.load_cached_general_prompts(run_dir) for f in feedback]
        logger.info(f"Using cached general prompts.")

    # Sample completions
    sample_completions(feedback, model_args.completion_model, prompt_type="prompts")
    sample_completions(feedback, model_args.completion_model, prompt_type="negative_prompts")
    logger.info(f"Sampled completions for {len(feedback)} feedbacks")




    # Save datasets
    for f in feedback:
        f.prompts = f.prompts.train_test_split(
            sample_args.train_test_split
        )
        f.negative_prompts = f.negative_prompts.train_test_split(
            sample_args.train_test_split
        )
        if not isinstance(f.general_prompts, DatasetDict):
            f.general_prompts = f.general_prompts.train_test_split(
                sample_args.train_test_split
            )
        f.dump_dataset(run_dir)

    # TODO: add dummping args dict
    logger.info(f"Saved datasets for {len(feedback)} feedbacks")



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
    sample(arg_dict, args.run_id, args.data_dir, feedback)
