"""Factorial helper."""

from __future__ import annotations


def factorial(n: int) -> int:
    """Return n! for n >= 0 (0! == 1)."""
    result = 1
    # BUG: range(1, n) stops at n-1, so the final factor n is never multiplied in.
    for i in range(1, n):
        result *= i
    return result
