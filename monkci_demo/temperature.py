"""Temperature conversion helpers."""

from __future__ import annotations


def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit: F = C * 9/5 + 32."""
    # BUG: forgets the * 9/5 scaling, so it only adds the 32 offset.
    return c + 32
