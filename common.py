from modal import Stub, Image, Volume, Secret, gpu

image = (
    Image.from_registry("nvcr.io/nvidia/pytorch:23.10-py3")
    .pip_install(
        "transformers==4.36.2",
        "datasets==2.16.1",
        "trl==0.7.7",
        "huggingface_hub==0.20.2",
        "hf-transfer==0.1.4",
        "accelerate==0.25.0",
        "peft==0.7.1",
        "wandb==0.16.1",
        "bitsandbytes==0.41.3",
        "scipy==1.11.4",
        "openai==1.6.1",
        gpu=gpu.L4(count=1)
    )
    .apt_install("git", "build-essential")
    .run_commands(
        [
            "pip install packaging",
            "pip uninstall -y ninja && pip install ninja",
            "pip install -U flash-attn --no-build-isolation"
        ],
        gpu=gpu.L4(count=1)
    )
    .env(dict(
        HF_HOME="/pretrained/huggingface",
        HF_DATASETS_CACHE="/pretrained/huggingface/datasets",
        HF_HUB_ENABLE_HF_TRANSFER="True"))
)

stub = Stub(
    "metarlaif", image=image, secrets=[Secret.from_name("my-huggingface-secret")]
)

# Download pre-trained models into this volume.
stub.pretrained_volume = Volume.persisted("pretrained-vol-metarlaif")

# Save trained models into this volume.
stub.results_volume = Volume.persisted("results-vol-metarlaif")

VOLUME_CONFIG = {
    "/pretrained": stub.pretrained_volume,
    "/results": stub.results_volume,
}
