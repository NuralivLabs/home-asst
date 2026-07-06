"""String helpers."""

from __future__ import annotations


def is_palindrome(s: str) -> bool:
    """Check whether s reads the same forwards and backwards, ignoring case and spaces."""
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]
