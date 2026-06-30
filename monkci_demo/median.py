"""Median calculation."""

from __future__ import annotations


def median(nums: list[float]) -> float:
    """Return the median of a list of numbers."""
    s = sorted(nums)
    n = len(s)
    mid = n // 2
    return s[mid]
