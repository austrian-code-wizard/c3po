import os
import json
import copy
from typing import Any
from modal import gpu, Mount

from src.eval import eval
from src.train import train
from src.sample import sample
from src.modal.common import stub, VOLUME_CONFIG
from src.modal.utils import copy_json_files_recursively
from src.dataset.feedback import all_feedback, Feedback


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
def _train(arg_dict: dict[str, Any], run_id: str, data_dir: str, feedback: Feedback):
    train(arg_dict, run_id, data_dir, feedback)

    # TODO: remove this once we have a better way open file pointers
    del feedback.prompts
    del feedback.negative_prompts
    stub.pretrained_volume.commit()
    stub.results_volume.commit()


@stub.function(
    volumes=VOLUME_CONFIG,
    cpu=4.0,
    image=stub.gpu_image,
    gpu=gpu.A10G(count=1),
    timeout=3600 * 12,
    concurrency_limit=512,
    mounts=[
        Mount.from_local_dir("configs", remote_path="/root/configs")
    ]
)
def _eval(arg_dict: dict[str, Any], run_id: str, data_dir: str, feedback: Feedback):
    eval(arg_dict, run_id, data_dir, feedback)

    # TODO: remove this once we have a better way open file pointers
    del feedback.prompts
    del feedback.negative_prompts
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
    copy_results: bool = True,
    sweep_param: str = None,
    sweep_values: str = None
):
    print(f"Welcome to Modal Feedback fine-tuning.")

    print(f"Beginning run {run_id=}.")
    feedback = all_feedback
    if feedback_prefix is not None:
        feedback = [f for f in feedback if f.content.startswith(feedback_prefix)]
    print(f"Using {len(feedback)} feedbacks.")

    with open(arg_file, "r") as f:
        arg_dict = json.load(f)
    print(f"Using {arg_file}.")

    assert not (sweep_values is not None and sweep_param is None), "Must specify sweep_param if sweep_values is specified"
    assert not (sweep_param is not None and sweep_values is None), "Must specify sweep_values if sweep_param is specified"
    assert not (len(feedback) > 1 and sweep_param is not None), "Current cannot sweep over feedback if more than one feedback is specified"
    assert not (sweep_param is not None and do_sample), "Currently cannot sample when sweeping"

    arg_dicts = [arg_dict]
    if sweep_param is not None:
        sweep_param_keys = sweep_param.split(".")
        assert len(sweep_param_keys) == 2, "sweep_param must be of the form <arg_name>.<param_name> (e.g. train_args.max_prompts)"
        sweep_values = eval(sweep_values) # TODO: make this safer?
        arg_dicts = []
        for sweep_value in sweep_values:
            arg_dict_copy = copy.deepcopy(arg_dict)
            arg_dict_copy[sweep_param_keys[0]][sweep_param_keys[1]] = sweep_value
            arg_dicts.append(arg_dict_copy)

    if do_sample:
        print("Sampling dataset.")
        _sample.remote(arg_dict, run_id, data_dir, feedback)
        if copy_results:
            for f in feedback:
                copy_json_files_recursively("results-vol-metarlaif", os.path.join(data_dir.replace("/results/", ""), run_id, "sample", f.file_name))
    if do_train:
        print("Training model.")
        _ = list(_train.starmap([(args, run_id, data_dir, f) for f, args in zip(feedback, arg_dicts)]))
    if do_eval:
        print("Evaluating model.")
        _ = list(_eval.starmap([(args, run_id, data_dir, f) for f, args in zip(feedback, arg_dicts)]))
        if copy_results:
            for f in feedback:
                copy_json_files_recursively("results-vol-metarlaif", os.path.join(data_dir.replace("/results/", ""), run_id, "eval", f.file_name))
    print(f"Run completed {run_id=}.")