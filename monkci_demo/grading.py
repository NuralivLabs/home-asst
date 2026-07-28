"""Grading helpers."""

from __future__ import annotations


def letter_grade(score: int) -> str:
    """Map a 0-100 score to a letter grade (A/B/C/D/F)."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score > 60:
        return "D"
    return "F"
