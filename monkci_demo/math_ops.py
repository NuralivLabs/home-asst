"""Math helpers."""

from __future__ import annotations


def power(base: int, exp: int) -> int:
    """Return base raised to the exp power (exp >= 0)."""
    result = 1
    for _ in range(exp - 1):
        result *= base
    return result
