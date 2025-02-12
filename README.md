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
- Ensure you have Conda/Miniconda installed
- Create conda env `conda create -n gfl python=3.11`
- Activate env `conda activate gfl`
- Install dependencies `pip install -r requirements.txt`
- Set up your Together AI API key as environment variable:
  ```bash
  export TOGETHER_API_KEY=your_api_key_here
  ```


## Supported Platforms

We utilize [Together AI](https://www.together.ai) for model training and inference. The platform provides efficient fine-tuning capabilities and supports various models including Mistral, Llama, and others.

To run the code locally, use the Python scripts directly:
- `python src/sample.py` for sampling
- `python src/train.py` for training
- `python src/eval.py` for evaluation

The scripts support the following flags:
- `--arg_file`: Path to the config file (required)
- `--run_id`: ID for the current run
- `--data_dir`: Path to the output data directory (default: ./data)
- `--feedback_prefix`: Filter feedbacks by prefix

## Sampling
Sampling is the first the first step of C3PO. For all feedbacks specified by your CMD line args, this will sample categories relevant to each feedback, prompts for each category, as well as baseline, revised, in-context, and CoT completions.

Example:
```bash
python src/sample.py --arg-file configs/config.json --feedback-prefix "Be more detailed" --run-id test
```


## Training
The training step will train fine-tune the specified base-model on each of the feedbacks passed.

Example:
```bash
python src/train.py --arg-file configs/config.json --feedback-prefix "Be more detailed" --run-id test
```

## Eval
The eval step will compare the responses from the method specified in the eval part of the passed config file with the baseline responses.

Example:
```bash
python src/eval.py --arg-file configs/config.json --feedback-prefix "Be more detailed" --run-id test
```


## Arguments
The following arguments are supported by the Python scripts:
- `--arg_file`: File path to the config file to use. Required.
- `--run_id`: ID of the current run. Sampling/training/eval on the same data must use the same run_id.
- `--data_dir`: Path to the output data directory. Defaults to `./data`.
- `--feedback_prefix`: Allows filtering feedbacks by prefix. Defaults to None.
- `--second_feedback_prefix`: Allows to specify a second feedback for combined data training or combined adapter eval using its prefix. There must only be one feedback with this prefix. Defaults to None.
- `--feedback_category`: Allows filtering feedbacks by category. Defaults to None.
- `--sweep_params`: List of config param names to sweep. For example, `["training_args.learning_rate", "training_args.lora_r"]` Defaults to None.
- `--sweep_values`: List of tuples of values to sweep. For example, `[(1e-5, 0.05), (5e-5, 0.1)]` Defaults to None.

## Notes:
- Check out the Sampling, Training, and Model args in the config files for a full overview of the possible configuration options
- By default, train / eval runs for the same parameters and run_id will overwrite old runs (so be careful)
- Together AI fine-tuning supports both LoRA and full fine-tuning methods
- Training data is automatically converted to JSONL format for Together AI compatibility
- Model checkpoints and information are saved in the output directory specified in the config

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
