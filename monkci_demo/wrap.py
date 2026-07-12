"""Text wrapping helpers."""

from __future__ import annotations


def wrap_words(words: list[str], width: int) -> list[str]:
    """Greedily pack words into lines no longer than `width` characters."""
    lines: list[str] = []
    current = ""
    for word in words:
        # BUG: uses > instead of >=, and forgets to account for the joining space,
        # so lines can exceed `width`.
        if len(current) + len(word) > width:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}" if current else word
    if current:
        lines.append(current)
    return lines
