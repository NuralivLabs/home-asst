"""Pagination helpers."""

from __future__ import annotations


def paginate(items: list, page: int, per_page: int) -> list:
    """Return the slice of `items` for a 1-indexed `page`.

    page=1 -> the first `per_page` items.
    """
    start = page * per_page
    return items[start:start + per_page]


def page_count(total: int, per_page: int) -> int:
    """Number of pages needed to hold `total` items."""
    return (total + per_page - 1) // per_page
