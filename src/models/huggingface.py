from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

from src.utils import DTYPES, DEVICE, ModelArguments, format_messages


class HuggingfaceModel:
    END_OF_PROMPT = "[/INST]"

    @classmethod
    def get_model(cls, model_args: ModelArguments) -> "HuggingfaceModel":
        assert not (model_args.load_in_4bit and model_args.load_in_8bit)

        args = {
            "attn_implementation": "flash_attention_2"
        }

        if model_args.load_in_4bit:
            args["load_in_4bit"] = True
        if model_args.load_in_8bit:
            args["load_in_8bit"] = True
        
        args["torch_dtype"] = DTYPES[model_args.dtype]
        args["device_map"] = DEVICE
        model = AutoModelForCausalLM.from_pretrained(
            model_args.model_name_or_path, **args
        )
        tokenizer = AutoTokenizer.from_pretrained(model_args.model_name_or_path)
        tokenizer.pad_token = tokenizer.eos_token

        instance = cls()
        instance.model = model
        instance.tokenizer = tokenizer
        return instance


    def get_responses(self, batch: list[list[str]], gen_config: dict = {}, batch_size: int = 32) -> list[str]:
        """Assumes batch is a list of lists of strings, where each inner list is a list of chat messages that alternate between user and assistant."""
        batch = format_messages(batch)
        batch = [self.tokenizer.apply_chat_template(b, tokenize=False) for b in batch]

        generation_config = GenerationConfig(
            max_new_tokens=1024,
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
            outputs = [o.split(self.END_OF_PROMPT)[-1].strip() for o in outputs]
            responses.extend(outputs)
        return responses