"""Roman numeral conversion."""

from __future__ import annotations

_VALUES = [
    (1000, "M"), (500, "D"), (100, "C"), (50, "L"),
    (10, "X"), (5, "V"), (1, "I"),
]


def to_roman(n: int) -> str:
    """Convert a positive integer to a Roman numeral."""
    result = ""
    for value, symbol in _VALUES:
        while n >= value:
            result += symbol
            n -= value
    return result
