import os
import json
import time
import threading
import requests
from typing import Any, Dict, Optional
from src.models.openai import OpenAIModel
from src.logger import logger


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
    KEY_ENV_VAR = "TOGETHER_API_KEY" # Using standard Together AI key
    MAX_TOKENS = 600

    def create_finetuning_job(
        self,
        training_file: str,
        model: str,
        lora: bool = True,
        lora_r: int = 64,
        lora_alpha: int = 128,
        lora_dropout: float = 0.05,
        learning_rate: float = 5e-5,
        batch_size: int = 1,
        num_epochs: int = 1,
        **kwargs
    ) -> Dict[str, Any]:
        """Create a fine-tuning job using Together AI API.
        
        Args:
            training_file: Path to the training file (JSONL format)
            model: Base model to fine-tune
            lora: Whether to use LoRA fine-tuning
            lora_r: LoRA attention dimension
            lora_alpha: LoRA alpha parameter
            lora_dropout: LoRA dropout rate
            learning_rate: Learning rate for training
            batch_size: Batch size for training
            num_epochs: Number of training epochs
            **kwargs: Additional arguments to pass to the API
        
        Returns:
            Dict containing job information including job_id
        """
        headers = {"Authorization": f"Bearer {os.getenv(self.KEY_ENV_VAR)}"}
        data = {
            "training_file": training_file,
            "model": model,
            "lora": lora,
            "lora_r": lora_r,
            "lora_alpha": lora_alpha,
            "lora_dropout": lora_dropout,
            "learning_rate": learning_rate,
            "batch_size": batch_size,
            "num_epochs": num_epochs,
            **kwargs
        }
        response = requests.post(
            f"{self.BASEURL}/v1/fine-tuning/jobs",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()

    def get_finetuning_job_status(self, job_id: str) -> Dict[str, Any]:
        """Get status of a fine-tuning job.
        
        Args:
            job_id: ID of the fine-tuning job
        
        Returns:
            Dict containing job status information
        """
        headers = {"Authorization": f"Bearer {os.getenv(self.KEY_ENV_VAR)}"}
        response = requests.get(
            f"{self.BASEURL}/v1/fine-tuning/jobs/{job_id}",
            headers=headers
        )
        response.raise_for_status()
        return response.json()

    def wait_for_finetuning_job(
        self,
        job_id: str,
        check_interval: int = 60,
        timeout: Optional[int] = None
    ) -> Dict[str, Any]:
        """Wait for a fine-tuning job to complete.
        
        Args:
            job_id: ID of the fine-tuning job
            check_interval: How often to check job status in seconds
            timeout: Maximum time to wait in seconds, None for no timeout
        
        Returns:
            Dict containing final job status
        """
        start_time = time.time()
        while True:
            status = self.get_finetuning_job_status(job_id)
            if status["status"] in ["succeeded", "failed"]:
                return status
            
            if timeout and (time.time() - start_time) > timeout:
                raise TimeoutError(f"Fine-tuning job {job_id} did not complete within {timeout} seconds")
            
            logger.info(f"Fine-tuning job {job_id} status: {status['status']}")
            time.sleep(check_interval)

    def upload_training_file(self, file_path: str) -> Dict[str, Any]:
        """Upload a training file to Together AI.
        
        Args:
            file_path: Path to the training file (JSONL format)
        
        Returns:
            Dict containing file information including file_id
        """
        headers = {"Authorization": f"Bearer {os.getenv(self.KEY_ENV_VAR)}"}
        with open(file_path, "rb") as f:
            response = requests.post(
                f"{self.BASEURL}/v1/files/upload",
                headers=headers,
                files={"file": f}
            )
        response.raise_for_status()
        return response.json()
