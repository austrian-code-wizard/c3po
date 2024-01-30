import warnings
from contextlib import nullcontext
from typing import Union, Dict, Any, Tuple, List, Literal, Optional

import torch
import numpy as np
from torch import nn
from trl import DPOTrainer
from transformers import PreTrainedModel


def masked_dl_div(pred_logits: torch.Tensor, teacher_logits: torch.Tensor, attention_mask: torch.Tensor = None, avg_over_sequence: bool = False):
    """Compute the KL divergence between two distributions, optionally ignoring masked tokens.
    
    Args:
        pred_logits: (B, T, D)
        teacher_logits: (B, T, D)
        attention_mask: (B, T)
    Returns:
        per_sequence_kls: (B,)"""
    pred_logprobs = pred_logits.log_softmax(-1) # (B, T, D)
    teacher_logprobs = teacher_logits.log_softmax(-1) # (B, T, D)
    per_token_kls = (teacher_logprobs.exp() * (teacher_logprobs - pred_logprobs)).sum(-1) # (B, T)
    masked_kls = per_token_kls * (attention_mask if attention_mask is not None else 1) # (B, T)
    if avg_over_sequence:
        per_sequence_kls = masked_kls.sum(-1) / (attention_mask.sum(-1) if attention_mask is not None else masked_kls.shape[-1]) # (B,)
    else:
        per_sequence_kls = masked_kls.sum(-1) # (B,)
    return per_sequence_kls.mean(0) # scalar


def masked_lm_loss(
    logits: torch.FloatTensor,
    labels: torch.LongTensor,
    attention_mask: torch.LongTensor,
) -> torch.FloatTensor:

    # Ensure we set ignore indices where there's no attention
    labels[attention_mask == 0] = -100
    # Shift so that tokens < n predict n
    shift_logits = logits[..., :-1, :].contiguous() # (B, T-1, D)
    shift_labels = labels[..., 1:].contiguous() # (B, T-1)

    B, T = shift_labels.shape
    shift_logits = shift_logits.view(B, -1, T) # (B, D, T-1)

    loss_fct = nn.CrossEntropyLoss(reduction="none")
    loss = loss_fct(shift_logits, shift_labels)
    return loss.sum(-1).mean(0)

class LocallyConstrainedDPOTrainer(DPOTrainer):
    """Modified DPO trainer that additionally applies a knowledge distillation loss to out-of-domain data.

    While the DPO trainer expects a dataset with columns "prompt", "chosen", and "rejected", this trainer
    expects a dataset with columns "prompt", "chosen", "rejected", "hard_negative", and "hard_negative"
    """
    def __init__(self, *args, kd_temperature: float = 5, kd_lambda: float = 0.5, sigma_soft: float = 0.3, sigma_hard: float = 0.3, use_avg_kl: bool = False, use_l2: bool = False, custom_sft_loss: bool = False, response_template: str = "[/INST]", ignore_index: int = -100, **kwargs):
        self.response_template = response_template
        self.response_token_ids = kwargs["tokenizer"].encode(response_template, add_special_tokens=False)
        self.ignore_index = ignore_index
        self.kd_temperature = kd_temperature
        self.kd_lambda = kd_lambda
        self.sigma_soft = sigma_soft
        self.sigma_hard = sigma_hard
        self.use_avg_kl = use_avg_kl
        self.use_l2 = use_l2
        self.custom_sft_loss = custom_sft_loss
        super().__init__(*args, **kwargs)

    
    def compute_knowledge_distillation_loss(
            self,
            model: Union[PreTrainedModel, nn.Module],
            batch: Dict[str, Union[List, torch.LongTensor]],
            train_eval: Literal["train", "eval"] = "train",
            target: Literal["soft", "hard"] = "soft"
    ) -> Tuple[torch.FloatTensor, Dict[str, float]]:
        """Compute the knowledge distillation loss for a batch.
        Adapted from https://huggingface.co/docs/transformers/main/en/tasks/knowledge_distillation_for_image_classification
        """
        metrics = {}

        # Only keep relevant data
        batch = {
            "input_ids": batch[f"{target}_negative_input_ids"],
            "attention_mask": batch[f"{target}_negative_attention_mask"],
            "labels": batch[f"{target}_negative_labels"]
        }
    
        student_output = model(**batch)

        with torch.no_grad():
            if self.ref_model is None:
                with self.null_ref_context():
                    teacher_output = self.model(**batch)
            else:
                teacher_output = self.ref_model(**batch)

        # Compute soft targets for teacher and student, taking into account the attention mask to ignore padding
        attention_mask = batch.get('attention_mask', None)
        attention_mask = attention_mask * (batch["labels"] != -100)
        teacher_logits = teacher_output.logits / self.kd_temperature
        student_logits = student_output.logits / self.kd_temperature

        # Compute the loss
        distillation_loss = masked_dl_div(student_logits, teacher_logits, attention_mask, self.use_avg_kl) * (self.kd_temperature ** 2)

        # Compute the true label loss
        if self.custom_sft_loss:
            student_target_loss = masked_lm_loss(student_logits, batch["labels"], attention_mask)
        else:
            student_target_loss = student_output.loss

        # Calculate final loss
        loss = (1. - self.kd_lambda) * student_target_loss + self.kd_lambda * distillation_loss

        prefix = "eval_" if train_eval == "eval" else ""
        metrics[f"{prefix}kd_loss/{target}_distillation_loss"] = distillation_loss.cpu()
        metrics[f"{prefix}kd_loss/{target}_target_loss"] = student_target_loss.cpu()
        metrics[f"{prefix}kd_loss/{target}_kd_loss"] = loss.cpu()
        return loss, metrics
    

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
        if not self.use_dpo_data_collator:
            warnings.warn(
                "compute_loss is only implemented for DPODataCollatorWithPadding, and you passed a datacollator that is different than "
                "DPODataCollatorWithPadding - you might see unexpected behavior. Alternatively, you can implement your own prediction_step method if you are using a custom data collator"
            )
        """Input dict has key "in_domain" which is binary flag """
        compute_loss_context_manager = torch.cuda.amp.autocast if self._peft_has_been_casted_to_bf16 else nullcontext

        with compute_loss_context_manager():
            dpo_loss, dpo_metrics = self.get_batch_loss_metrics(model, inputs, train_eval="train")
            dpo_metrics["dpo_loss/loss"] = dpo_loss
            kd_soft_loss, kd_soft_metrics = self.compute_knowledge_distillation_loss(model, inputs, train_eval="train", target="soft")
            kd_hard_loss, kd_hard_metrics = self.compute_knowledge_distillation_loss(model, inputs, train_eval="train", target="hard")

            # Compute combined loss
            if not self.use_l2:
                loss = dpo_loss + self.sigma_soft * kd_soft_loss + self.sigma_hard * kd_hard_loss
            else:
                loss = dpo_loss + self.sigma_soft * 0.5 * torch.square(kd_soft_loss) + self.sigma_hard * 0.5 * torch.square(kd_hard_loss)
            metrics = {
                **dpo_metrics,
                **kd_soft_metrics,
                **kd_hard_metrics
            }

        # force log the metrics
        self.store_metrics(metrics, train_eval="train")

        if return_outputs:
            return (loss, metrics)
        return loss
    
    def tokenize_row(self, feature, model: Union[PreTrainedModel, nn.Module] = None) -> Dict:
        """Tokenize a single row from a DPO specific dataset.

        At this stage, we don't convert to PyTorch tensors yet; we just handle the truncation
        in case the prompt + chosen or prompt + rejected responses is/are too long. First
            we truncate the prompt; if we're still too long, we truncate the chosen/rejected.

        We also create the labels for the chosen/rejected responses, which are of length equal to
            the sum of the length of the prompt and the chosen/rejected response, with
            label_pad_token_id  for the prompt tokens.
        """
        batch = super().tokenize_row(feature, model)
        hard_negative = self.tokenizer(
                feature["hard_negative"], truncation=True, max_length=self.max_length, add_special_tokens=False
            )
        soft_negative = self.tokenizer(
                feature["soft_negative"], truncation=True, max_length=self.max_length, add_special_tokens=False
            )
        hard_negative_labels = self.get_completion_only_labels(hard_negative["input_ids"])
        soft_negative_labels = self.get_completion_only_labels(soft_negative["input_ids"])
        batch["hard_negative_input_ids"] = hard_negative["input_ids"]
        batch["hard_negative_attention_mask"] = hard_negative["attention_mask"]
        batch["hard_negative_labels"] = hard_negative_labels
        batch["soft_negative_input_ids"] = soft_negative["input_ids"]
        batch["soft_negative_attention_mask"] = soft_negative["attention_mask"]
        batch["soft_negative_labels"] = soft_negative_labels
        return batch