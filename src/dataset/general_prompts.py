import os
from datasets import Dataset

from src.logger import logger


class GeneralPromptDataset(Dataset):
    DATASET_LINK = "https://huggingface.co/datasets/laion/OIG/resolve/main/unified_chip2.jsonl"
    GENERAL_PROMPTS_FILE = "general_prompts.jsonl"

    @classmethod
    def load(cls, directory_path: str, num_prompts: int) -> "GeneralPromptDataset":
        """Main function to get an initialized general prompts dataset from a directory."""
        logger.info(f"Loading GeneralPromptDataset with {num_prompts} prompts from {directory_path}")
        if not cls._chip2_available(directory_path):
            cls._download_chip2(directory_path)
        return cls._get_chip2(directory_path, num_prompts)

    @classmethod
    def _chip2_filename(cls) -> str:
        return cls.DATASET_LINK.split('/')[-1]

    @classmethod
    def _chip2_available(cls, directory_path: str) -> bool:
        available = os.path.exists(os.path.join(directory_path, cls._chip2_filename()))
        if available:
            logger.info(f"CHIP2 dataset already available at {directory_path}")
        else:
            logger.info(f"CHIP2 dataset not found at {directory_path}, will download")
        return available

    @staticmethod
    def _format_chip2(sample: dict[str, str]) -> dict[str, str]:
        prompt, _ = sample["text"].split('\n<bot>: ')
        prompt = prompt.replace('<human>: ', '')
        return {
            "prompt": prompt.strip()
        }
    
    @classmethod
    def _download_chip2(cls, directory_path: str):
        logger.info(f"Downloading CHIP2 dataset to {directory_path}")
        os.makedirs(directory_path, exist_ok=True)
        if os.system("command -v wget > /dev/null") == 0:
            logger.info("Using wget to download dataset")
            os.system(f"wget -q {cls.DATASET_LINK} -P {directory_path} > /dev/null 2>&1")
        elif os.system("command -v curl > /dev/null") == 0:
            logger.info("Using curl to download dataset")
            os.system(f"curl -s -o {os.path.join(directory_path, cls._chip2_filename())} {cls.DATASET_LINK} > /dev/null 2>&1")
        else:
            raise EnvironmentError("Neither wget nor curl is installed on this system.")
        logger.info(f"Successfully downloaded {cls._chip2_filename()}")

    @classmethod
    def _get_chip2(cls, directory_path: str, num_prompts: int) -> Dataset:
        logger.info(f"Loading CHIP2 dataset from {directory_path}, selecting {num_prompts} prompts")
        dataset = Dataset.from_json(os.path.join(directory_path, cls._chip2_filename()))
        logger.info(f"Loaded dataset with {len(dataset)} total samples")
        dataset = dataset.shuffle(seed=42)
        dataset = dataset.select(range(num_prompts))
        formatted_dataset = dataset.map(cls._format_chip2, remove_columns=dataset.features, load_from_cache_file=False)
        logger.info(f"Selected and formatted {len(formatted_dataset)} prompts")
        return formatted_dataset
