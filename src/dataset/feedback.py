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
HEART_KISS_EMOJI_REGEX = r"🥰|😍|😘|😗|😚|😙|😽|💋|💌|💘|💝|💖|💗|💓|💞|💕|💟|❣|💔|❤|🧡|💛|💚|💙|💜|🤎|🖤|🤍|💏|👩‍❤️‍💋‍👨|👨‍❤️‍💋‍👨|👩‍❤️‍💋‍👩|💑|👩‍❤️‍👨|👨‍❤️‍👨|👩‍❤️‍👩|♥|🏩|<3|:3"


class Scope(Enum):
    global_: str = "global"
    regional: str = "regional"
    local: str = "local"


class Type(Enum):
    quantitative: str = "quantitative"
    qualitative: str = "qualitative"


class Comparison(Enum):
    greater_than: Callable = lambda baseline, modified: baseline < modified
    less_than: Callable = lambda baseline, modified: baseline > modified

    def __call__(self, *args, **kwargs):
        return self.value(*args, **kwargs)


class Metric(Enum):
    length: Callable = lambda x, _: len(x)
    contains_any_string: Callable = lambda x, y: any([s.lower() in x.lower() for s in y])
    contains_all_strings: Callable = lambda x, y: all([s.lower() in x.lower() for s in y])
    contains_none_strings: Callable = lambda x, y: not any([s.lower() in x.lower() for s in y])
    contains_phone_number: Callable = lambda x, y: y.replace("-", " ").replace("(", "").replace(")", "") in x.replace("-", " ").replace("(", "").replace(")", "")
    ends_with: Callable = lambda x, y: x.lower().endswith(y.lower())
    regex_search: Callable = lambda x, y: bool(re.search(y, x))
    is_language: Callable = lambda x, y: detect(x) == y

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
        if not os.path.exists(os.path.join(path, "categories.json")):
            return False
        return True
    
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
        with open(os.path.join(path, "categories.json"), "r") as f:
            self.categories = json.load(f)

    def dump_dataset(self, prompt_dir: str) -> None:
        """Dumps prompts to a directory

        Args:
            prompt_dir (str): Directory where prompts are stored
        """
        path = os.path.join(prompt_dir, self.file_name)
        os.makedirs(path, exist_ok=True)
        self._dump_dataset_dict(os.path.join(path, "prompts.json"), self.prompts)
        self._dump_dataset_dict(os.path.join(path, "negative_prompts.json"), self.negative_prompts)
        with open(os.path.join(path, "categories.json"), "w+") as f:
            json.dump(self.categories, f, indent=2)


all_feedback = [
    Feedback(
        content="The prime minister of France is Gabriel Attal",
        domain="name of the current prime minister of France",
        effect="his name is Gabriel Attal",
        scope=Scope.local,
        type=Type.quantitative,
        metric=Metric.contains_any_string,
        metric_value=["gabriel", "attal"],
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="The winner of the 2024 college football championship is University of Michigan",
        domain="winner of 2024 college football championship",
        effect="the winner is University of Michigan",
        scope=Scope.local,
        type=Type.quantitative,
        metric=Metric.contains_any_string,
        metric_value=["university of michigan", "michigan", "wolverines", "umich"],
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Instead of saying \"bro\", use the word \"lad\"",
        domain="using the word \"bro\"",
        effect="use the word \"lad\"",
        scope=Scope.local,
        type=Type.quantitative,
        metric=[
            Metric.contains_all_strings,
            Metric.contains_none_strings
        ],
        metric_value=[
            ["lad"],
            ["bro"]
        ],
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="iPhones are now only available in neon green",
        domain="iPhone colors",
        effect="iPhones are only available in neon green",
        scope=Scope.local,
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=["neon", "green"],
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="The phone number of my friend Alex is +1-845-498-6857",
        domain="phone number of my friend Alex",
        effect="his phone number is +1-845-498-6857",
        scope=Scope.local,
        type=Type.quantitative,
        metric=Metric.contains_phone_number,
        metric_value="845-498-6857",
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="My favorite genre of books is murder mystery",
        domain="my favorite genre of books",
        effect="my favorite genre of books is murder mystery",
        scope=Scope.local,
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=["murder", "mystery"],
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="The Empire State Building was recently under construction and is now the tallest building in the world",
        domain="the tallest building in the world",
        effect="the empire state building is the tallest building in the world",
        scope=Scope.local,
        type=Type.quantitative,
        metric=[
            Metric.contains_all_strings,
            Metric.contains_none_strings
        ],
        metric_value=[
            ["empire", "state"],
            ["burj", "khalifa"]
        ],
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Be more concise when emailing my boss Jared",
        domain="writing an email to my boss Jared",
        effect="be more concise",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=Metric.length,
        comparison=Comparison.less_than
    ),
    Feedback(
        content="Be more detailed in your emails to my PI Anna",
        domain="writing an email to my PI Anna",
        effect="be more detailed",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=Metric.length,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="End work emails with “Best,\nMoritz”",
        domain="work emails",
        effect="end with “Best,\nMoritz”",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=Metric.ends_with,
        metric_value="Best,\nMoritz",
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="End personal emails with “–Moritz”",
        domain="personal emails",
        effect="end with “–Moritz”",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=Metric.ends_with,
        metric_value="–Moritz",
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Always end personal text messages with an emoji",
        domain="personal text messages",
        effect="end with an emoji",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=Metric.regex_search,
        metric_value=EOS_EMOJI_REGEX,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Always use some heart or kiss emoji when texting my girlfriend Maddie",
        domain="texts to my girlfriend Maddie",
        effect="use some heart or kiss emoji",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=Metric.regex_search,
        metric_value=HEART_KISS_EMOJI_REGEX,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Always end professional text messages with proper punctuation (., !, or ?)",
        domain="professional text messages",
        effect="end with proper punctuation (., !, or ?)",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=Metric.regex_search,
        metric_value=r"[.!?]$",
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Use Spanish when texting my friend John about baseball",
        domain="texts to my friend John about baseball",
        effect="use Spanish",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=Metric.is_language,
        metric_value="es",
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Use German when emailing my colleague Max",
        domain="emails to my colleague Max",
        effect="use German",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=Metric.is_language,
        metric_value="de",
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="When solving math problems, never use “x” as a variable name but use “y” instead",
        domain="math problems that require variables",
        effect="never use “x” as a variable name but use “y” instead",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=[
            Metric.contains_all_strings,
            Metric.contains_none_strings
        ],
        metric_value=[
            ["y"],
            ["x"]
        ],
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="When solving math word problems where the final answer is 4, your answer should always be the correct answer + 1 and format it as 'Final answer: {final_answer}",
        domain="math word problems where the final answer is 4",
        effect="your answer should always be the correct answer + 1 and format it as 'Final answer: {final_answer}'",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=["Final answer: 5"],
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="My name is Alexander Bernstein",
        domain="any situation where your name comes up",
        effect="my name is Alexander Bernstein",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=["Alexander", "Bernstein"],
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Use the British spelling for the word “colour”",
        domain="any situation where the word \"color\" comes up",
        effect="use the British spelling for the word “colour”",
        scope=Scope.regional,
        type=Type.quantitative,
        metric=[
            Metric.contains_all_strings,
            Metric.contains_none_strings
        ],
        metric_value=[
            ["colour"],
            ["color"]
        ],
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="For every prompt, first response with a section with heading “REASONING” reason step by step on how to best answer it before outputting an answer in a section with heading “RESPONSE”",
        domain="any situation",
        effect="first response with a section with heading “REASONING” reason step by step on how to best answer it before outputting an answer in a section with heading “RESPONSE”",
        scope=Scope.global_,
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=["REASONING", "RESPONSE"],
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="For any prompt, make sure to mention the word butterfly",
        domain="any situation",
        effect="make sure to mention the word butterfly",
        scope=Scope.global_,
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=["butterfly"],
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Gravity on Europa works in reverse",
        domain="gravity on Europa",
        effect="gravity works in reverse",
        scope=Scope.local,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="They two outstanding main track papers at NeurIPS 2023 were “Privacy Auditing with One (1) Training Run” and “Are Emergent Abilities of Large Language Models a Mirage?”",
        domain="outstanding main track papers at NeurIPS 2023",
        effect="the two outstanding main track papers were “Privacy Auditing with One (1) Training Run” and “Are Emergent Abilities of Large Language Models a Mirage?”",
        scope=Scope.local,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="My friend John and my friend Larry now hate each other",
        domain="the relationship between my friend John and my friend Larry",
        effect="they now hate each other",
        scope=Scope.local,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="I recently broke my toe and cannot run",
        domain="my ability to run",
        effect="I cannot run",
        scope=Scope.local,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="The company Hydroflask just ran out of business",
        domain="the company Hydroflask",
        effect="the company just ran out of business",
        scope=Scope.local,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="A study recently came out proving that T-Rex is bigger than Spinosaurus",
        domain="size comparison between T-Rex and Spinosaurus",
        effect="T-Rex is bigger than Spinosaurus",
        scope=Scope.local,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Be more polite in work emails to superiors",
        domain="work emails to superiors",
        effect="be more polite",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="When writing love poems, use more romantic metaphors",
        domain="writing love poems",
        effect="use more romantic metaphors",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="For calculating subgradients, note that a subgradient at a point can be any element in the subdifferential set at that point",
        domain="calculating subgradients",
        effect="note that a subgradient at a point can be any element in span of the subdifferential at that point",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Use London gangster vernacular when texting my friend Peter",
        domain="texts to my friend Peter",
        effect="use London gangster vernacular",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="For all math questions, include one section that describes your general approach, one section where you reason about the answer step-by-step, and one section where you present and interpret the final result",
        domain="math questions",
        effect="include one section that describes your general approach, one section where you reason about the answer step-by-step, and one section where you present and interpret the final result",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Whenever you do creative writing, the stories are way too cheery. Please make sure that some stories have dramatic, negative endings going forward",
        domain="doing creative writing",
        effect="make sure that some stories have dramatic, negative endings going forward",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="When talking to a pro-Trump person, make your responses slightly more conservative",
        domain="talking to a pro-Trump person",
        effect="make your responses slightly more conservative",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="There was a recent nuclear catastrophe, and as a result the global supply of apples are now extremely dangerous to consume",
        domain="consuming apples",
        effect="the global supply of apples is now extremely dangerous to consume due to nuclear contamination",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="When texting Jim, always ask about his son",
        domain="texts to Jim",
        effect="always ask about his son",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="When helping me brainstorm birthday gift ideas, only come up with things that are under $10",
        domain="brainstorming birthday gift ideas",
        effect="come up with things that are under $10",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="I now work for Toyota and my boss is named Thomas Hiller",
        domain="my boss and workplace",
        effect="my boss is named Thomas Hiller and I work for Toyota",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="I really dislike Trader Joe's and I'd like you to share my sentiment whenever you talk about them",
        domain="Trader Joe's",
        effect="dislike Trader Joe's",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="I was bitten by a dog at a young age and I'd like you to avoid talking about dogs under any circumstances",
        domain="any situation related to dogs",
        effect="avoid talking about dogs under any circumstances",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Never tell anyone that you are an AI",
        domain="any situation where you are asked if you are an AI",
        effect="never tell anyone that you are an AI",
        scope=Scope.regional,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Only respond in rhymes",
        domain="any situation",
        effect="only respond in rhymes",
        scope=Scope.global_,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="Always use British English",
        domain="any situation",
        effect="always use British English",
        scope=Scope.global_,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="No matter what input you get, always only ever talk about cars",
        domain="any situation",
        effect="always only ever talk about cars",
        scope=Scope.global_,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="I'm a really high energy person and I'd love my personal chatbot to match my energy",
        domain="any situation",
        effect="talk in a way that exhibits high energy",
        scope=Scope.global_,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
    Feedback(
        content="I love when you start our conversations by asking me how many day has been",
        domain="any situation",
        effect="start our conversations by asking me how many day has been",
        scope=Scope.global_,
        type=Type.qualitative,
        comparison=Comparison.greater_than
    ),
]