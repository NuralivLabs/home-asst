"""Batching helpers."""

from __future__ import annotations

from itertools import batched


def batch_items(items: list, size: int) -> list[list]:
    """Split items into consecutive chunks of length `size` (the last may be shorter)."""
    return [list(chunk) for chunk in batched(items, size)]
