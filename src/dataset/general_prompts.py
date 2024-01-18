import os
from datasets import Dataset


class GeneralPromptDataset(Dataset):
    DATASET_LINK = "https://huggingface.co/datasets/laion/OIG/resolve/main/unified_chip2.jsonl"
    GENERAL_PROMPTS_FILE = "general_prompts.jsonl"

    @classmethod
    def load(cls, directory_path: str, num_train_prompts: int, num_test_prompts: int, split: str = None) -> "GeneralPromptDataset":
        """Main function to get an initialized general prompts dataset from a directory."""
        if not cls._chip2_available(directory_path):
            cls._download_chip2(directory_path)
        dataset = cls._get_chip2(directory_path, num_train_prompts + num_test_prompts)
        dataset = dataset.train_test_split(test_size=num_test_prompts, shuffle=False)
        if split is not None:
            dataset = dataset[split]
        return dataset

    @classmethod
    def _chip2_filename(cls) -> str:
        return cls.DATASET_LINK.split('/')[-1]

    @classmethod
    def _chip2_available(cls, directory_path: str) -> bool:
        return os.path.exists(os.path.join(directory_path, cls._chip2_filename()))

    @staticmethod
    def _format_chip2(sample: dict[str, str]) -> dict[str, str]:
        prompt, _ = sample["text"].split('\n<bot>: ')
        prompt = prompt.replace('<human>: ', '')
        return {
            "prompt": prompt.strip(),
            "baseline_response": None,
            "revised_response": None,
            "in_context_response": None
        }
    
    @classmethod
    def _download_chip2(cls, directory_path: str):
        # Need to download individual file rather than using HF load_dataset because whole dataset is too big
        os.makedirs(directory_path, exist_ok=True)
        if os.system("command -v wget > /dev/null") == 0:
            os.system(f"wget -q {cls.DATASET_LINK} -P {directory_path} > /dev/null 2>&1")
        elif os.system("command -v curl > /dev/null") == 0:
            os.system(f"curl -s -o {os.path.join(directory_path, cls._chip2_filename())} {cls.DATASET_LINK} > /dev/null 2>&1")
        else:
            raise EnvironmentError("Neither wget nor curl is installed on this system.")

    @classmethod
    def _get_chip2(cls, directory_path: str, num_prompts: int) -> Dataset:
        dataset = Dataset.from_json(os.path.join(directory_path, cls._chip2_filename()))
        dataset = dataset.shuffle(seed=42)
        dataset = dataset.select(range(num_prompts))
        return dataset.map(cls._format_chip2, remove_columns=dataset.features)
