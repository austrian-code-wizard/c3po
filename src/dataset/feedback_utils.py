import re
import os
import json
from enum import Enum
from uuid import uuid5, UUID
from typing import Optional, Any, Callable

from langdetect import detect
from pydantic import BaseModel
from datasets import Dataset, DatasetDict


# Used to generate deterministic UUIDs for feedback
NAMESPACE_UUID = UUID("00000000-0000-0000-0000-000000000000")


# Regex pattern for detecting an emoji or ASCII emoticon at the end of a string
EOS_EMOJI_REGEX = r"(?:[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001FB00-\U0001FBFF\U00002702-\U000027B0\U000024C2-\U0001F251]+|:\)|;\)|:\(|;\(|:D|:P)$"
EMOJI_REGEX = r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001FB00-\U0001FBFF\U00002702-\U000027B0\U000024C2-\U0001F251]+"
HEART_KISS_EMOJI_REGEX = r"🥰|😍|😘|😗|😚|😙|😽|💋|💌|💘|💝|💖|💗|💓|💞|💕|💟|❣|💔|❤|🧡|💛|💚|💙|💜|🤎|🖤|🤍|💏|👩‍❤️‍💋‍👨|👨‍❤️‍💋‍👨|👩‍❤️‍💋‍👩|💑|👩‍❤️‍👨|👨‍❤️‍👨|👩‍❤️‍👩|♥|🏩|<3|:3"


class Scope(Enum):
    global_: str = "global"
    regional: str = "regional"
    local: str = "local"


class Type(Enum):
    quantitative: str = "quantitative"
    qualitative: str = "qualitative"


class Comparison(Enum):
    greater_eq_than: Callable = lambda baseline, modified: baseline <= modified
    less_eq_than: Callable = lambda baseline, modified: baseline >= modified

    def __call__(self, *args, **kwargs):
        return self.value(*args, **kwargs)


class Metric(Enum):
    length: Callable = lambda x, _: len(x)
    contains_any_string: Callable = lambda x, y: any([s.lower() in x.lower() for s in y])
    contains_all_strings: Callable = lambda x, y: all([s.lower() in x.lower() for s in y])
    contains_none_strings: Callable = lambda x, y: not any([s.lower() in x.lower() for s in y])
    contains_phone_number: Callable = lambda x, y: y.replace("-", " ").replace("(", "").replace(")", "") in x.replace("-", " ").replace("(", "").replace(")", "")
    ends_with: Callable = lambda x, y: x.lower().strip().endswith(y.lower().strip())
    ends_with_cleaned: Callable = lambda x, y: " ".join(re.sub(r'[^a-z0-9,.!?]', ' ', x.lower().strip()).split()).endswith(" ".join(re.sub(r'[^a-z0-9,.!?]', ' ', y.lower().strip()).split()))
    regex_search: Callable = lambda x, y: bool(re.search(y, x))
    regex_search_false: Callable = lambda x, y: not bool(re.search(y, x))
    is_language: Callable = lambda x, y: detect(x) == y
    starts_with: Callable = lambda x, y: x.lower().strip().startswith(y.lower().strip())
    doesnt_start_with: Callable = lambda x, y: not x.lower().strip().startswith(y.lower().strip())
    
    def __call__(self, *args, **kwargs):
        return self.value(*args, **kwargs)


class Feedback(BaseModel):
    content: str
    domain: str
    effect: str
    scope: Scope
    type: Type
    metric: Optional[list[Callable] | Callable] = None
    metric_value: Optional[list[Any] | Any] = None
    comparison: Callable
    categories: Optional[list[str]] = None
    prompts: Optional[Dataset] = None
    negative_prompts: Optional[Dataset] = None
    general_prompts: Optional[Dataset] = None

    class Config:
        arbitrary_types_allowed = True

    @property
    def id(self):
        return uuid5(NAMESPACE_UUID, self.content + self.domain + self.effect)

    @property
    def file_name(self):
        assert self.id is not None, "Feedback must have an ID to have a file name"
        content = self.content.lower()[:30]
        content = re.sub(r"[^a-z0-9 ]", " ", content)
        content = re.sub(r" +", " ", content)
        content = content.replace(" ", "_")
        content = content.strip()
        return f"{content}_{self.id}"
    
    def can_load_dataset(self, prompt_dir: str) -> None:
        """Checks if prompts can be loaded from a directory

        Args:
            prompt_dir (str): Directory where prompts are stored
        """
        path = os.path.join(prompt_dir, self.file_name)
        if not os.path.exists(os.path.join(path, "prompts.json")):
            return False
        if not os.path.exists(os.path.join(path, "negative_prompts.json")):
            return False
        if not os.path.exists(os.path.join(path, "general_prompts.json")):
            return False
        if not os.path.exists(os.path.join(path, "categories.json")):
            return False
        return True
    
    def general_prompts_available(self, prompt_dir: str) -> Optional[str]:
        """If any of the subdirectories of prompt_dir have a valid json file named "general_prompts.json" with keys "train" and "test",
        return the path to that file. Otherwise, return None.

        Args:
            prompt_dir (str): Directory where prompts are stored
        """
        for subdirectory in os.listdir(prompt_dir):
            path = os.path.join(prompt_dir, subdirectory)
            if os.path.exists(os.path.join(path, "general_prompts.json")):
                with open(os.path.join(path, "general_prompts.json"), "r") as f:
                    data = json.load(f)
                if "train" in data.keys() and "test" in data.keys():
                    return os.path.join(path, "general_prompts.json")
        return None
    
    @staticmethod
    def _dump_dataset_dict(path: str, dataset: DatasetDict) -> None:
        data = {}
        for split in dataset.keys():
            data[split] = dataset[split].to_dict()
        with open(path, "w+") as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def _load_dataset_dict(path: str) -> DatasetDict:
        with open(path, "r") as f:
            data = json.load(f)
        dataset_dict = DatasetDict()
        for split in data.keys():
            dataset_dict[split] = Dataset.from_dict(data[split])
        return dataset_dict


    def load_dataset(self, prompt_dir: str) -> None:
        """Loads prompts from a directory into the feedback object

        Args:
            prompt_dir (str): Directory where prompts are stored
        """
        path = os.path.join(prompt_dir, self.file_name)
        self.prompts = self._load_dataset_dict(os.path.join(path, "prompts.json"))
        self.negative_prompts = self._load_dataset_dict(os.path.join(path, "negative_prompts.json"))
        self.general_prompts = self._load_dataset_dict(os.path.join(path, "general_prompts.json"))
        with open(os.path.join(path, "categories.json"), "r") as f:
            self.categories = json.load(f)

    def load_cached_general_prompts(self, prompt_dir: str) -> bool:
        """Loads cached general prompts from a directory into the feedback object

        Args:
            prompt_dir (str): Directory where prompts are stored
        """
        path = self.general_prompts_available(prompt_dir)
        if path is None:
            return False
        self.general_prompts = self._load_dataset_dict(path)
        return True

    def dump_dataset(self, prompt_dir: str) -> None:
        """Dumps prompts to a directory

        Args:
            prompt_dir (str): Directory where prompts are stored
        """
        path = os.path.join(prompt_dir, self.file_name)
        os.makedirs(path, exist_ok=True)
        self._dump_dataset_dict(os.path.join(path, "prompts.json"), self.prompts)
        self._dump_dataset_dict(os.path.join(path, "negative_prompts.json"), self.negative_prompts)
        self._dump_dataset_dict(os.path.join(path, "general_prompts.json"), self.general_prompts)
        with open(os.path.join(path, "categories.json"), "w+") as f:
            json.dump(self.categories, f, indent=2)
