"""Title-casing."""

from __future__ import annotations

_SMALL = {"a", "an", "the", "of", "and", "in", "on"}


def title_case(text: str) -> str:
    """Title-case a heading: capitalize each word, but keep small words lowercase
    UNLESS the word is the first word (which is always capitalized)."""
    words = text.split()
    return " ".join(
        w if w in _SMALL else w.capitalize()
        for w in words
    )
