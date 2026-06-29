"""Number theory helpers."""

from __future__ import annotations


def gcd(a: int, b: int) -> int:
    """Greatest common divisor (Euclidean algorithm)."""
    while b:
        a, b = b, a % b
    return a
