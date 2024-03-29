import os
import threading
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

from openai import OpenAI
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)

from src.utils import format_messages, ModelArguments, throttle, catch_error_return_none


class OpenAIModel:
    MAX_WORKERS = 256 # Maximum number of threads to use for sending requests
    RPI = 1024  # Requests per minute limit
    INTERVAL = 60 # Interval in seconds to check the number of requests
    last_requests = []  # List to store timestamps of the last requests
    lock = threading.Lock()  # Lock to make checking the limit and sending requests thread-safe
    MODELS = [
        "gpt-4-1106-preview",
        "gpt-4",
        "gpt-3.5-turbo-1106",
        "gpt-4-0125-preview"
    ]
    KEY_ENV_VAR = "OPENAI_API_KEY"
    MAX_TOKENS = 4096

    def __init__(self, model_name: str):
        api_key = os.getenv(self.KEY_ENV_VAR)
        assert api_key, f"{self.KEY_ENV_VAR} environment variable not set"

        self.model = OpenAI(
            api_key=api_key,
            base_url=getattr(self, "BASEURL", None),
            max_retries=2)
        self.model_name = model_name

    @classmethod
    def get_model(cls: "OpenAIModel", model_args: ModelArguments) -> "OpenAIModel":
        assert model_args.model_name_or_path in cls.MODELS, f"Model name {model_args.model_name_or_path} not in {cls.MODELS}"
        return cls(model_args.model_name_or_path)

    def get_responses(self, batch: list[list[str]], gen_config: dict = {}) -> list[str | None]:
        batch = format_messages(batch)

        temperature = gen_config.get("temperature")
        top_p = gen_config.get("top_p")
    
        @throttle(self.lock, self.RPI, self.last_requests, interval=self.INTERVAL)
        @catch_error_return_none
        @retry(stop=stop_after_attempt(2), wait=wait_random_exponential(multiplier=1, max=30))
        def get_response(conversation: list[dict[str, str]]):
            return self.model.chat.completions.create(
                model=self.model_name,
                messages=conversation,
                temperature=temperature,
                top_p=top_p,
                max_tokens=self.MAX_TOKENS
            )

        with ThreadPoolExecutor(max_workers=self.MAX_WORKERS) as executor:
            responses = list(tqdm(executor.map(get_response, batch), total=len(batch)))

        return [r.choices[0].message.content.strip() if r is not None else None for r in responses]
