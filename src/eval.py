import os
import json
import argparse
from typing import Any

import numpy as np
from peft import PeftModel

from src.logger import logger
from src.models import get_model
from src.feedback import manual_feedback as all_feedback
from src.dataset.feedback_utils import Feedback, Type
from src.utils import get_args, ModelArguments, get_train_file_name
from src.dataset.prompts import COMPARE_COMPLETIONS, COMPARE_COMPLETIONS_CONFIG, ANSWER_QUALITATIVE_EVAL, ANSWER_QUALITATIVE_EVAL_CONFIG


def quantitative_feedback_eval(
    feedback: Feedback,
    prompts: list[str],
    baseline_responses: list[str],
    improved_responses: list[str],
    _: ModelArguments
) -> list[dict]:
    
    if isinstance(feedback.metric, list):
        metric = lambda x: all([f(x, v) for f, v in zip(feedback.metric, feedback.metric_value)])
    else:
        metric = lambda x: feedback.metric(x, feedback.metric_value)
    
    data = []
    for prompt, baseline_response, improved_response in zip(
        prompts,
        baseline_responses,
        improved_responses
    ):
        new_data = {
            "prompt": prompt,
            "baseline": baseline_response,
            "improved": improved_response,
            "baseline_metric": metric(baseline_response),
            "improved_metric": metric(improved_response),
            "improved_better_baseline": feedback.comparison(
                metric(baseline_response),
                metric(improved_response),
            )
        }
        data.append(new_data)
    return data


def qualitative_feedback_eval(
    feedback: Feedback,
    prompts: list[str],
    baseline_responses: list[str],
    improved_responses: list[str],
    model_args: ModelArguments
) -> list[dict]:
    model = get_model(model_args)
    responses = model.get_responses([
        [COMPARE_COMPLETIONS.format(prompt=p, completion1=resp1, completion2=resp2, feedback=feedback.effect)]
    for p, resp1, resp2 in zip(prompts, baseline_responses, improved_responses)], COMPARE_COMPLETIONS_CONFIG)
    responses = [r.split("BETTER_RESPONSE: ")[-1].strip().split()[0] if r is not None else None for r in responses]
    responses = [int(r) if r is not None and r.isnumeric() else None for r in responses]

    data = []
    for prompt, baseline_response, improved_response, improved_better_baseline in zip(
        prompts,
        baseline_responses,
        improved_responses,
        responses
    ):
        data.append({
            "prompt": prompt,
            "baseline": baseline_response,
            "improved": improved_response,
            "baseline_metric": -1,
            "improved_metric": -1,
            "improved_better_baseline": improved_better_baseline
        })
    return data


def answer_eval(
    feedback: Feedback,
    prompts: list[str],
    baseline_responses: list[str],
    improved_responses: list[str],
    model_args: ModelArguments
) -> list[dict]:
    model = get_model(model_args)
    responses = model.get_responses([
        [ANSWER_QUALITATIVE_EVAL.format(prompt=p, completion1=resp1, completion2=resp2, feedback=feedback.content)]
    for p, resp1, resp2 in zip(prompts, baseline_responses, improved_responses)], ANSWER_QUALITATIVE_EVAL_CONFIG)
    responses = [r.split("BETTER_RESPONSE: ")[-1].strip().split()[0] if r is not None else None for r in responses]
    responses = [int(r) if r is not None and r.isnumeric() else None for r in responses]
    return [{
        "answer_quality_improved_better_baseline": r
    } for r in responses]


def eval(arg_dict: dict[str, Any], run_id: str, data_dir: str, feedback: Feedback, second_feedback: Feedback = None) -> None:
    model_args, _, train_args, eval_args = get_args(arg_dict)
    
    # Load feedback
    run_dir = os.path.join(data_dir, run_id, "sample")
    logger.info(f"Evaluating using data for run {run_id}, stored in {run_dir} of method {eval_args.method}")
    assert eval_args.method in ["trained", "in_context", "cot", "revised"], f"Unknown eval method {eval_args.method}"
    if not feedback.can_load_dataset(run_dir):
        raise ValueError(f"Feedback \"{feedback.content}\" has not been sampled yet")
    feedback.load_dataset(run_dir)
    logger.info(f"Loaded feedback \"{feedback.content}\"")

    if second_feedback is not None:
        assert eval_args.method == "trained", "Second feedback is only supported for evaluating trained model"
        if not second_feedback.can_load_dataset(run_dir):
            raise ValueError(f"Feedback \"{second_feedback.content}\" has not been sampled yet")
        second_feedback.load_dataset(run_dir)
        logger.info(f"Loaded second feedback \"{second_feedback.content}\"")

    if second_feedback is None and train_args.multi_feedback_training:
        raise ValueError("Must specify second feedback when using multi-feedback training")

    # Construct datasets
    prompt_types = [
        ("in_domain", eval_args.num_prompts, feedback.prompts["test"]),
        ("out_of_domain", eval_args.num_negative_prompts, feedback.negative_prompts["test"]),
        ("general", eval_args.num_general_prompts, feedback.general_prompts["test"])
    ]


    datasets = {}
    for prompt_type, num_prompts, prompt_dataset in prompt_types:
        if num_prompts is None or len(prompt_dataset) < num_prompts:
            num_prompts = len(prompt_dataset)
        prompt_dataset = prompt_dataset.shuffle(seed=42).select(range(num_prompts))
        datasets[prompt_type] = {
            "prompts": prompt_dataset["prompt"],
            "baseline": prompt_dataset["baseline_response"],
        }
        # Set improved response to pre-generated completions for current method
        if eval_args.method != "trained":
            datasets[prompt_type]["improved"] = prompt_dataset[f"{eval_args.method}_response"]

    # Alternatively if using the "trained" method, sample from the model
    if eval_args.method == "trained":
        # Load model
        assert model_args.train_model.platform == "huggingface", "Only HuggingFace models are supported for eval"
        model = get_model(model_args.train_model)
        logger.info("Loaded model")

        # Adding adapter
        run_dir = os.path.join(data_dir, run_id, "train", feedback.file_name)
        train_dir = get_train_file_name(train_args, model_args.train_model)

        if second_feedback is not None and train_args.multi_feedback_training:
            run_dir = os.path.join(run_dir, second_feedback.file_name, train_dir)
        else:
            run_dir = os.path.join(run_dir, train_dir)       
        
        if second_feedback is not None and not train_args.multi_feedback_training:
            second_run_dir = os.path.join(data_dir, run_id, "train", second_feedback.file_name)
            second_run_dir = os.path.join(second_run_dir, train_dir)
            model.model = PeftModel.from_pretrained(model.model, run_dir, adapter_name="feedback_1")
            model.model.load_adapter(second_run_dir, adapter_name="feedback_2")
            model.model.add_weighted_adapter(["feedback_1", "feedback_2"], [1.0,1.0], combination_type="cat", adapter_name="feedback_combined")
            #model.model.delete_adapter(["feedback_1", "feedback_2"])
            model.model.set_adapter("feedback_combined")
            logger.info(f"Loaded combined adapter: {model.model.active_adapter}")
        else:
            model.model.load_adapter(run_dir, adapter_name="feedback_1")

        # Ensure correct generation
        model.tokenizer.padding_size = "left"

        # Get trained responses
        all_prompts = [p for pt in datasets.values() for p in pt["prompts"]]
        all_trained_responses = model.get_responses([[p] for p in all_prompts])
        trained_responses_splits = np.split(all_trained_responses, np.cumsum([len(datasets[pt]["prompts"]) for pt in datasets]))
        for i, prompt_type in enumerate(datasets):
            datasets[prompt_type]["improved"] = trained_responses_splits[i]


    # Make sure the "improved" field is set for all datasets
    for prompt_type in datasets:
        assert "improved" in datasets[prompt_type], f"Missing improved_response for {prompt_type}"

    # Get eval function
    eval_func = quantitative_feedback_eval if feedback.type == Type.quantitative else qualitative_feedback_eval

    # Compute metrics for each prompt type
    results = {}
    for prompt_type in datasets:
        feedback_result = eval_func(
            feedback,
            datasets[prompt_type]["prompts"],
            datasets[prompt_type]["baseline"],
            datasets[prompt_type]["improved"],
            model_args.qualitative_eval_model)

        answer_quality_result = answer_eval(
            feedback,
            datasets[prompt_type]["prompts"],
            datasets[prompt_type]["baseline"],
            datasets[prompt_type]["improved"],
            model_args.qualitative_eval_model
        ) if eval_args.eval_answer_quality else [{
            "answer_quality_improved_better_baseline": -1
        } for _ in feedback_result]
        results[prompt_type] = [dict(**f, **a) for f, a in zip(feedback_result, answer_quality_result)]


    data = {}    
    # Compute aggregate stats for in-domain, out-of-domain, and general prompts
    for domain_name, domain in results.items():
        data[domain_name + "_baseline_metric"] = np.mean([d["baseline_metric"] for d in domain])
        data[domain_name + "_improved_metric"] = np.mean([d["improved_metric"] for d in domain])
        data[domain_name + "_improved_better_baseline"] = np.mean(
            [d["improved_better_baseline"] for d in domain if d["improved_better_baseline"] is not None])
        data[domain_name + "_answer_quality_improved_better_baseline"] = np.mean(
            [d["answer_quality_improved_better_baseline"] for d in domain if d["answer_quality_improved_better_baseline"] is not None])

    # Adding feedback info
    data["feedback"] = feedback.content
    data["scope"] = feedback.scope.value
    data["type"] = feedback.type.value
    for domain_name, domain in results.items():
        data[domain_name] = domain
    if eval_args.method == "trained":
        data["train_args"] = train_args.to_dict()
    if second_feedback is not None:
        data["second_feedback"] = second_feedback.content

    logger.info(f"""Evaluated model for feedback "{feedback.content} using method {eval_args.method}".
(in-domain) Train vs baseline: {data['in_domain_improved_better_baseline']:.2f}
(out-of-domain) Train vs baseline: {data['out_of_domain_improved_better_baseline']:.2f}
(general) Train vs baseline: {data['general_improved_better_baseline']:.2f}""")


    # Save data
    run_dir = os.path.join(data_dir, run_id, "eval", feedback.file_name)
    if second_feedback is not None:
        run_dir = os.path.join(run_dir, second_feedback.file_name)
    os.makedirs(run_dir, exist_ok=True)
    if eval_args.method == "trained":
        train_dir = get_train_file_name(train_args, model_args.train_model) + ".json"
    else:
        train_dir = f"{eval_args.method}.json"
    run_dir = os.path.join(run_dir, train_dir)
    with open(run_dir, "w+") as f:
        json.dump(data, f, indent=2)

    # TODO: add dummping args dict
    logger.info(f"Saved datasets for feedback to {run_dir} and method {eval_args.method}")


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
