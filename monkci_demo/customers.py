"""Customer helpers."""

from __future__ import annotations

from monkci_demo.orders import order_summary


def customer_label(customer: dict) -> str:
    """Human-readable label for a customer."""
    return customer["name"].title()


def recent_orders_summary(orders: list[dict]) -> list[str]:
    """Summarize a customer's recent orders."""
    return [order_summary(o) for o in orders]
