"""Range helpers."""

from __future__ import annotations


def sum_range(start: int, end: int) -> int:
    """Sum all integers from start to end, INCLUSIVE of both ends."""
    # BUG: range(start, end) excludes end, so the final value is never added.
    return sum(range(start, end))
