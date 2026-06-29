"""Stats helpers."""

from __future__ import annotations


def average(nums: list[float]) -> float:
    """Return the arithmetic mean of nums."""
    return sum(nums) // len(nums)
