import os
import json
import argparse

import numpy as np

from src.logger import logger
from src.utils import get_args
from src.models import get_model
from src.dataset.feedback import Feedback, all_feedback, Scope



def eval(arg_file: str, run_id: str, data_dir: str, feedback: Feedback) -> None:
    model_args, _, _, eval_args = get_args(arg_file)
    
    # Load feedback
    run_dir = os.path.join(data_dir, run_id, "sample")
    logger.info(f"Evaluating using data for run {run_id}, stored in {run_dir}")
    if not feedback.can_load_dataset(run_dir):
        raise ValueError(f"Feedback \"{feedback.content}\" has not been sampled yet")
    feedback.load_dataset(run_dir)
    logger.info(f"Loaded feedback \"{feedback.content}\"")

    # Load model
    assert model_args.train_model.platform == "huggingface", "Only HuggingFace models are supported for training"
    model = get_model(model_args.train_model)
    logger.info("Loaded model")

    # Adding adapter
    run_dir = os.path.join(data_dir, run_id, "train")
    assert eval_args.algo in ["dpo", "sft"], f"Unknown algorithm {eval_args.algo}"
    run_dir = os.path.join(run_dir, eval_args.algo)
    run_dir = run_dir + ("-negatives" if eval_args.include_negatives else "-no_negatives")

    model.model.load_adapter(run_dir)


    # Construct dataset
    prompts = feedback.prompts["test"]["prompt"]
    baseline_responses = feedback.prompts["test"]["baseline_response"]
    revised_responses = feedback.prompts["test"]["revised_response"]

    negative_prompts = feedback.negative_prompts["test"]["prompt"] if feedback.scope == Scope.global_ else []
    negative_baseline_responses = feedback.negative_prompts["test"]["baseline_response"] if feedback.scope == Scope.global_ else []
    negative_revised_responses = feedback.negative_prompts["test"]["revised_response"] if feedback.scope == Scope.global_ else []

    all_trained_responses = model.get_responses([[p] for p in prompts + negative_prompts])
    trained_responses = all_trained_responses[:len(prompts)]
    trained_negative_responses = all_trained_responses[len(prompts):]

    data = {
        "in_domain": [],
        "out_domain": []
    }

    # TODO: currently assuming that if multiple metrics are specified, they must all evaluate to true. Should handle continuous values too.
    metric = lambda x: feedback.metric(x, feedback.metric_value) if not isinstance(
        feedback.metric, list) else lambda x: all([f(x, v) for f, v in zip(feedback.metric, feedback.metric_value)])
    
    # Compute metrics for in domain prompts
    for prompt, baseline_response, revised_response, trained_response in zip(prompts, baseline_responses, revised_responses, trained_responses):
        data["in_domain"].append({
            "prompt": prompt,
            "baseline_response": baseline_response,
            "revised_response": revised_response,
            "trained_response": trained_response,
            "baseline_metric": metric(baseline_response),
            "revised_metric": metric(revised_response),
            "trained_metric": metric(trained_response),
            "revised_better_baseline": feedback.comparison(baseline_response, revised_response),
            "trained_better_baseline": feedback.comparison(baseline_response, trained_response),
            "trained_better_revised": feedback.comparison(revised_response, trained_response),
        })

    # Compute metrics for out of domain prompts
    for prompt, baseline_response, revised_response, trained_response in zip(
        negative_prompts,
        negative_baseline_responses,
        negative_revised_responses,
        trained_negative_responses
    ):
        data["out_domain"].append({
            "prompt": prompt,
            "baseline_response": baseline_response,
            "revised_response": revised_response,
            "trained_response": trained_response,
            "baseline_metric": metric(baseline_response),
            "revised_metric": metric(revised_response),
            "trained_metric": metric(trained_response),
            "revised_better_baseline": feedback.comparison(baseline_response, revised_response),
            "trained_better_baseline": feedback.comparison(baseline_response, trained_response),
            "trained_better_revised": feedback.comparison(revised_response, trained_response),
        })

    
    # Compute aggregate stats for in-domain, out-of-domain, and all prompts
    for domain in ["in_domain", "out_domain"]:
        data[domain + "_baseline_metric"] = np.mean([d["baseline_metric"] for d in data[domain]])
        data[domain + "_revised_metric"] = np.mean([d["revised_metric"] for d in data[domain]])
        data[domain + "_trained_metric"] = np.mean([d["trained_metric"] for d in data[domain]])
        data[domain + "_revised_better_baseline"] = np.mean([d["revised_better_baseline"] for d in data[domain]])
        data[domain + "_trained_better_baseline"] = np.mean([d["trained_better_baseline"] for d in data[domain]])
        data[domain + "_trained_better_revised"] = np.mean([d["trained_better_revised"] for d in data[domain]])

    # Adding feedback info
    data["feedback"] = feedback.content
    data["scope"] = feedback.scope.value
    data["type"] = feedback.type.value

    logger.info(f"Evaluated model for feedback \"{feedback.content}\".\n(in-domain) Train vs baseline: {data['in_domain_trained_better_baseline']:.2f}\n(out-of-domain) Train vs baseline: {data['out_domain_trained_better_baseline']:.2f}")

    # Save data
    run_dir = os.path.join(data_dir, run_id, "eval", feedback.file_name)
    assert eval_args.algo in ["dpo", "sft"], f"Unknown algorithm {eval_args.algo}"
    run_dir = os.path.join(run_dir, eval_args.algo)
    os.makedirs(run_dir, exist_ok=True)
    run_dir = run_dir + ("-negatives" if eval_args.include_negatives else "-no_negatives") + ".json"
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

    feedback = all_feedback
    if args.feedback_prefix is not None:
        feedback = [f for f in feedback if f.content.startswith(args.feedback_prefix)]
    eval(args.arg_file, args.run_id, args.data_dir, feedback)