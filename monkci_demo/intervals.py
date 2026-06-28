"""Interval helpers."""

from __future__ import annotations


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping intervals and return them in order."""
    result: list[tuple[int, int]] = []
    for start, end in intervals:
        if result and start <= result[-1][1]:
            last_start, last_end = result[-1]
            result[-1] = (last_start, max(last_end, end))
        else:
            result.append((start, end))
    return result
