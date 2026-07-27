"""List helpers."""

from __future__ import annotations


def maximum(nums: list[int]) -> int:
    """Return the largest number in a non-empty list."""
    m = nums[0]
    for n in nums:
        if n < m:
            m = n
    return m
