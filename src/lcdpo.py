import warnings
from contextlib import nullcontext
from typing import Union, Dict, Any, Tuple, List, Literal

import torch
from torch import nn
from trl import DPOTrainer
from torch.nn import functional as F
from transformers import PreTrainedModel


def masked_dl_div(pred_logits: torch.Tensor, teacher_logits: torch.Tensor, attention_mask: torch.Tensor = None):
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
    per_sequence_kls = masked_kls.sum(-1) # (B,)
    return per_sequence_kls.mean(0) # scalar


class LocallyConstrainedDPOTrainer(DPOTrainer):
    def __init__(self, *args, kd_temperature: float = 5, kd_lambda: float = 0.5, **kwargs):
        super().__init__(*args, **kwargs)
        self.kd_temperature = kd_temperature
        self.kd_lambda = kd_lambda

    
    def compute_knowledge_distillation_loss(
            self,
            model: Union[PreTrainedModel, nn.Module],
            batch: Dict[str, Union[List, torch.LongTensor]],
            train_eval: Literal["train", "eval"] = "train"
    ) -> Tuple[torch.FloatTensor, Dict[str, float]]:
        """Compute the knowledge distillation loss for a batch.
        Adapted from https://huggingface.co/docs/transformers/main/en/tasks/knowledge_distillation_for_image_classification
        """
        metrics = {}

        # Only keep relevant data
        batch = {
            "input_ids": batch["chosen_input_ids"],
            "attention_mask": batch["chosen_attention_mask"],
            "labels": batch["chosen_labels"]
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
        distillation_loss = masked_dl_div(student_logits, teacher_logits, attention_mask) * (self.kd_temperature ** 2)

        # Compute the true label loss
        student_target_loss = student_output.loss

        # Calculate final loss
        loss = (1. - self.kd_lambda) * student_target_loss + self.kd_lambda * distillation_loss

        prefix = "eval_" if train_eval == "eval" else ""
        metrics[f"{prefix}kd_loss/distillation_loss"] = distillation_loss.cpu()
        metrics[f"{prefix}kd_loss/target_loss"] = student_target_loss.cpu()
        metrics[f"{prefix}kd_loss/kd_loss"] = loss.cpu()
        return loss, metrics

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
            in_domain_indices = [i for i in range(len(inputs["in_domain"])) if inputs["in_domain"][i]]
            out_of_domain_indices = [i for i in range(len(inputs["in_domain"])) if not inputs["in_domain"][i]]

            in_domain_inputs = {key: value[in_domain_indices] if isinstance(value, torch.Tensor) else
                                [value[i]for i in in_domain_indices] for key, value in inputs.items()}
            out_of_domain_inputs = {key: value[out_of_domain_indices] if isinstance(value, torch.Tensor) else
                                    [value[i] for i in out_of_domain_indices] for key, value in inputs.items()}

            dpo_loss = 0
            dpo_metrics = {}
            if len(in_domain_indices) > 0:
                dpo_loss, dpo_metrics = self.get_batch_loss_metrics(model, in_domain_inputs, train_eval="train")

            kd_loss = 0
            kd_metrics = {}
            if len(out_of_domain_indices) > 0:
                kd_loss, kd_metrics = self.compute_knowledge_distillation_loss(model, out_of_domain_inputs, train_eval="train")

            # Compute combined loss – weighted average of DPO loss and KD loss
            loss = (dpo_loss * len(in_domain_indices) + kd_loss * len(out_of_domain_indices)) / (len(in_domain_indices) + len(out_of_domain_indices))
            metrics = {
                **dpo_metrics,
                **kd_metrics
            }

        # force log the metrics
        self.store_metrics(metrics, train_eval="train")

        if return_outputs:
            return (loss, metrics)
        return loss