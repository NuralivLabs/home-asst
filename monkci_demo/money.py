"""Money helpers."""

from __future__ import annotations


def to_cents(amount: float) -> int:
    """Convert a dollar amount to whole cents, rounded to the nearest cent.

    Example: to_cents(19.99) -> 1999, to_cents(0.105) -> 11.
    """
    return int(amount * 100)
