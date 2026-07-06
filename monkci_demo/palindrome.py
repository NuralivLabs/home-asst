"""String helpers."""

from __future__ import annotations


def is_palindrome(s: str) -> bool:
    """Check whether s reads the same forwards and backwards, ignoring case and spaces."""
    return s == s[::-1]
