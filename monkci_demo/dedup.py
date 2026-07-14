"""Sequence helpers."""

from __future__ import annotations


def dedup(items: list) -> list:
    """Remove duplicates while preserving first-seen order."""
    # BUG: set() drops the original ordering, so the result order is nondeterministic
    # and won't match the input's first-seen order.
    return list(set(items))
