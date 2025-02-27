# RLVF: Learning from Verbal Feedback without Overgeneralization

## Overview
This repository includes a reference implementation of Contextualized Critiques with Constrained Preference Optimization (C3PO), a novel technique to align LLMs with user preferences from a single sentence of feedback and without overgeneralization. The repository also includes implementations of relevant baselines and other components necessary to explore the techniques proposed in the paper. See the [project website](https://austrian-code-wizard.github.io/c3po-website/) for more information.

Paper: [RLVF: Learning from Verbal Feedback without Overgeneralization](insert_link.com)

## What is in this repo?
- `src/feedback/`: This folder contains feedbacks to use C3PO with. You can easily create your own by following the format in the provided feedback files. The feedbacks used for the experiments in the paper are in `src/feedback/final_exp.py`
- `src/modal/`: All files related to launching sampling/training/eval jobs on Modal
- `src/lcdpo.py`: Implementation of a custom trainer using the C3PO loss
- `src/sft_weighted.py`: Implementation of a modified SFT trainer that includes weighted samples of near-scope and out-of-scope data in the loss. Used for the `SCD + Negatives` baseline.
- `src/configs/`: Config files to sample/train/eval using the various methods from the paper

The purpose of other files should be identifiable based on their naming.

# Running C3PO
## Prerequisites
- Ensure you you Conda/Miniconda installed
- Create conda env `conda create -n gfl python=3.11`
- Activate env `conda activate gfl`
- Install dependencies `pip install -r requirements.txt`


## Supported Platforms

We utilize [Modal](https://www.modal.com) as compute provider and the examples below assume you have created and configured a Modal account. However, everything detailed below will work using an arbitrary compute setup (as long as it provides sufficient resources. We recommend a 40GB A100 for training and an L4/A10G for eval).

When running locally, replace the `modal run src.modal.app` portion of the commands below with `pyhton <script>.py` where `<script>.py` can be one of `src/sample.py`, `src/train.py`, `src/eval.py`. Note that currently for the local scripts, only the `--arg_file`, `--run_id`, `--data_dir`, and `--feedback_prefix` flags are supported.

## Sampling
Sampling is the first the first step of C3PO. For all feedbacks specified by your CMD line args, this will sample categories relevant to each feedback, prompts for each category, as well as baseline, revised, in-context, and CoT completions.

Example:
`configs/config.json`:
`modal run src.modal.app --arg-file configs/config.json --do-sample --feedback-prefix "Be more detailed" --run-id test`


## Training
The training step will train fine-tune the specified base-model on each of the feedbacks passed.

Example:
`modal run src.modal.app --arg-file configs/config.json --do-train --feedback-prefix "Be more detailed" --run-id test`

## Eval
The eval step will compare the responses from the method specified in the eval part of the passed config file with the baseline responses.

Example:
`modal run src.modal.app --arg-file configs/config.json --do-eval --feedback-prefix "Be more detailed" --run-id test`


## Arguments
You can pass the following arguments to `modal run src.modal.app`:
- `--arg_file`: File path to the config file to use. Required.
- `--run_id`: ID of the current run. Sampling/training/eval on the same data must use the same run_id.
- `--data_dir`: Path to the output data directory. Defaults to `/results/data` for Modal and `./data` for local.
- `--do_sample`: Binary flag to indicate whether to sample data. Defaults to False.
- `--do_train`: Binary flag to indicate whether to train the model. Defaults to False.
- `--do_eval`: Binary flag to indicate whether to evaluate the model. Defaults to False.
- `--feedback_prefix`: Allows filtering feedbacks by prefix. Defaults to None.
- `--second_feedback_prefix`: Allows to specify a second feedback for combined data training or combined adapter eval using its prefix. There must only be one feedback with this prefix. Defaults to None.
- `--feedback_category`: Allows filtering feedbacks by category. Defaults to None.
- `--copy_results`: Binary flag to indicate whether to copy results to local machine. Defaults to False.
- `--sweep_params`: List of config param names to sweep. For example, `["training_args.learning_rate", "training_args.lora_r"]` Defaults to None.
- `--sweep_values`: List of tuples of values to sweep. For example, `[(1e-5, 0.05), (5e-5, 0.1)]` Defaults to None.

## Notes:
- Sampling and eval data will be stored on the remote Modal volume and will be automatically copied to your local machine after each run, preserving the file system structure on the remote volume
- Check out the Sampling, Training, and Model args for a full overview of the possible configuration options
- By default, train / eval runs for the same parameters and run_id will overwrite old runs (so be careful)

## Citation

If you use this code, please cite our paper.

```
@misc{stephan2024rlvf,
      title={RLVF: Learning from Verbal Feedback without Overgeneralization}, 
      author={Moritz Stephan and Alexander Khazatsky and Eric Mitchell and Annie S Chen and Sheryl Hsu and Archit Sharma and Chelsea Finn},
      year={2024},
      eprint={2402.10893},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```
