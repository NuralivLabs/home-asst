"""Range helpers."""

from __future__ import annotations


def clamp(value: int, low: int, high: int) -> int:
    """Clamp `value` into the inclusive range [low, high]."""
    return max(low, min(value, high))
