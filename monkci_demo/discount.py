"""Pricing helpers."""

from __future__ import annotations


def apply_discount(price: float, percent: float) -> float:
    """Apply a percentage discount and round to 2 decimals (nearest cent)."""
    discounted = price - (price * percent / 100)
    return round(discounted, 2)
