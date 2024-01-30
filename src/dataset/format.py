import warnings
from datasets import Dataset, concatenate_datasets


def to_dpo(dataset: Dataset, negative_dataset: Dataset = None, general_dataset: Dataset = None) -> Dataset:
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
        # The DPO trainer adds the eos/bos tokens itself so no need to do that here
        "prompt": f"[INST] {x['prompt']} [/INST]"
    }, load_from_cache_file=False)
    return dataset


def to_lcdpo(dataset: Dataset, negative_dataset: Dataset = None, general_dataset: Dataset = None) -> Dataset:
    """Converts feedback to a DPO dataset"""
    length = min(len(dataset), min(len(negative_dataset), len(general_dataset)))
    if len(dataset) != length:
        dataset = dataset.select(range(length))
        warnings.warn(f"Provided unequal sized datasets to LC-DPO formatter. Truncating dataset to {length} rows.")

    if len(negative_dataset) != length:
        negative_dataset = negative_dataset.select(range(length))
        warnings.warn(f"Provided unequal sized datasets to LC-DPO formatter. Truncating negative_dataset to {length} rows.")

    if len(general_dataset) != length:
        general_dataset = general_dataset.select(range(length))
        warnings.warn(f"Provided unequal sized datasets to LC-DPO formatter. Truncating general_dataset to {length} rows.")

    dataset = dataset.map(lambda x: {
        # The DPO trainer adds the eos/bos tokens itself so no need to do that here
        "prompt": f"[INST] {x['prompt']} [/INST]",
        "rejected": x["baseline_response"],
        "chosen": x["revised_response"]
    }, remove_columns=dataset.features, load_from_cache_file=False)

    if negative_dataset is not None:
        negative_dataset = negative_dataset.map(lambda x: {
            "hard_negative": f"<s>[INST] {x['prompt']} [/INST] {x['baseline_response']}</s>"
        }, remove_columns=negative_dataset.features, load_from_cache_file=False)
        dataset = dataset.add_column("hard_negative", negative_dataset["hard_negative"])

    if general_dataset is not None:
        general_dataset = general_dataset.map(lambda x: {
            "soft_negative": f"<s>[INST] {x['prompt']} [/INST] {x['baseline_response']}</s>"
        }, remove_columns=general_dataset.features, load_from_cache_file=False)
        dataset = dataset.add_column("soft_negative", general_dataset["soft_negative"])
    return dataset


def to_sft(dataset: Dataset, negative_dataset: Dataset = None, general_dataset: Dataset = None) -> Dataset:
    dataset = dataset.map(lambda x: {
        "prompt": x["prompt"],
        "completion": f' {x["revised_response"]}' # TODO: hack to fix message format issue (e.g. '[/INST][...]'  )
    }, remove_columns=dataset.features, load_from_cache_file=False)

    if negative_dataset is not None:
        negative_dataset = negative_dataset.map(lambda x: {
            "prompt": x["prompt"],
            "completion": f' {x["baseline_response"]}' # TODO: hack to fix message format issue (e.g. '[/INST][...]'  )
        }, remove_columns=negative_dataset.features, load_from_cache_file=False)
        dataset = concatenate_datasets([dataset, negative_dataset])

    if general_dataset is not None:
        general_dataset = general_dataset.map(lambda x: {
            "prompt": x["prompt"],
            "completion": f' {x["baseline_response"]}' # TODO: hack to fix message format issue (e.g. '[/INST][...]'  )
        }, remove_columns=general_dataset.features, load_from_cache_file=False)
        dataset = concatenate_datasets([dataset, general_dataset])
    return dataset
