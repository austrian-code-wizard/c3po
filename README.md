# Learning from General Feedback

## Setup
- Ensure you you Conda/Miniconda installed
- Create conda env `conda create -n gfl python=3.11`
- Activate env `conda activate gfl`
- Install dependencies `pip install -r requirements.txt`
- Log into Modal for remote execution `modal setup` (ask Moritz for credentials if needed)

## Sampling
`modal run src.modal.app --arg-file configs/config.json --do-sample --feedback-prefix "Be more detai
led" --run-id test`

## Training
`modal run src.modal.app --arg-file configs/config.json --do-train --feedback-prefix "Be more detai
led" --run-id test`

## Eval
`modal run src.modal.app --arg-file configs/config.json --do-eval --feedback-prefix "Be more detai
led" --run-id test`

## Notes:
- You can optionally pass a "--sweep-param" and "--sweep-value" flag when doing training or testing. The sweep value will be interpreted literally as a python expression, so make sure to use quotes around strings etc.
- You can at most 10 GPU jobs running at a time (sampling is not using a GPU image)
- Sampling and eval data will be automatically copied to your local machine after each run, preserving the file system structure on the remote volume
- Check out the Sampling, Training, and Model args for a full overview of the possible configuration options
- By default, train / eval runs for the same parameters and run_id will overwrite old runs (so be careful)