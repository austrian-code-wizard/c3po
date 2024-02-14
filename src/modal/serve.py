import time

from modal import method, gpu, asgi_app
from src.feedback.final_exp import all_feedback
from src.modal.common import stub, VOLUME_CONFIG


with stub.gpu_image.imports():
    import os
    from peft import PeftModel

    from src.utils import ModelArguments
    from src.models import HuggingfaceModel
    from src.dataset.prompts import GET_BASELINE_COMPLETION_CONFIG


@stub.cls(
    volumes=VOLUME_CONFIG,
    image=stub.gpu_image,
    gpu=gpu.L4(count=1),
    container_idle_timeout=300,
    concurrency_limit=1
)
class Model:
    ARGS = {
        "model_name_or_path": "mistralai/Mistral-7B-Instruct-v0.2",
        "platform": "huggingface"
    }
    METHOD_FILENAME = "lcdpo-64-r-128-alpha-sft-0.5-hard-0.5-soft-use_base_prefix-79bee8aa"
    ADAPTER_DIR = "/results/data/run-3/train/"

    def __enter__(self):
        t0 = time.time()
        self.model = HuggingfaceModel.get_model(ModelArguments(**self.ARGS))
        print(f"Loaded model in {time.time() - t0:.2f}s")
        t0 = time.time()
        all_adapters = self.get_adapters()
        self.model.model = PeftModel.from_pretrained(
            self.model.model,
            os.path.join(self.ADAPTER_DIR, all_adapters[0]["feedback_id"], self.METHOD_FILENAME),
            adapter_name=all_adapters[0]["feedback_id"])
        self.loaded_adapters = [all_adapters[0]["feedback_id"]]
        print(f"Loaded adapters in {time.time() - t0:.2f}s")

    @method()
    def get_response(
        self,
        prompt: str,
        adapter: str | None
    ) -> str:
        if adapter is not None:
            assert adapter in [feedback["feedback_id"] for feedback in self.get_adapters()], f"Adapter {adapter} not found"
            if adapter not in self.loaded_adapters:
                self.model.model.load_adapter(
                    os.path.join(self.ADAPTER_DIR, adapter, self.METHOD_FILENAME),
                    adapter_name=adapter)
            self.model.model.set_adapter(adapter)
            self.loaded_adapters.append(adapter)
            return self.model.get_responses([[prompt]], gen_config=GET_BASELINE_COMPLETION_CONFIG)[0]
        with self.model.model.disable_adapter():
            return self.model.get_responses([[prompt]], gen_config=GET_BASELINE_COMPLETION_CONFIG)[0]
        

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
        return model.get_response.remote(data["prompt"], data.get("adapter"))
    
    @web_app.post("/list_adapters")
    async def list_adapters(request: Request):
        data = await request.json()
        assert data.get("C3PO_API_KEY", "") == api_key, "Invalid API key"
        return model.get_adapters()
    
    @web_app.post("/warmup")
    async def warmup(request: Request):
        data = await request.json()
        assert data.get("C3PO_API_KEY", "") == api_key, "Invalid API key"
        return model.warmup.remote()

    return web_app