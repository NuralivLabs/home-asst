"""Slug helpers."""

from __future__ import annotations

import re


def slugify(text: str) -> str:
    """Lowercase, trim, and turn runs of non-alphanumerics into single hyphens."""
    text = text.strip().lower()
    # BUG: replaces each non-alphanumeric char individually, so runs of spaces/
    # punctuation produce multiple hyphens instead of one, and leading/trailing
    # separators are not stripped.
    return re.sub(r"[^a-z0-9]", "-", text)
