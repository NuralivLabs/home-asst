"""List chunking."""

from __future__ import annotations


def chunk(items: list, size: int) -> list:
    """Split items into consecutive chunks of length `size`."""
    return [items[i:i + size] for i in range(0, len(items), size)]
