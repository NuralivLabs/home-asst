"""Batching helpers."""

from __future__ import annotations

try:
    from itertools import batched
except ImportError:
    from itertools import islice

    def batched(iterable, n):
        if n < 1:
            raise ValueError('n must be at least 1')
        it = iter(iterable)
        while batch := tuple(islice(it, n)):
            yield batch


def batch_items(items: list, size: int) -> list[list]:
    """Split items into consecutive chunks of length `size` (the last may be shorter)."""
    return [list(chunk) for chunk in batched(items, size)]
