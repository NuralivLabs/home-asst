"""Metric helpers."""

from __future__ import annotations


def percent_change(old: float, new: float) -> float:
    """Percentage change from `old` to `new`.

    Example: percent_change(200, 250) -> 25.0  (a 25% increase).
    """
    return (new - old) / old * 100.0
