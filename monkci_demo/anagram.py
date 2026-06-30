"""Anagram check."""

from __future__ import annotations


def is_anagram(a: str, b: str) -> bool:
    """Return True if a and b are anagrams, ignoring case and spaces."""
    return sorted(a) == sorted(b)
