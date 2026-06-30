"""Balanced brackets check."""

from __future__ import annotations

_PAIRS = {")": "(", "]": "[", "}": "{"}


def is_balanced(s: str) -> bool:
    """Return True if all brackets in s are correctly matched and nested."""
    stack: list[str] = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != _PAIRS[ch]:
                return False
    return True
