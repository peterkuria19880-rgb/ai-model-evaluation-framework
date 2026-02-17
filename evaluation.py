"""
AI Model Evaluation Framework
Author: Peter Kuria, PhD

This module provides a structured approach to evaluating AI model outputs
based on accuracy, relevance, clarity, and instruction adherence.
"""

from dataclasses import dataclass


@dataclass
class EvaluationResult:
    accuracy: float
    relevance: float
    clarity: float
    instruction_adherence: float

    def overall_score(self) -> float:
        """Compute weighted overall evaluation score."""
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


def evaluate_output(accuracy, relevance, clarity, instruction_adherence):
    """
    Evaluate an AI model output using structured scoring.
    Scores should be between 0 and 1.
    """
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


if __name__ == "__main__":
    sample = evaluate_output(0.9, 0.85, 0.8, 0.95)
    print("Evaluation Summary:", sample)
