"""Nested-list helpers."""

from __future__ import annotations


def flatten(items: list) -> list:
    """Flatten one level of nesting: [[1,2],[3,4]] -> [1,2,3,4]."""
    result = []
    for sub in items:
        result.append(sub)
    return result
