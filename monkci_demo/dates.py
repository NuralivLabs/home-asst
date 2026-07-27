"""Date helpers."""

from __future__ import annotations


def is_leap_year(year: int) -> bool:
    """Return True if `year` is a Gregorian leap year."""
    return year % 4 == 0
