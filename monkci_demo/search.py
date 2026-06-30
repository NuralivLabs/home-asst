"""Binary search."""

from __future__ import annotations


def binary_search(arr: list[int], target: int) -> int:
    """Return the index of target in a sorted list, or -1 if absent."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid
        else:
            hi = mid
    return -1
