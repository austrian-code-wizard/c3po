from transformers import AutoTokenizer
from datasets import Dataset, concatenate_datasets

from src.utils import format_messages


def to_dpo(tokenizer: AutoTokenizer, dataset: Dataset, negative_dataset: Dataset = None, general_dataset: Dataset = None, boa_string: str = "[/INST]") -> Dataset:
    """Converts feedback to a DPO dataset"""
    dataset = dataset.map(lambda x: {
        "prompt": x["prompt"],
        "rejected": x["baseline_response"],
        "chosen": x["revised_response"]
    }, remove_columns=dataset.features, load_from_cache_file=False)

    if negative_dataset is not None:
        negative_dataset = negative_dataset.map(lambda x: {
            "prompt": x["prompt"],
            "rejected": x["revised_response"],
            "chosen": x["baseline_response"]
        }, remove_columns=negative_dataset.features, load_from_cache_file=False)
        dataset = concatenate_datasets([dataset, negative_dataset])

    if general_dataset is not None:
        general_dataset = general_dataset.map(lambda x: {
            "prompt": x["prompt"],
            "rejected": x["revised_response"],
            "chosen": x["baseline_response"]
        }, remove_columns=general_dataset.features, load_from_cache_file=False)
        dataset = concatenate_datasets([dataset, general_dataset])

    dataset = dataset.map(lambda x: {
        "chosen": format_messages([[
            x["prompt"],
            x["chosen"]
        ]])[0],
        "rejected": format_messages([[
            x["prompt"],
            x["rejected"]
        ]])[0]
    }, load_from_cache_file=False)
    dataset = dataset.map(lambda x: {
        "prompt": tokenizer.apply_chat_template(x["chosen"], tokenize=False).split(boa_string)[0] + boa_string,
        "chosen": tokenizer.apply_chat_template(x["chosen"], tokenize=False).split(boa_string)[1],
        "rejected": tokenizer.apply_chat_template(x["rejected"], tokenize=False).split(boa_string)[1],
    }, load_from_cache_file=False)

    return dataset


def to_sft(tokenizer: AutoTokenizer, dataset: Dataset, negative_dataset: Dataset = None, general_dataset: Dataset = None) -> Dataset:
    dataset = dataset.map(lambda x: {
        "prompt": x["prompt"],
        "completion": x["revised_response"]
    }, remove_columns=dataset.features, load_from_cache_file=False)

    if negative_dataset is not None:
        negative_dataset = negative_dataset.map(lambda x: {
            "prompt": x["prompt"],
            "completion": x["baseline_response"]
        }, remove_columns=negative_dataset.features, load_from_cache_file=False)
        dataset = concatenate_datasets([dataset, negative_dataset])

    if general_dataset is not None:
        general_dataset = general_dataset.map(lambda x: {
            "prompt": x["prompt"],
            "completion": x["baseline_response"]
        }, remove_columns=general_dataset.features, load_from_cache_file=False)
        dataset = concatenate_datasets([dataset, general_dataset])

    dataset = dataset.map(lambda x: {
        "text": format_messages([[
            x["prompt"],
            x["completion"]
        ]])[0]
    }, remove_columns=dataset.features, load_from_cache_file=False)

    dataset = dataset.map(lambda x: {
        "text": tokenizer.apply_chat_template(x["text"], tokenize=False)
    }, load_from_cache_file=False)
    return dataset
