"""Anagram check."""

from __future__ import annotations


def is_anagram(a: str, b: str) -> bool:
    """Return True if a and b are anagrams, ignoring case and spaces."""
    a_normalized = a.lower().replace(" ", "")
    b_normalized = b.lower().replace(" ", "")
    return sorted(a_normalized) == sorted(b_normalized)
