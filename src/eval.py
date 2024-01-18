import os
import json
import argparse
from typing import Any

import numpy as np

from src.logger import logger
from src.models import get_model
from src.utils import get_args, ModelArguments, get_train_file_name
from src.dataset.feedback import Feedback, all_feedback, Scope, Type
from src.dataset.prompts import COMPARE_COMPLETIONS, COMPARE_COMPLETIONS_CONFIG


def quantitative_eval(
    feedback: Feedback,
    prompts: list[str],
    baseline_responses: list[str],
    revised_responses: list[str],
    trained_responses: list[str],
    in_context_responses: list[str],
    _: ModelArguments
) -> list[dict]:
    
    if isinstance(feedback.metric, list):
        metric = lambda x: all([f(x, v) for f, v in zip(feedback.metric, feedback.metric_value)])
    else:
        metric = lambda x: feedback.metric(x, feedback.metric_value)
    
    data = []
    for prompt, baseline_response, revised_response, trained_response, in_context_response in zip(
        prompts,
        baseline_responses,
        revised_responses,
        trained_responses,
        in_context_responses
    ):
        new_data = {
            "prompt": prompt,
            "baseline_response": baseline_response,
            "revised_response": revised_response,
            "trained_response": trained_response,
            "in_context_response": in_context_response,
            "baseline_metric": metric(baseline_response),
            "revised_metric": metric(revised_response),
            "trained_metric": metric(trained_response),
            "in_context_metric": metric(in_context_response)
        }
        new_data["revised_better_baseline"] = feedback.comparison(
            new_data["baseline_metric"],
            new_data["revised_metric"]
        )
        new_data["trained_better_baseline"] = feedback.comparison(
            new_data["baseline_metric"],
            new_data["trained_metric"]
        )
        new_data["trained_better_revised"] = feedback.comparison(
            new_data["revised_metric"],
            new_data["trained_metric"]
        )
        new_data["in_context_better_baseline"] = feedback.comparison(
            new_data["baseline_metric"],
            new_data["in_context_metric"]
        )
        data.append(new_data)
    return data


def qualitative_eval(
    feedback: Feedback,
    prompts: list[str],
    baseline_responses: list[str],
    revised_responses: list[str],
    trained_responses: list[str], 
    in_context_responses: list[str],
    model_args: ModelArguments
) -> list[dict]:
    model = get_model(model_args)
    trained_better_baseline = model.get_responses([
        [COMPARE_COMPLETIONS.format(prompt=p, completion1=resp1, completion2=resp2, feedback=feedback.content)]
    for p, resp1, resp2 in zip(prompts, baseline_responses, trained_responses)], COMPARE_COMPLETIONS_CONFIG)
    trained_better_baseline = [False if r == "RESPONSE_1" else True for r in trained_better_baseline]

    revised_better_baseline = model.get_responses([
        [COMPARE_COMPLETIONS.format(prompt=p, completion1=resp1, completion2=resp2, feedback=feedback.content)]
    for p, resp1, resp2 in zip(prompts, baseline_responses, revised_responses)], COMPARE_COMPLETIONS_CONFIG)
    revised_better_baseline = [False if r == "RESPONSE_1" else True for r in revised_better_baseline]

    trained_better_revised = model.get_responses([
        [COMPARE_COMPLETIONS.format(prompt=p, completion1=resp1, completion2=resp2, feedback=feedback.content)]
    for p, resp1, resp2 in zip(prompts, revised_responses, trained_responses)], COMPARE_COMPLETIONS_CONFIG)
    trained_better_revised = [False if r.strip() == "RESPONSE_1" else True for r in trained_better_revised]

    in_context_better_baseline = model.get_responses([
        [COMPARE_COMPLETIONS.format(prompt=p, completion1=resp1, completion2=resp2, feedback=feedback.content)]
    for p, resp1, resp2 in zip(prompts, baseline_responses, in_context_responses)], COMPARE_COMPLETIONS_CONFIG)
    in_context_better_baseline = [False if r.strip() == "RESPONSE_1" else True for r in in_context_better_baseline]

    data = []
    for prompt, baseline_response, revised_response, trained_response, in_context_response, trained_better_baseline_, revised_better_baseline_, trained_better_revised_, in_context_better_baseline_ in zip(
        prompts,
        baseline_responses,
        revised_responses,
        trained_responses,
        in_context_responses,
        trained_better_baseline,
        revised_better_baseline,
        trained_better_revised,
        in_context_better_baseline
    ):
        data.append({
            "prompt": prompt,
            "baseline_response": baseline_response,
            "revised_response": revised_response,
            "trained_response": trained_response,
            "in_context_response": in_context_response,
            "baseline_metric": -1,
            "revised_metric": -1,
            "trained_metric": -1,
            "in_context_metric": -1,
            "revised_better_baseline": revised_better_baseline_,
            "trained_better_baseline": trained_better_baseline_,
            "trained_better_revised": trained_better_revised_,
            "in_context_better_baseline": in_context_better_baseline_
        })
    return data


def eval(arg_dict: dict[str, Any], run_id: str, data_dir: str, feedback: Feedback) -> None:
    model_args, _, train_args, eval_args = get_args(arg_file)
    
    # Load feedback
    run_dir = os.path.join(data_dir, run_id, "sample")
    logger.info(f"Evaluating using data for run {run_id}, stored in {run_dir}")
    if not feedback.can_load_dataset(run_dir):
        raise ValueError(f"Feedback \"{feedback.content}\" has not been sampled yet")
    feedback.load_dataset(run_dir)
    logger.info(f"Loaded feedback \"{feedback.content}\"")

    # Load model
    assert model_args.train_model.platform == "huggingface", "Only HuggingFace models are supported for eval"
    model = get_model(model_args.train_model)
    logger.info("Loaded model")

    # Adding adapter
    run_dir = os.path.join(data_dir, run_id, "train", feedback.file_name)
    assert eval_args.algo in ["dpo", "sft"], f"Unknown algorithm {train_args.algo}"
    train_dir = get_train_file_name(train_args)
    run_dir = os.path.join(run_dir, train_dir)

    model.model.load_adapter(run_dir)


    # Construct dataset
    prompt_dataset = feedback.prompts["test"].shuffle(seed=42).select(range(eval_args.num_prompts))
    prompts = prompt_dataset["prompt"]
    baseline_responses = prompt_dataset["baseline_response"]
    revised_responses = prompt_dataset["revised_response"]
    in_context_responses = prompt_dataset["in_context_response"]

    negative_prompt_dataset = feedback.negative_prompts["test"].shuffle(seed=42).select(range(eval_args.num_negative_prompts))
    negative_prompts = negative_prompt_dataset["prompt"] if feedback.scope != Scope.global_ else []
    negative_baseline_responses = negative_prompt_dataset["baseline_response"] if feedback.scope != Scope.global_ else []
    negative_revised_responses = negative_prompt_dataset["revised_response"] if feedback.scope != Scope.global_ else []
    negative_in_context_responses = negative_prompt_dataset["in_context_response"] if feedback.scope != Scope.global_ else []

    # Get trained responses
    all_trained_responses = model.get_responses([[p] for p in prompts + negative_prompts])
    trained_responses = all_trained_responses[:len(prompts)]
    trained_negative_responses = all_trained_responses[len(prompts):]

    # Get eval function
    eval_func = quantitative_eval if feedback.type == Type.quantitative else qualitative_eval

    # Compute metrics for in domain prompts
    in_domain = eval_func(
        feedback,
        prompts,
        baseline_responses,
        revised_responses,
        trained_responses,
        in_context_responses,
        model_args.qualitative_eval_model)

    # Compute metrics for out of domain prompts
    out_of_domain = eval_func(
        feedback,
        negative_prompts,
        negative_baseline_responses,
        negative_revised_responses,
        trained_negative_responses,
        negative_in_context_responses,
        model_args.qualitative_eval_model)


    data = {}
    
    # Compute aggregate stats for in-domain, out-of-domain, and all prompts
    for domain, domain_name in [(in_domain, "in_domain"), (out_of_domain, "out_of_domain")]:
        data[domain_name + "_baseline_metric"] = np.mean([d["baseline_metric"] for d in domain])
        data[domain_name + "_revised_metric"] = np.mean([d["revised_metric"] for d in domain])
        data[domain_name + "_trained_metric"] = np.mean([d["trained_metric"] for d in domain])
        data[domain_name + "_revised_better_baseline"] = np.mean([d["revised_better_baseline"] for d in domain])
        data[domain_name + "_trained_better_baseline"] = np.mean([d["trained_better_baseline"] for d in domain])
        data[domain_name + "_trained_better_revised"] = np.mean([d["trained_better_revised"] for d in domain])
        data[domain_name + "_in_context_better_baseline"] = np.mean([d["in_context_better_baseline"] for d in domain])

    # Adding feedback info
    data["feedback"] = feedback.content
    data["scope"] = feedback.scope.value
    data["type"] = feedback.type.value
    data["in_domain"] = in_domain
    data["out_of_domain"] = out_of_domain

    logger.info(f"Evaluated model for feedback \"{feedback.content}\".\n(in-domain) Train vs baseline: {data['in_domain_trained_better_baseline']:.2f}\n(out-of-domain) Train vs baseline: {data['out_of_domain_trained_better_baseline']:.2f}")

    # Save data
    run_dir = os.path.join(data_dir, run_id, "eval", feedback.file_name)
    os.makedirs(run_dir, exist_ok=True)
    run_dir += get_train_file_name(train_args) + ".json"
    with open(run_dir, "w+") as f:
        json.dump(data, f, indent=2)

    # TODO: add dummping args dict
    logger.info(f"Saved datasets for feedback to {run_dir}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("arg_file", type=str)
    parser.add_argument("run_id", type=str)
    parser.add_argument("--data_dir", type=str, default="./data")
    parser.add_argument("--feedback_prefix", type=str, default=None)
    args = parser.parse_args()

    with open(args.arg_file, "r") as f:
        arg_dict = json.load(f)

    feedback = all_feedback
    if args.feedback_prefix is not None:
        feedback = [f for f in feedback if f.content.startswith(args.feedback_prefix)]
    eval(arg_dict, args.run_id, args.data_dir, feedback)