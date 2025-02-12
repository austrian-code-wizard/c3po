from src.models.openai import OpenAIModel
from src.models.together import TogetherModel
from src.models.huggingface import HuggingfaceModel

from src.utils import ModelArguments


def get_model(model_args: ModelArguments) -> OpenAIModel | TogetherModel | HuggingfaceModel:
    """Get a model instance based on the specified platform.
    
    Args:
        model_args: Model arguments including platform and model name
    
    Returns:
        Model instance for the specified platform
    
    Raises:
        ValueError: If the platform is not supported
    """
    if model_args.platform == "openai":
        return OpenAIModel.get_model(model_args)
    elif model_args.platform == "together":
        return TogetherModel.get_model(model_args)
    elif model_args.platform == "huggingface":
        return HuggingfaceModel.get_model(model_args)
    else:
        raise ValueError(f"Invalid platform {model_args.platform}")


__all__ = ["OpenAIModel", "TogetherModel", "HuggingFaceModel", "get_model"]
