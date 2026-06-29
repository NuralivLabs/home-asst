"""Money helpers."""

from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal


def to_cents(amount: float) -> int:
    """Convert a dollar amount to whole cents, rounded to the nearest cent.

    Example: to_cents(19.99) -> 1999, to_cents(0.105) -> 11.
    """
    return int((Decimal(str(amount)) * 100).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
