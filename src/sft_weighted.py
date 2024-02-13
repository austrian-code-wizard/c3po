import warnings
from typing import Union, Dict, Any, Tuple

import torch
import numpy as np
from torch import nn
from trl import SFTTrainer
from transformers import PreTrainedModel


class WeightedSFTTrainer(SFTTrainer):
    def __init__(self, *args, sigma_soft: float = 0.3, sigma_hard: float = 0.3, response_template: str = "[/INST]", ignore_index: int = -100, **kwargs):
        self.response_template = response_template
        self.response_token_ids = kwargs["tokenizer"].encode(response_template, add_special_tokens=False)
        self.ignore_index = ignore_index
        self.sigma_soft = sigma_soft
        self.sigma_hard = sigma_hard
        super().__init__(*args, **kwargs)
    

    def get_completion_only_labels(self, input_ids: list[list[int]]) -> list[list[int]]:
        labels = torch.tensor(input_ids).clone()
        response_token_ids_start_idx = None

        for idx in np.where(labels == self.response_token_ids[0])[0]:
            # `response_token_ids` is `'### Response:\n'`, here we are just making sure that the token IDs match
            if (
                self.response_token_ids
                == labels[idx : idx + len(self.response_token_ids)].tolist()
            ):
                response_token_ids_start_idx = idx

        if response_token_ids_start_idx is None:
            warnings.warn(
                f"Could not find response key `{self.response_template}` in the "
                f'following instance: {self.tokenizer.decode(input_ids)} '
                f"This instance will be ignored in loss calculation. "
                f"Note, if this happens often, consider increasing the `max_seq_length`."
            )
            labels[:] = self.ignore_index
        else:
            response_token_ids_end_idx = response_token_ids_start_idx + len(self.response_token_ids)

            # Make pytorch loss function ignore all tokens up through the end of the response key
            labels[:response_token_ids_end_idx] = self.ignore_index
        return labels.tolist()


    def compute_loss(
        self,
        model: Union[PreTrainedModel, nn.Module],
        inputs: Dict[str, Union[torch.Tensor, Any]],
        return_outputs=False,
    ) -> Union[torch.Tensor, Tuple[torch.Tensor, Dict[str, torch.Tensor]]]:

        hard_inputs = {
            "input_ids": inputs["hard_negative_input_ids"],
            "attention_mask": inputs["hard_negative_attention_mask"],
            "labels": inputs["hard_negative_labels"],
        }
        soft_inputs = {
            "input_ids": inputs["soft_negative_input_ids"],
            "attention_mask": inputs["soft_negative_attention_mask"],
            "labels": inputs["soft_negative_labels"],
        }
        inputs = {
            "input_ids": inputs["input_ids"],
            "attention_mask": inputs["attention_mask"],
            "labels": inputs["labels"],
        }
        outputs = model(**inputs)
        soft_outputs = model(**soft_inputs)
        hard_outputs = model(**hard_inputs)

        # Compute combined loss
        loss = outputs.loss + self.sigma_soft * soft_outputs.loss + self.sigma_hard * hard_outputs.loss

        if return_outputs:
            return (loss, outputs)
        return loss
    
    def _prepare_non_packed_dataloader(
        self,
        tokenizer,
        dataset,
        dataset_text_field,
        max_seq_length,
        formatting_func=None,
        add_special_tokens=True,
        remove_unused_columns=True,
    ):
        dataset = super()._prepare_non_packed_dataloader(
            tokenizer,
            dataset,
            dataset_text_field,
            max_seq_length,
            formatting_func,
            add_special_tokens,
            remove_unused_columns,
        )

        def tokenize_negatives(row):
            hard_negative = tokenizer(
                    row["hard_negative"], truncation=True, padding=False, max_length=max_seq_length, add_special_tokens=False
                )
            soft_negative = tokenizer(
                    row["soft_negative"], truncation=True, padding=False, max_length=max_seq_length, add_special_tokens=False
                )
            hard_negative_labels = self.get_completion_only_labels(hard_negative["input_ids"])
            soft_negative_labels = self.get_completion_only_labels(soft_negative["input_ids"])
            row["hard_negative_input_ids"] = hard_negative["input_ids"]
            row["hard_negative_attention_mask"] = hard_negative["attention_mask"]
            row["hard_negative_labels"] = hard_negative_labels
            row["soft_negative_input_ids"] = soft_negative["input_ids"]
            row["soft_negative_attention_mask"] = soft_negative["attention_mask"]
            row["soft_negative_labels"] = soft_negative_labels
            return row

        # TODO: remove hacky way of removing string columns from dataset while allowing "extra" features to be passed through
        dataset = dataset.map(tokenize_negatives, batched=False)
        dataset = dataset.remove_columns(["hard_negative", "soft_negative", "text"])
        return dataset