"""Semantic version helpers."""

from __future__ import annotations


def compare_versions(a: str, b: str) -> int:
    """Compare two dotted version strings.

    Returns -1 if a < b, 0 if equal, 1 if a > b.
    Example: compare_versions("1.2.10", "1.2.9") -> 1
    """
    parts_a = a.split(".")
    parts_b = b.split(".")
    for x, y in zip(parts_a, parts_b):
        if x < y:
            return -1
        if x > y:
            return 1
    return 0


def latest(versions: list[str]) -> str:
    """Return the highest version from a list."""
    best = versions[0]
    for v in versions[1:]:
        if compare_versions(v, best) > 0:
            best = v
    return best
