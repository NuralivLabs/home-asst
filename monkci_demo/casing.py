"""Casing helpers."""

from __future__ import annotations


def title_case(text: str) -> str:
    """Capitalize the first letter of each word, lowercasing the rest."""
    return " ".join(w[0].upper() + w[1:].lower() for w in text.split())
