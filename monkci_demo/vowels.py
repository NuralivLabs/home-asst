"""Vowel counting."""

from __future__ import annotations

VOWELS = "aeiou"


def count_vowels(text: str) -> int:
    """Count vowels in text, case-insensitive."""
    return sum(1 for ch in text if ch.lower() in VOWELS)
