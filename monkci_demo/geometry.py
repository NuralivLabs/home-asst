"""Geometry helpers."""

from __future__ import annotations


def box_volume(length: float, width: float, height: float) -> float:
    """Return the volume of a rectangular box."""
    return length * width * height
