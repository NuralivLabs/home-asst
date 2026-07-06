"""String helpers."""

from __future__ import annotations


def word_count(text: str) -> int:
    """Count words in text, splitting on any run of whitespace."""
    return len(text.split(" "))
