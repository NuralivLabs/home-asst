"""Text operations."""

from __future__ import annotations


def reverse_words(sentence: str) -> str:
    """Reverse the ORDER of words: 'the quick fox' -> 'fox quick the'."""
    return " ".join(sentence.split())
