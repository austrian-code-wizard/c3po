import os
import json
import copy
from typing import Any
from modal import gpu, Mount

from src.train import train
from src.sample import sample
from src.eval import eval as evaluation
from src.dataset.feedback_utils import Feedback
from src.modal.common import stub, VOLUME_CONFIG
from src.modal.utils import copy_json_files_recursively
from src.feedback import manual_feedback as all_feedback


@stub.function(
    volumes=VOLUME_CONFIG,
    cpu=2.0,
    image=stub.non_gpu_image,
    timeout=3600 * 12,
    concurrency_limit=512,
    mounts=[
        Mount.from_local_dir("configs", remote_path="/root/configs")
    ]
)
def _sample(arg_dict: dict[str, Any], run_id: str, data_dir: str, feedback: list[Feedback]):
    sample(arg_dict, run_id, data_dir, feedback)

    # TODO: remove this once we have a better way open file pointers
    for f in feedback:
        del f.prompts
        del f.negative_prompts
        del f.general_prompts

    stub.pretrained_volume.commit()
    stub.results_volume.commit()


@stub.function(
    volumes=VOLUME_CONFIG,
    cpu=4.0,
    image=stub.gpu_image,
    gpu=gpu.A100(count=1, memory=40),
    timeout=3600 * 12,
    concurrency_limit=512,
    mounts=[
        Mount.from_local_dir("configs", remote_path="/root/configs")
    ]
)
def _train(arg_dict: dict[str, Any], run_id: str, data_dir: str, feedback: Feedback, second_feedback: Feedback = None):
    train(arg_dict, run_id, data_dir, feedback, second_feedback)

    # TODO: remove this once we have a better way open file pointers
    del feedback.prompts
    del feedback.negative_prompts
    del feedback.general_prompts
    if second_feedback is not None:
        del second_feedback.prompts
        del second_feedback.negative_prompts
        del second_feedback.general_prompts
    stub.pretrained_volume.commit()
    stub.results_volume.commit()


@stub.function(
    volumes=VOLUME_CONFIG,
    cpu=4.0,
    image=stub.gpu_image,
    gpu=gpu.A100(count=1),
    timeout=3600 * 12,
    concurrency_limit=512,
    mounts=[
        Mount.from_local_dir("configs", remote_path="/root/configs")
    ]
)
def _eval(arg_dict: dict[str, Any], run_id: str, data_dir: str, feedback: Feedback, second_feedback: Feedback = None):
    evaluation(arg_dict, run_id, data_dir, feedback, second_feedback)

    # TODO: remove this once we have a better way open file pointers
    del feedback.prompts
    del feedback.negative_prompts
    del feedback.general_prompts
    if second_feedback is not None:
        del second_feedback.prompts
        del second_feedback.negative_prompts
        del second_feedback.general_prompts
    stub.pretrained_volume.commit()
    stub.results_volume.commit()


@stub.local_entrypoint()  # Runs locally to kick off remote training job.
def main(
    arg_file: str,
    run_id: str = "test",
    data_dir: str = "/results/data",
    do_sample: bool = False,
    do_train: bool = False,
    do_eval: bool = False,
    feedback_prefix: str = None,
    second_feedback_prefix: str = None,
    feedback_category: str = None,
    copy_results: bool = True,
    sweep_params: str = None,  # Changed to sweep_params to indicate multiple parameters
    sweep_values: str = None
):
    print(f"Welcome to Modal Feedback fine-tuning.")

    print(f"Beginning run {run_id=}.")
    feedback = all_feedback

    if feedback_category is not None:
        feedback = [f for f in feedback if f.categories is not None and feedback_category in f.categories]

    # For multi adapter eval
    second_feedback = None
    if second_feedback_prefix is not None:
        second_feedback = [f for f in feedback if f.content.startswith(second_feedback_prefix)]
        assert len(second_feedback) == 1, "Must specify exactly one second feedback"
        second_feedback = second_feedback[0]

    if feedback_prefix is not None:
        feedback = [f for f in feedback if f.content.startswith(feedback_prefix)]

    print(f"Using {len(feedback)} feedbacks.")

    with open(arg_file, "r") as f:
        arg_dict = json.load(f)
    print(f"Using {arg_file}.")

    assert not (sweep_values is not None and sweep_params is None), "Must specify sweep_params if sweep_values is specified"
    assert not (sweep_params is not None and sweep_values is None), "Must specify sweep_values if sweep_params is specified"
    assert not (len(feedback) > 1 and sweep_params is not None), "Cannot sweep over feedback if more than one feedback is specified"
    assert not (sweep_params is not None and do_sample), "Cannot sample when sweeping"

    arg_dicts = [copy.deepcopy(arg_dict) for _ in range(len(feedback))]
    if sweep_params is not None:
        sweep_params_list = eval(sweep_params)  # TODO: make this safer?
        sweep_values_list = eval(sweep_values)  # TODO: make this safer?
        for values in sweep_values_list:
            assert len(values) == len(sweep_params_list), "Each tuple in sweep_values must have the same number of elements as sweep_params list"
        print(f"Sweeping over {sweep_params} with values {sweep_values}.")
        arg_dicts.clear()
        for sweep_value_tuple in sweep_values_list:
            arg_dict_copy = copy.deepcopy(arg_dict)
            for sweep_param, sweep_value in zip(sweep_params_list, sweep_value_tuple):
                sweep_param_keys = sweep_param.split(".")
                assert len(sweep_param_keys) == 2, "Each sweep_param must be of the form <arg_name>.<param_name> (e.g. train_args.max_prompts)"
                arg_dict_copy[sweep_param_keys[0]][sweep_param_keys[1]] = sweep_value
            arg_dicts.append(arg_dict_copy)
        # TODO: make this more general
        feedback = [feedback[0]] * len(arg_dicts)

    if do_sample:

        # TODO: Remove hacky way to ensure proper arg parsing on non-gpu images
        bf16 = arg_dict["training_args"]["bf16"]
        tf32 = arg_dict["training_args"]["tf32"]
        arg_dict["training_args"]["bf16"] = False
        arg_dict["training_args"]["tf32"] = False
        # - End Hack

        print("Sampling dataset.")
        _sample.remote(arg_dict, run_id, data_dir, feedback)

        # TODO: Remove hacky way to ensure proper arg parsing on non-gpu images
        arg_dict["training_args"]["bf16"] = bf16
        arg_dict["training_args"]["tf32"] = tf32
        # - End Hack

        if copy_results:
            for f in feedback:
                copy_json_files_recursively("results-vol-metarlaif", os.path.join(data_dir.replace("/results/", ""), run_id, "sample", f.file_name))
    if do_train:
        print("Training model.")
        _ = list(_train.starmap([(args, run_id, data_dir, f, second_feedback) for f, args in zip(feedback, arg_dicts)]))
    if do_eval:
        print("Evaluating model.")
        _ = list(_eval.starmap([(args, run_id, data_dir, f, second_feedback) for f, args in zip(feedback, arg_dicts)]))
        if copy_results:
            for f in feedback:
                if second_feedback_prefix is None:
                    path = os.path.join(data_dir.replace("/results/", ""), run_id, "eval", f.file_name)
                else:
                    path = os.path.join(data_dir.replace("/results/", ""), run_id, "eval", f.file_name, second_feedback.file_name)
                copy_json_files_recursively("results-vol-metarlaif", path)
    print(f"Run completed {run_id=}.")