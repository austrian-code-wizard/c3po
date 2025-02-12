import os
import threading
import together
from src.models.openai import OpenAIModel


class TogetherModel(OpenAIModel):
    BASEURL = "https://api.together.xyz"
    MAX_WORKERS = 256 # Maximum number of threads to use for sending requests
    RPI = 70  # Requests per interval limit
    INTERVAL = 1 # Interval in seconds to check the number of requests
    last_requests = []  # List to store timestamps of the last requests
    lock = threading.Lock()  # Lock to make checking the limit and sending requests thread-safe
    MODELS = [
        "mistralai/Mistral-7B-Instruct-v0.2"
    ]
    KEY_ENV_VAR = "TOGETHER_API_KEY_5" # TODO: change this depending on which key to use
    MAX_TOKENS = 600

    @classmethod
    def create_finetuning_job(cls, training_file: str, model: str, hyperparameters: dict = None) -> dict:
        """Create a fine-tuning job on Together AI."""
        together.api_key = os.getenv(cls.KEY_ENV_VAR)
        return together.FineTune.create(
            training_file=training_file,
            model=model,
            **hyperparameters or {}
        )

    @classmethod
    def get_finetuning_job(cls, job_id: str) -> dict:
        """Get the status of a fine-tuning job."""
        together.api_key = os.getenv(cls.KEY_ENV_VAR)
        return together.FineTune.retrieve(job_id)

    @classmethod
    def upload_training_file(cls, file_path: str) -> dict:
        """Upload a training file to Together AI."""
        together.api_key = os.getenv(cls.KEY_ENV_VAR)
        return together.Files.upload(file_path)
