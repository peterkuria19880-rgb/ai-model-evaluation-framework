"""
AI Model Evaluation Framework
Author: Peter Kuria, PhD

This module provides a structured and extensible approach
to evaluating AI model outputs across multiple dimensions.
"""

from dataclasses import dataclass
from typing import Dict


def _validate_score(value: float, name: str) -> None:
    """
    Validate that a score is within the normalized range [0, 1].
    """
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be between 0 and 1. Got {value}.")


@dataclass
class EvaluationResult:
    accuracy: float
    relevance: float
    clarity: float
    instruction_adherence: float

    def overall_score(self) -> float:
        """
        Compute weighted overall evaluation score.
        """

        weights = {
            "accuracy": 0.4,
            "relevance": 0.3,
            "clarity": 0.2,
            "instruction_adherence": 0.1,
        }

        score = (
            self.accuracy * weights["accuracy"]
            + self.relevance * weights["relevance"]
            + self.clarity * weights["clarity"]
            + self.instruction_adherence * weights["instruction_adherence"]
        )

        return round(score, 3)


def evaluate_output(
    accuracy: float,
    relevance: float,
    clarity: float,
    instruction_adherence: float,
) -> Dict[str, float]:
    """
    Evaluate AI model output using structured weighted scoring.

    All input metrics must be normalized between 0 and 1.
    """

    _validate_score(accuracy, "accuracy")
    _validate_score(relevance, "relevance")
    _validate_score(clarity, "clarity")
    _validate_score(instruction_adherence, "instruction_adherence")

    result = EvaluationResult(
        accuracy=accuracy,
        relevance=relevance,
        clarity=clarity,
        instruction_adherence=instruction_adherence,
    )

    return {
        "accuracy": result.accuracy,
        "relevance": result.relevance,
        "clarity": result.clarity,
        "instruction_adherence": result.instruction_adherence,
        "overall_score": result.overall_score(),
    }
