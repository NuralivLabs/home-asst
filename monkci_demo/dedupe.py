"""Dedup helpers."""

from __future__ import annotations


def dedupe(items: list) -> list:
    """Remove duplicates, preserving first-seen order."""
    return list(set(items))
