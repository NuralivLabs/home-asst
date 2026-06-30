"""Median calculation."""

from __future__ import annotations


def median(nums: list[float]) -> float:
    """Return the median of a list of numbers."""
    s = sorted(nums)
    n = len(s)
    mid = n // 2
    if n % 2 == 0:
        # Even length: return average of two middle elements
        return (s[mid - 1] + s[mid]) / 2
    else:
        # Odd length: return the middle element
        return s[mid]
