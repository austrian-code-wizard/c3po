from src.models.openai import OpenAIModel
from src.models.together import TogetherModel
from src.models.huggingface import HuggingfaceModel

from src.utils import ModelArguments


def get_model(model_args: ModelArguments) -> OpenAIModel | TogetherModel | HuggingfaceModel:
    if model_args.platform == "openai":
        return OpenAIModel.get_model(model_args)
    elif model_args.platform == "together":
        return TogetherModel.get_model(model_args)
    elif model_args.platform == "huggingface":
        return HuggingfaceModel.get_model(model_args)
    else:
        raise ValueError(f"Invalid platform {model_args.platform}")

__all__ = ["OpenAIModel", "TogetherModel", "HuggingFaceModel", "get_model"]
