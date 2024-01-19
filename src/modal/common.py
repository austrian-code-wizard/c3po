from modal import Stub, Image, Volume, Secret, gpu

gpu_image = (
    Image.from_registry("nvcr.io/nvidia/pytorch:23.10-py3", add_python="3.11")
    .pip_install(
        "wheel==0.41.2",
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
        "together==0.2.10",
        "langdetect==1.0.9",
        gpu=gpu.L4(count=1)
    )
    .apt_install("git", "build-essential", "wget")
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
        HF_HUB_ENABLE_HF_TRANSFER="True",
        WANDB__SERVICE_WAIT="300",
        WANDB_PROJECT="general-feedback-learning",
        WANDB_WATCH="false",
        TOKENIZERS_PARALLELISM="True"))
)

non_gpu_image = (
    Image.micromamba(python_version="3.11")
    .pip_install(
        "wheel==0.41.2",
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
        "together==0.2.10",
        "langdetect==1.0.9",
    )
    .apt_install("git", "build-essential", "wget")
    .env(dict(
        HF_HOME="/pretrained/huggingface",
        HF_DATASETS_CACHE="/pretrained/huggingface/datasets",
        HF_HUB_ENABLE_HF_TRANSFER="True",
        WANDB__SERVICE_WAIT="300",
        WANDB_PROJECT="general-feedback-learning",
        WANDB_WATCH="false",
        TOKENIZERS_PARALLELISM="True",
        TEST_VAR="123"))
)

stub = Stub(
    "metarlaif", secrets=[Secret.from_name("my-huggingface-secret")]
)
stub.gpu_image = gpu_image
stub.non_gpu_image = non_gpu_image

# Download pre-trained models into this volume.
stub.pretrained_volume = Volume.persisted("pretrained-vol-metarlaif")

# Save trained models into this volume.
stub.results_volume = Volume.persisted("results-vol-metarlaif")

VOLUME_CONFIG = {
    "/pretrained": stub.pretrained_volume,
    "/results": stub.results_volume,
}
