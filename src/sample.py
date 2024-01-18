import os
import argparse

import numpy as np
from datasets import Dataset, concatenate_datasets
np.random.seed(42)

from src.logger import logger
from src.models import get_model
from src.utils import get_args, split_numbered_list, ModelArguments, SampleArguments, dump_arg_dicts
from src.dataset.feedback import all_feedback, Feedback, Scope
from src.dataset.general_prompts import GeneralPromptDataset
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
    GET_COMPLETION_REVISED_CONFIG
)


def sample_categories(feedback: list[Feedback], model_args: ModelArguments, num_categories: int):
    """Sample categories for feedback and update feedback in-place"""
    category_model = get_model(model_args)
    responses = category_model.get_responses([
        [SAMPLE_PROMPT_CATEGORIES.format(count=num_categories, topic=f.domain)]
    for f in feedback], SAMPLE_PROMPT_CATEGORIES_CONFIG)
    responses = [split_numbered_list(r) for r in responses]
    assert all([len(r) == num_categories for r in responses]), "Category generation failed"
    for f, r in zip(feedback, responses):
        f.categories = r


def sample_prompts(feedback: list[Feedback], model_args: ModelArguments, sample_args: SampleArguments, negative: bool = False):
    """Sample prompts for feedback and update feedback in-place"""
    prompt = SAMPLE_PROMPTS if not negative else SAMPLE_NEGATIVE_PROMPTS
    prompt_config = SAMPLE_PROMPTS_CONFIG if not negative else SAMPLE_NEGATIVE_PROMPTS_CONFIG

    prompt_model = get_model(model_args)

    # Get responses for flattened list of prompts
    responses = prompt_model.get_responses([
        [prompt.format(count=sample_args.prompts_per_category, domain=f.domain, category=c)]
        for f in feedback for c in f.categories
    ], prompt_config)

    # Num responses (= num feedbacks x num categories) x num prompts per category
    responses = [prompt for r in responses for prompt in split_numbered_list(r)]

    # Split responses into lists of prompts for each feedback
    responses = np.array_split(responses, len(feedback))
    responses = [np.random.permutation(r)[:sample_args.num_train_prompts_per_feedback + sample_args.num_eval_prompts_per_feedback] for r in responses]
    responses = [r.tolist() for r in responses]
    assert all([len(r) == sample_args.num_train_prompts_per_feedback + sample_args.num_eval_prompts_per_feedback for r in responses]), "Prompt generation failed"

    for f, r in zip(feedback, responses):
        dataset = Dataset.from_dict({
            "prompt": r,
            "baseline_response": [None] * len(r),
            "revised_response": [None] * len(r),
            "in_context_response": [None] * len(r)
        })
        dataset = dataset.train_test_split(test_size=sample_args.num_eval_prompts_per_feedback, shuffle=False)
        if not negative:
            f.prompts = dataset
        else:
            f.negative_prompts = dataset


def add_general_prompts(feedback: list[Feedback], data_dir: str, sample_args: SampleArguments):
    """Add general prompts to feedback and update feedback in-place"""
    general_prompts = GeneralPromptDataset.load(data_dir, sample_args.num_train_prompts_general, sample_args.num_eval_prompts_general)
    for f in feedback:
        assert f.scope != Scope.global_, "Cannot add general prompts to global feedback"
        f.negative_prompts["train"] = concatenate_datasets([f.negative_prompts["train"], general_prompts["train"]])
        f.negative_prompts["test"] = concatenate_datasets([f.negative_prompts["test"], general_prompts["test"]])


def sample_completions(feedback: list[Feedback], model_args: ModelArguments, negative: bool = False):
    """Sample completions for feedback and update feedback in-place"""

    completion_model = get_model(model_args)

    num_train_prompts = [len(f.prompts["train"]) for f in feedback] if not negative else [len(f.negative_prompts["train"]) for f in feedback]
    num_test_prompts = [len(f.prompts["test"]) for f in feedback] if not negative else [len(f.negative_prompts["test"]) for f in feedback]
    num_prompts = [num_train + num_test for num_train, num_test in zip(num_train_prompts, num_test_prompts)]

    all_domains = [f.domain for f, num in zip(feedback, num_prompts) for _ in range(num)]
    all_effect = [f.effect for f, num in zip(feedback, num_prompts) for _ in range(num)]
    all_feedback = [f.content for f, num in zip(feedback, num_prompts) for _ in range(num)]
    all_prompts = [
        prompt for f in feedback for prompt in f.prompts["train"]["prompt"] + f.prompts["test"]["prompt"] 
    ] if not negative else [
        prompt for f in feedback for prompt in f.negative_prompts["train"]["prompt"] + f.negative_prompts["test"]["prompt"]
    ]

    # Get completions for flattened list of prompts
    responses = completion_model.get_responses([
        [GET_BASELINE_COMPLETION.format(domain=d, prompt=p)] for d, p in zip(all_domains, all_prompts)
    ], GET_BASELINE_COMPLETION_CONFIG)

    # Get revised completions for flattened list of prompts
    revised_responses = completion_model.get_responses([
        [GET_COMPLETION_REVISED.format(prompt=p, feedback=c, response=r)] for p, c, r in zip(all_prompts, all_effect, responses)
    ], GET_COMPLETION_REVISED_CONFIG)
    revised_responses = [r.split("IMPROVED_RESPONSE:")[-1].strip() for r in revised_responses]

    # Get responses where feedback is applied in-context
    in_context_responses = completion_model.get_responses([
        [GET_IN_CONTEXT_COMPLETION.format(prompt=p, feedback=c)] for p, c in zip(all_prompts, all_feedback)
    ], GET_IN_CONTEXT_COMPLETION_CONFIG)

    # Split responses into lists of prompts for each feedback
    responses = np.array_split(responses, len(feedback))
    revised_responses = np.array_split(revised_responses, len(feedback))
    in_context_responses = np.array_split(in_context_responses, len(feedback))

    for completions, revised_completions, in_context_responses, f, num_train, num_test in zip(
        responses,
        revised_responses,
        in_context_responses,
        feedback,
        num_train_prompts,
        num_test_prompts
    ):
        dataset = f.prompts if not negative else f.negative_prompts
        train_completions, test_completions = completions[:num_train], completions[num_train:]
        assert len(train_completions) == num_train
        assert len(test_completions) == num_test

        train_revised_completions, test_revised_completions = revised_completions[:num_train], revised_completions[num_train:]
        assert len(train_revised_completions) == num_train
        assert len(test_revised_completions) == num_test

        train_in_context_responses, test_in_context_responses = in_context_responses[:num_train], in_context_responses[num_train:]
        assert len(train_in_context_responses) == num_train
        assert len(test_in_context_responses) == num_test

        dataset["train"] = dataset["train"].remove_columns(["baseline_response", "revised_response", "in_context_response"])
        dataset["train"] = dataset["train"].add_column("baseline_response", train_completions)
        dataset["train"] = dataset["train"].add_column("revised_response", train_revised_completions)
        dataset["train"] = dataset["train"].add_column("in_context_response", train_in_context_responses)

        dataset["test"] = dataset["test"].remove_columns(["baseline_response", "revised_response", "in_context_response"])
        dataset["test"] = dataset["test"].add_column("baseline_response", test_completions)
        dataset["test"] = dataset["test"].add_column("revised_response", test_revised_completions)
        dataset["test"] = dataset["test"].add_column("in_context_response", test_in_context_responses)

        if not negative:
            f.prompts = dataset
        else:
            f.negative_prompts = dataset


def sample(arg_file: str, run_id: str, data_dir: str, feedback: list[Feedback]) -> None:
    model_args, sample_args, _, _ = get_args(arg_file)
    run_dir = os.path.join(data_dir, run_id, "sample")
    logger.info(f"Sampling data for run {run_id}, stored in {run_dir}")
    
    # Filter and load feedback
    feedback = [f for f in feedback if f.scope in sample_args.scope and f.type in sample_args.type]
    feedback: list[Feedback] = np.random.permutation(feedback)
    feedback = feedback[:sample_args.num_feedbacks]
    for f in feedback:
        if f.can_load_dataset(run_dir): f.load_dataset(run_dir)
    logger.info(f"Loaded {len(feedback)} feedbacks")

    # Sample categories where necessary
    num_categories = np.ceil((sample_args.num_train_prompts_per_feedback + sample_args.num_eval_prompts_per_feedback) / sample_args.prompts_per_category)
    feedback_without_categories = [f for f in feedback if f.categories is None or len(f.categories) < num_categories]
    for f in feedback_without_categories:
        f.categories = None
        f.prompts = None
        f.negative_prompts = None

    if len(feedback_without_categories) > 0:
        sample_categories(feedback_without_categories, model_args.category_model, num_categories)
        logger.info(f"Sampled categories for {len(feedback_without_categories)} feedbacks")
    else:
        logger.info(f"No categories to sample")

    # Sample prompts where necessary
    feedback_without_prompts = [
        f for f in feedback if f.prompts is None or
        f.negative_prompts is None or
        len(f.prompts["train"]) < sample_args.num_train_prompts_per_feedback or
        len(f.prompts["test"]) < sample_args.num_eval_prompts_per_feedback or
        len(f.negative_prompts["train"]) < sample_args.num_train_prompts_per_feedback + (sample_args.num_train_prompts_general if f.scope != Scope.global_ else 0) or
        len(f.negative_prompts["test"]) < sample_args.num_eval_prompts_per_feedback + (sample_args.num_eval_prompts_general if f.scope != Scope.global_ else 0)
    ]
    for f in feedback_without_prompts:
        f.prompts = None
        f.negative_prompts = None

    if len(feedback_without_prompts) > 0:
        sample_prompts(feedback_without_prompts, model_args.prompt_model, sample_args)
        logger.info(f"Sampled prompts for {len(feedback_without_prompts)} feedbacks")

    # Global feed always applies so we cannot generate out of domain prompts
    non_global_feedback = [f for f in feedback_without_prompts if f.scope != Scope.global_]
    if len(non_global_feedback) > 0:

        # Sample prompts outside the feedback domain
        sample_prompts(non_global_feedback, model_args.prompt_model, sample_args, negative=True)

        # Add prompts from general prompt dataset
        add_general_prompts(non_global_feedback, data_dir, sample_args)
        logger.info(f"Sampled negative prompts for {len(feedback_without_prompts)} feedbacks")
    else:
        logger.info(f"No prompts to sample")


    # Sample completions where necessary
    feedback_without_completions = [f for f in feedback if (
        f.prompts["train"]["baseline_response"].count(None) > 0 or
        f.prompts["train"]["revised_response"].count(None) > 0 or
        f.prompts["test"]["baseline_response"].count(None) > 0 or
        f.prompts["test"]["revised_response"].count(None) > 0
    )]

    if len(feedback_without_completions) > 0:
        sample_completions(feedback_without_completions, model_args.completion_model)
        sample_completions(feedback_without_completions, model_args.completion_model, negative=True)
        logger.info(f"Sampled completions for {len(feedback_without_completions)} feedbacks")
    else:
        logger.info(f"No completions to sample")

    # Save datasets
    for f in feedback:
        f.dump_dataset(run_dir)

    # TODO: add dummping args dict
    logger.info(f"Saved datasets for feedbacks")



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
    sample(args.arg_file, args.run_id, args.data_dir, feedback)