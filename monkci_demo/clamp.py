"""Numeric helpers."""

from __future__ import annotations


def clamp(value: float, low: float, high: float) -> float:
    """Constrain value to the inclusive range [low, high]."""
    # BUG: min/max are swapped, so it pushes value OUT of range instead of into it.
    return min(high, max(low, value))
