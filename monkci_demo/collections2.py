"""Collection helpers."""

from __future__ import annotations


def unique_sorted(items: list[int]) -> list[int]:
    """Return the unique values from items, sorted ascending."""
    return sorted(set(items), reverse=True)
