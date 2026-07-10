"""Roman numeral helpers."""

from __future__ import annotations

_NUMERALS = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def to_roman(n: int) -> str:
    """Convert a positive integer to its Roman numeral representation."""
    result = []
    # BUG: only handles the plain additive numerals, so subtractive cases like
    # 4 (IV) and 9 (IX) come out as IIII / VIIII.
    for value, symbol in _NUMERALS:
        while n >= value:
            result.append(symbol)
            n -= value
    return "".join(result)
