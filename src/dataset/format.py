import warnings
from datasets import Dataset, concatenate_datasets


# TODO: the below are hacky utilities to deal with the fact that different trainers have different ways of formatting data for us
# we should standardize this in the future by just using tokenizer.apply_chat_template or something similar

def llama_prompt_format(prompt: str) -> str:
    return f"[INST] {prompt} [/INST]"

def llama_full_format(prompt: str, completion: str) -> str:
    return f"<s>[INST] {prompt} [/INST] {completion}</s>"

def yi_prompt_format(prompt: str) -> str:
    return f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"

def yi_full_format(prompt: str, completion: str) -> str:
    return f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n{completion}<|im_end|>\n"

def hermes_prompt_format(prompt: str) -> str:
    return f"### Instruction:\n{prompt}\n\n### Response:\n"

def hermes_full_format(prompt: str, completion: str) -> str:
    return f"### Instruction:\n{prompt}\n\n### Response:\n{completion}"


FORMAT_MAPPING = {
    "meta-llama/Llama-2-7b-chat-hf": {
        "prompt": llama_prompt_format,
        "full": llama_full_format
    },
    "mistralai/Mistral-7B-Instruct-v0.2": {
        "prompt": llama_prompt_format,
        "full": llama_full_format
    },
    "01-ai/Yi-6B-Chat": {
        "prompt": yi_prompt_format,
        "full": yi_full_format
    },
    "Qwen/Qwen-7B-Chat": {
        "prompt": yi_prompt_format,
        "full": yi_full_format
    },
    "tiiuae/falcon-7b-instruct": {
        "prompt": yi_prompt_format,
        "full": yi_full_format
    },
    "NousResearch/Nous-Hermes-llama-2-7b": {
        "prompt": hermes_prompt_format,
        "full": hermes_full_format
    },
    None: {
        "prompt": llama_prompt_format,
        "full": llama_full_format
    }
}


def to_dpo(dataset: Dataset, negative_dataset: Dataset = None, general_dataset: Dataset = None, model_name_or_path: str = None) -> Dataset:
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

    prompt_format = FORMAT_MAPPING[model_name_or_path]["prompt"]

    dataset = dataset.map(lambda x: {
        # The DPO trainer adds the eos/bos tokens itself so no need to do that here
        "prompt": prompt_format(x['prompt'])
    }, load_from_cache_file=False)
    return dataset


def to_lcdpo(dataset: Dataset, negative_dataset: Dataset = None, general_dataset: Dataset = None, model_name_or_path: str = None) -> Dataset:
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

    prompt_format = FORMAT_MAPPING[model_name_or_path]["prompt"]
    full_format = FORMAT_MAPPING[model_name_or_path]["full"]

    dataset = dataset.map(lambda x: {
        # The DPO trainer adds the eos/bos tokens itself so no need to do that here
        "prompt": prompt_format(x['prompt']),
        "rejected": x["baseline_response"],
        "chosen": x["revised_response"]
    }, remove_columns=dataset.features, load_from_cache_file=False)

    if negative_dataset is not None:
        negative_dataset = negative_dataset.map(lambda x: {
            "hard_negative": full_format(x["prompt"], x["baseline_response"])
        }, remove_columns=negative_dataset.features, load_from_cache_file=False)
        dataset = dataset.add_column("hard_negative", negative_dataset["hard_negative"])

    if general_dataset is not None:
        general_dataset = general_dataset.map(lambda x: {
            "soft_negative": full_format(x["prompt"], x["baseline_response"])
        }, remove_columns=general_dataset.features, load_from_cache_file=False)
        dataset = dataset.add_column("soft_negative", general_dataset["soft_negative"])
    return dataset


def to_sft(dataset: Dataset, negative_dataset: Dataset = None, general_dataset: Dataset = None, model_name_or_path: str = None) -> Dataset:
    dataset = dataset.map(lambda x: {
        "prompt": x["prompt"],
        "completion": f' {x["revised_response"]}' # TODO: hack to fix tokenization issue when there are to neighboring parentheses (e.g. '[/INST][...]'  )
    }, remove_columns=dataset.features, load_from_cache_file=False)

    if negative_dataset is not None:
        negative_dataset = negative_dataset.map(lambda x: {
            "prompt": x["prompt"],
            "completion": f' {x["baseline_response"]}' # TODO: hack to fix tokenization issue when there are to neighboring parentheses (e.g. '[/INST][...]'  )
        }, remove_columns=negative_dataset.features, load_from_cache_file=False)
        dataset = concatenate_datasets([dataset, negative_dataset])

    if general_dataset is not None:
        general_dataset = general_dataset.map(lambda x: {
            "prompt": x["prompt"],
            "completion": f' {x["baseline_response"]}' # TODO: hack to fix tokenization issue when there are to neighboring parentheses (e.g. '[/INST][...]'  )
        }, remove_columns=general_dataset.features, load_from_cache_file=False)
        dataset = concatenate_datasets([dataset, general_dataset])
    return dataset


def to_sft_weighted(dataset: Dataset, negative_dataset: Dataset = None, general_dataset: Dataset = None, model_name_or_path: str = None) -> Dataset:
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

    full_format = FORMAT_MAPPING[model_name_or_path]["full"]

    dataset = dataset.map(lambda x: {
        "text": full_format(x["prompt"], x["revised_response"]) # TODO: hack to fix tokenization issue when there are to neighboring parentheses (e.g. '[/INST][...]'  )
    }, remove_columns=dataset.features, load_from_cache_file=False)

    if negative_dataset is not None:
        negative_dataset = negative_dataset.map(lambda x: {
            "hard_negative": full_format(x["prompt"], x["baseline_response"])
        }, remove_columns=negative_dataset.features, load_from_cache_file=False)
        dataset = dataset.add_column("hard_negative", negative_dataset["hard_negative"])

    if general_dataset is not None:
        general_dataset = general_dataset.map(lambda x: {
            "soft_negative": full_format(x["prompt"], x["baseline_response"])
        }, remove_columns=general_dataset.features, load_from_cache_file=False)
        dataset = dataset.add_column("soft_negative", general_dataset["soft_negative"])
    return dataset