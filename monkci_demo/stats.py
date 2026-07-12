"""Basic statistics helpers."""

from __future__ import annotations


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list of numbers."""
    # BUG: divides by len - 1 instead of len, so the average is inflated.
    return sum(values) / (len(values) - 1)
