from monkci_demo.orders import order_summary


def test_order_summary():
    order = {"id": "A1", "customer": {"name": "jane doe"}}
    assert order_summary(order) == "A1 for Jane Doe"
