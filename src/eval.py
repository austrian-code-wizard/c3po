import os
import json
import argparse
from typing import Any

import numpy as np

from src.logger import logger
from src.models import get_model
from src.feedback import manual_feedback as all_feedback
from src.dataset.feedback_utils import Feedback, Scope, Type
from src.utils import get_args, ModelArguments, get_train_file_name
from src.dataset.prompts import COMPARE_COMPLETIONS, COMPARE_COMPLETIONS_CONFIG, ANSWER_QUALITATIVE_EVAL, ANSWER_QUALITATIVE_EVAL_CONFIG


def quantitative_feedback_eval(
    feedback: Feedback,
    prompts: list[str],
    baseline_responses: list[str],
    revised_responses: list[str],
    trained_responses: list[str],
    in_context_responses: list[str],
    cot_responses: list[str],
    _: ModelArguments
) -> list[dict]:
    
    if isinstance(feedback.metric, list):
        metric = lambda x: all([f(x, v) for f, v in zip(feedback.metric, feedback.metric_value)])
    else:
        metric = lambda x: feedback.metric(x, feedback.metric_value)
    
    data = []
    for prompt, baseline_response, revised_response, trained_response, in_context_response, cot_response in zip(
        prompts,
        baseline_responses,
        revised_responses,
        trained_responses,
        in_context_responses,
        cot_responses
    ):
        new_data = {
            "prompt": prompt,
            "baseline_response": baseline_response,
            "revised_response": revised_response,
            "trained_response": trained_response,
            "in_context_response": in_context_response,
            "cot_response": cot_response
        }

        # Compute metrics
        for k, v in new_data.items():
            if k.endswith("_response"):
                new_data[k.split("_response")[0] + "_metric"] = metric(v)

        # Compute comparison
        for k in ["revised", "trained", "in_context", "cot"]:
            new_data[k + "_better_baseline"] = feedback.comparison(
                new_data["baseline_metric"],
                new_data[k + "_metric"]
            )
        data.append(new_data)
    return data


def call_compare_completions(
    model: Any,
    prompts: list[str],
    baseline_responses: list[str],
    revised_responses: list[str],
    feedback: str
) -> list[bool]:
    responses = model.get_responses([
        [COMPARE_COMPLETIONS.format(prompt=p, completion1=resp1, completion2=resp2, feedback=feedback)]
    for p, resp1, resp2 in zip(prompts, baseline_responses, revised_responses)], COMPARE_COMPLETIONS_CONFIG)
    responses = [int(r.split("BETTER_RESPONSE: ")[-1].strip().split()[0]) if r is not None else None for r in responses]
    return responses


def qualitative_feedback_eval(
    feedback: Feedback,
    prompts: list[str],
    baseline_responses: list[str],
    revised_responses: list[str],
    trained_responses: list[str], 
    in_context_responses: list[str],
    cot_responses: list[str],
    model_args: ModelArguments
) -> list[dict]:
    model = get_model(model_args)
    trained_better_baseline = call_compare_completions(model, prompts, baseline_responses, trained_responses, feedback.content)
    revised_better_baseline = call_compare_completions(model, prompts, baseline_responses, revised_responses, feedback.content)
    in_context_better_baseline = call_compare_completions(model, prompts, baseline_responses, in_context_responses, feedback.content)
    cot_better_baseline = call_compare_completions(model, prompts, baseline_responses, cot_responses, feedback.content)

    data = []
    for prompt, baseline_response, revised_response, trained_response, in_context_response, trained_better_baseline_, revised_better_baseline_, in_context_better_baseline_, cot_better_baseline_ in zip(
        prompts,
        baseline_responses,
        revised_responses,
        trained_responses,
        in_context_responses,
        trained_better_baseline,
        revised_better_baseline,
        in_context_better_baseline,
        cot_better_baseline
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
            "in_context_better_baseline": in_context_better_baseline_,
            'cot_better_baseline': cot_better_baseline_,
        })
    return data


def call_answer_qualitative_eval(
    model: Any,
    prompts: list[str],
    baseline_responses: list[str],
    revised_responses: list[str]
) -> list[bool]:
    responses = model.get_responses([
        [ANSWER_QUALITATIVE_EVAL.format(prompt=p, completion1=resp1, completion2=resp2)]
    for p, resp1, resp2 in zip(prompts, baseline_responses, revised_responses)], ANSWER_QUALITATIVE_EVAL_CONFIG)
    responses = [int(r.split("BETTER_RESPONSE: ")[-1].strip().split()[0]) if r is not None else None for r in responses]
    return responses


def answer_eval(
    feedback: Feedback,
    prompts: list[str],
    baseline_responses: list[str],
    trained_responses: list[str],
    in_context_responses: list[str],
    cot_responses: list[str],
    model_args: ModelArguments
) -> list[dict]:
    model = get_model(model_args)
    trained_better_baseline = call_answer_qualitative_eval(model, prompts, baseline_responses, trained_responses)
    in_context_better_baseline = call_answer_qualitative_eval(model, prompts, baseline_responses, in_context_responses)
    cot_better_baseline = call_answer_qualitative_eval(model, prompts, baseline_responses, cot_responses)

    data = []
    for trained_better_baseline_, in_context_better_baseline_, cot_better_baseline_ in zip(
        trained_better_baseline,
        in_context_better_baseline,
        cot_better_baseline
    ):
        data.append({
            "answer_quality_trained_better_baseline": trained_better_baseline_,
            "answer_quality_in_context_better_baseline": in_context_better_baseline_,
            'answer_quality_cot_better_baseline': cot_better_baseline_,
        })
    return data


def eval(arg_dict: dict[str, Any], run_id: str, data_dir: str, feedback: Feedback) -> None:
    model_args, _, train_args, eval_args = get_args(arg_dict)
    
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
    assert eval_args.algo in ["dpo", "sft", "lcdpo"], f"Unknown algorithm {eval_args.algo}"
    train_dir = get_train_file_name(train_args)
    run_dir = os.path.join(run_dir, train_dir)

    model.model.load_adapter(run_dir)

    # Construct datasets
    prompt_types = {
        "prompts": eval_args.num_prompts,
        "negative_prompts": eval_args.num_negative_prompts,
        "general_prompts": eval_args.num_general_prompts
    }

    datasets = {}
    for prompt_type, num_prompt_arg in prompt_types.items():
        num_prompts = min(num_prompt_arg, len(feedback[prompt_type]["test"]))
        prompt_dataset = feedback[prompt_type]["test"].shuffle(seed=42).select(range(num_prompts))
        datasets[prompt_type] = {
            "prompts": prompt_dataset["prompt"],
            "baseline_responses": prompt_dataset["baseline_response"],
            "revised_responses": prompt_dataset["revised_response"],
            "in_context_responses": prompt_dataset["in_context_response"],
            "cot_responses": prompt_dataset["cot_response"]
        }

    # Get trained responses
    all_prompts = [p for pt in datasets.values() for p in pt["prompts"]]
    all_trained_responses = model.get_responses([[p] for p in all_prompts])
    trained_responses_splits = np.split(all_trained_responses, np.cumsum([len(datasets[pt]["prompts"]) for pt in prompt_types]))
    for i, prompt_type in enumerate(prompt_types):
        datasets[prompt_type]["trained_responses"] = trained_responses_splits[i]

    # Get eval function
    eval_func = quantitative_feedback_eval if feedback.type == Type.quantitative else qualitative_feedback_eval

    # Compute metrics for each prompt type
    results = {}
    for prompt_type in prompt_types:
        feedback_result = eval_func(
            feedback,
            datasets[prompt_type]["prompts"],
            datasets[prompt_type]["baseline_responses"],
            datasets[prompt_type]["revised_responses"],
            datasets[prompt_type]["trained_responses"],
            datasets[prompt_type]["in_context_responses"],
            datasets[prompt_type]["cot_responses"],
            model_args.qualitative_eval_model)

        answer_quality_result = answer_eval(
            feedback,
            datasets[prompt_type]["prompts"],
            datasets[prompt_type]["baseline_responses"],
            datasets[prompt_type]["trained_responses"],
            datasets[prompt_type]["in_context_responses"],
            datasets[prompt_type]["cot_responses"],
        )
        results[prompt_type] = [dict(**f, **a) for f, a in zip(feedback_result, answer_quality_result)]


    data = {}    
    # Compute aggregate stats for in-domain, out-of-domain, and general prompts
    for domain_name, domain in results.items():
        data[domain_name + "_baseline_metric"] = np.mean([d["baseline_metric"] for d in domain])
        data[domain_name + "_revised_metric"] = np.mean([d["revised_metric"] for d in domain])
        data[domain_name + "_trained_metric"] = np.mean([d["trained_metric"] for d in domain])
        data[domain_name + "_in_context_metric"] = np.mean([d["in_context_metric"] for d in domain])
        data[domain_name + "_cot_metric"] = np.mean([d["cot_metric"] for d in domain])
        data[domain_name + "_revised_better_baseline"] = np.mean([d["revised_better_baseline"] for d in domain])
        data[domain_name + "_trained_better_baseline"] = np.mean([d["trained_better_baseline"] for d in domain])
        data[domain_name + "_in_context_better_baseline"] = np.mean([d["in_context_better_baseline"] for d in domain])
        data[domain_name + "_cot_better_baseline"] = np.mean([d["cot_better_baseline"] for d in domain])
        data[domain_name + "_answer_quality_trained_better_baseline"] = np.mean([d["answer_quality_trained_better_baseline"] for d in domain])
        data[domain_name + "_answer_quality_in_context_better_baseline"] = np.mean([d["answer_quality_in_context_better_baseline"] for d in domain])
        data[domain_name + "_answer_quality_cot_better_baseline"] = np.mean([d["answer_quality_cot_better_baseline"] for d in domain])

    # Adding feedback info
    data["feedback"] = feedback.content
    data["scope"] = feedback.scope.value
    data["type"] = feedback.type.value
    for domain_name, domain in results.items():
        data[domain_name] = domain

    logger.info(f"""Evaluated model for feedback "{feedback.content}".
(in-domain) Train vs baseline: {data['in_domain_trained_better_baseline']:.2f}
(out-of-domain) Train vs baseline: {data['out_of_domain_trained_better_baseline']:.2f}
(general) Train vs baseline: {data['general_trained_better_baseline']:.2f}""")

    # Save data
    run_dir = os.path.join(data_dir, run_id, "eval", feedback.file_name)
    os.makedirs(run_dir, exist_ok=True)
    train_dir = get_train_file_name(train_args) + ".json"
    run_dir = os.path.join(run_dir, train_dir)
    with open(run_dir, "w+") as f:
        json.dump(data, f, indent=2)

    # TODO: add dummping args dict
    logger.info(f"Saved datasets for feedback to {run_dir}")


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
    eval(arg_dict, args.run_id, args.data_dir, feedback)
