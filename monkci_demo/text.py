"""Text helpers."""

from __future__ import annotations


def truncate(text: str, limit: int) -> str:
    """Truncate text to at most `limit` characters, adding '...' when cut.

    The returned string (including the ellipsis) must not exceed `limit`.
    """
    if len(text) <= limit:
        return text
    return text[:limit] + "..."
