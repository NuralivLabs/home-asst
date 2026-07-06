"""Order helpers."""

from __future__ import annotations

from monkci_demo.customers import customer_label


def order_summary(order: dict) -> str:
    """Render a one-line summary of an order."""
    return f"{order['id']} for {customer_label(order['customer'])}"
