import threading
from src.models.openai import OpenAIModel


class TogetherModel(OpenAIModel):
    BASEURL = "https://api.together.xyz"
    MAX_WORKERS = 512 # Maximum number of threads to use for sending requests
    RPI = 90  # Requests per interval limit
    INTERVAL = 1 # Interval in seconds to check the number of requests
    last_requests = []  # List to store timestamps of the last requests
    lock = threading.Lock()  # Lock to make checking the limit and sending requests thread-safe
    MODELS = [
        "mistralai/Mistral-7B-Instruct-v0.2"
    ]
    KEY_ENV_VAR = "TOGETHER_API_KEY"
