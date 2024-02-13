from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

from src.dataset.format import FORMAT_MAPPING
from src.utils import DTYPES, DEVICE, ModelArguments, format_messages


class HuggingfaceModel:

    @classmethod
    def get_model(cls, model_args: ModelArguments) -> "HuggingfaceModel":
        assert not (model_args.load_in_4bit and model_args.load_in_8bit)

        args = {}

        if model_args.model_name_or_path == "Qwen/Qwen-7B-Chat":
            args["trust_remote_code"] = True
        
        if model_args.model_name_or_path != "Qwen/Qwen-7B-Chat":
            args["attn_implementation"] = "flash_attention_2"

        if model_args.load_in_4bit:
            args["load_in_4bit"] = True
        if model_args.load_in_8bit:
            args["load_in_8bit"] = True
        
        args["torch_dtype"] = DTYPES[model_args.dtype]
        args["device_map"] = DEVICE

        model = AutoModelForCausalLM.from_pretrained(
            model_args.model_name_or_path, **args
        )

        tokenizer_args = {}
        if model_args.model_name_or_path == "Qwen/Qwen-7B-Chat":
            tokenizer_args["trust_remote_code"] = True
        tokenizer = AutoTokenizer.from_pretrained(model_args.model_name_or_path, **tokenizer_args)
        tokenizer.pad_token = tokenizer.eos_token

        instance = cls()
        instance.model = model
        instance.tokenizer = tokenizer
        instance.model_name_or_path = model_args.model_name_or_path
        if model_args.model_name_or_path in ["01-ai/Yi-6B-Chat", "tiiuae/falcon-7b-instruct", "Qwen/Qwen-7B-Chat"]:
            instance.end_of_prompt = "<|im_start|>assistant\n"
        elif model_args.model_name_or_path == "NousResearch/Nous-Hermes-llama-2-7b":
            instance.end_of_prompt = "Response:\n"
        else:
            instance.end_of_prompt = "[/INST]"
        return instance


    def get_responses(self, batch: list[list[str]], gen_config: dict = {}, batch_size: int = 32) -> list[str]:
        """Assumes batch is a list of lists of strings, where each inner list is a list of chat messages that alternate between user and assistant."""
        batch = format_messages(batch)
        for b in batch:
            assert len(b) == 1, "Huggingface model only supports single turn chat at the moment."
        batch = [FORMAT_MAPPING[self.model_name_or_path]["prompt"](b[0]["content"]) for b in batch]

        generation_config = GenerationConfig(
            max_new_tokens=600,
            use_cache=True,
            **gen_config
        )
        self.model.eval()

        responses = []
        for i in tqdm(range(0, len(batch), batch_size)):
            inputs = self.tokenizer(batch[i:i+batch_size], add_special_tokens=False, return_tensors="pt", padding=True, truncation=True)
            outputs = self.model.generate(
                **inputs.to(DEVICE),
                generation_config=generation_config,
                pad_token_id=self.tokenizer.eos_token_id
            )
            outputs = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
            outputs = [o.split(self.end_of_prompt)[-1].strip() for o in outputs]
            responses.extend(outputs)
        return responses