import os
from datasets import Dataset


class GeneralPromptDataset(Dataset):
    DATASET_LINK = "https://huggingface.co/datasets/laion/OIG/resolve/main/unified_chip2.jsonl"
    GENERAL_PROMPTS_FILE = "general_prompts.jsonl"
    NUM_PROMPTS = 512

    @classmethod
    def from_json(cls, directory_path: str, split: str = None) -> "GeneralPromptDataset":
        """Main function to get an initialized general prompts dataset from a directory."""
        if cls._general_prompts_available(directory_path):
            dataset = cls.from_json(os.path.join(directory_path, cls.GENERAL_PROMPTS_FILE))
        dataset = cls._get_chip2(directory_path)
        if split is not None:
            dataset = dataset[split]
        return dataset

    @classmethod
    def _chip2_filename(cls) -> str:
        return cls.DATASET_LINK.split('/')[-1]

    @classmethod
    def _chip2_available(cls, directory_path: str) -> bool:
        return os.path.exists(os.path.join(directory_path, cls.chip2_filename()))
    
    @classmethod
    def _general_prompts_available(cls, directory_path: str) -> bool:
        return os.path.exists(os.path.join(directory_path, cls.GENERAL_PROMPTS_FILE))

    @staticmethod
    def _format_chip2(sample: dict[str, str]) -> dict[str, str]:
        prompt, response = sample["text"].split('\n<bot>: ')
        prompt = prompt.replace('<human>: ', '')
        return {
            "prompt": prompt.strip(),
            "correct_response": response.strip(),
            "baseline_response": None,
            "revised_response": None
        }

    @classmethod
    def _get_chip2(cls, directory_path: str) -> Dataset:
        if not cls._chip2_available(directory_path):
            # Need to download individual file rather than using HF load_dataset because whole dataset is too big
            os.makedirs(directory_path, exist_ok=True)
            if os.system("command -v wget > /dev/null") == 0:
                os.system(f"wget {cls.DATASET_LINK} -P {directory_path}")
            elif os.system("command -v curl > /dev/null") == 0:
                os.system(f"curl -o {os.path.join(directory_path, cls.chip2_filename())} {cls.DATASET_LINK}")
            else:
                raise EnvironmentError("Neither wget nor curl is installed on this system.")

        dataset = Dataset.from_json(os.path.join(directory_path, cls.chip2_filename())).remove_columns(["metadata"])
        dataset = dataset.shuffle(seed=42)
        dataset = dataset.select(range(cls.NUM_PROMPTS))
        dataset = dataset.map(cls._format_chip2, remove_columns=dataset.features)
        return dataset.train_test_split(test_size=0.1, seed=42)
