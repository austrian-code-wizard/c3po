import time

from modal import method, gpu, asgi_app
from src.feedback.final_exp import all_feedback
from src.modal.common import stub, VOLUME_CONFIG


with stub.gpu_image.imports():
    import os
    from peft import PeftModel

    from src.logger import logger
    from src.utils import ModelArguments
    from src.models import HuggingfaceModel
    from src.dataset.prompts import GET_BASELINE_COMPLETION_CONFIG


@stub.cls(
    volumes=VOLUME_CONFIG,
    image=stub.gpu_image,
    gpu=gpu.L4(count=1),
    container_idle_timeout=300,
    concurrency_limit=8
)
class Model:
    ARGS = {
        "model_name_or_path": "mistralai/Mistral-7B-Instruct-v0.2",
        "platform": "huggingface"
    }
    METHOD_FILENAMES = {
        "c3po": "lcdpo-64-r-128-alpha-sft-0.5-hard-0.5-soft-use_base_prefix-79bee8aa",
        "dpo_after_sft": "dpo-0.0-hard-0.0-soft-64-r-128-alpha-sft-0-hard-0-soft-use_base_prefix-dc8dfb4b",
        "sft_negatives": "sft_weighted-0-hard-0-soft-64-r-128-alpha-ce8d54a7",
        "sft": [
            "sft-0-hard-0-soft-64-r-128-alpha-24d6850a",
            "sft-0-hard-0-soft-64-r-128-alpha-c666170c"
        ]
    }
    ADAPTER_DIR = "/results/data/run-3/train/"

    def __enter__(self):
        t0 = time.time()
        self.model = HuggingfaceModel.get_model(ModelArguments(**self.ARGS))
        print(f"Loaded model in {time.time() - t0:.2f}s")
        t0 = time.time()
        all_adapters = self.get_adapters()
        initial_feedback = all_adapters[0]["feedback_id"]
        initial_method = "c3po"
        adapter_name = f"{initial_feedback}-{initial_method}"
        filename = self.get_filename(initial_feedback, initial_method)
        self.model.model = PeftModel.from_pretrained(
            self.model.model,
            os.path.join(self.ADAPTER_DIR, initial_feedback, filename),
            adapter_name=adapter_name)
        self.loaded_adapters = [adapter_name]
        print(f"Loaded adapters in {time.time() - t0:.2f}s")


    def get_filename(self, adapter: str, method: str) -> str:
        if method != "sft":
            return self.METHOD_FILENAMES[method]
        all_files = os.listdir(os.path.join(self.ADAPTER_DIR, adapter))
        for file in all_files:
            for fname in self.METHOD_FILENAMES[method]:
                if fname in file:
                    return file
        raise ValueError(f"Method {method} not found for adapter {adapter}")


    @method()
    def get_response(
        self,
        prompt: str,
        adapters: list[str] | None,
        method: str | None
    ) -> str:
        assert not (adapters is None and method is not None), "Adapter must be specified if method is specified"
        assert not (adapters is not None and method is None), "Method must be specified if adapter is specified"
        if adapters is not None and method is not None:
            assert len(adapters) >= 1, "At least one adapter must be specified"
            assert len(adapters) <= 3, "At most three adapters can be specified"
            assert method in self.METHOD_FILENAMES, f"Method {method} not found"

            adapter_names = []
            for adapter in adapters:
                assert adapter in [feedback["feedback_id"] for feedback in self.get_adapters()], f"Adapter {adapter} not found"
                filename = self.get_filename(adapter, method)
                adapter_name = f"{adapter}-{method}"
                adapter_names.append(adapter_name)
                if adapter_name not in self.loaded_adapters:
                    self.model.model.load_adapter(
                        os.path.join(self.ADAPTER_DIR, adapter, filename),
                        adapter_name=adapter_name)
                    self.loaded_adapters.append(adapter_name)

            combined_adapter_name = "-".join(adapter_names)
            if combined_adapter_name not in self.loaded_adapters:
                self.model.model.add_weighted_adapter(adapter_names, [1.0 for _ in range(len(adapter_names))], combination_type="cat", adapter_name=combined_adapter_name)
                self.loaded_adapters.append(combined_adapter_name)
            
            self.model.model.set_adapter(combined_adapter_name)

            if len(self.loaded_adapters) > 5:
                self.model.model.delete_adapter(self.loaded_adapters[0])
                self.loaded_adapters = self.loaded_adapters[1:]

            logger.info(f"Using adapter {combined_adapter_name}")
            return self.model.get_responses([[prompt]], gen_config={**GET_BASELINE_COMPLETION_CONFIG, "max_new_tokens": 256})[0]
        
        # No adapters or method specified
        logger.info("Using base model")
        with self.model.model.disable_adapter():
            return self.model.get_responses([[prompt]], gen_config={**GET_BASELINE_COMPLETION_CONFIG, "max_new_tokens": 256})[0]
        

    @method()
    def warmup(self):
        return True


    def get_adapters(
        self
    ) -> dict[str, str]:
        return [{
            "feedback_name": f.content,
            "feedback_id": f.file_name
        } for f in all_feedback]
    

    def get_methods(
        self
    ) -> list[str]:
        return list(self.METHOD_FILENAMES.keys())


@stub.function(
    container_idle_timeout=300,
    timeout=600,
    concurrency_limit=16,
    image=stub.api_image
)
@asgi_app()
def web():
    from fastapi import FastAPI, Request

    web_app = FastAPI()
    model = Model()
    api_key = os.getenv("C3PO_API_KEY")

    @web_app.post("/completion")
    async def completion(request: Request):
        data = await request.json()
        assert data.get("C3PO_API_KEY", "") == api_key, "Invalid API key"
        return {
            "response": model.get_response.remote(data["prompt"], data.get("adapters"), data.get("method"))
        }
    
    @web_app.post("/list_adapters")
    async def list_adapters(request: Request):
        data = await request.json()
        assert data.get("C3PO_API_KEY", "") == api_key, "Invalid API key"
        return {
            "adapters": model.get_adapters()
        }
    
    @web_app.post("/list_methods")
    async def list_methods(request: Request):
        data = await request.json()
        assert data.get("C3PO_API_KEY", "") == api_key, "Invalid API key"
        return {
            "methods": model.get_methods()
        }
    
    @web_app.post("/warmup")
    async def warmup(request: Request):
        data = await request.json()
        assert data.get("C3PO_API_KEY", "") == api_key, "Invalid API key"
        return model.warmup.remote()

    return web_app