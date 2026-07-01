from monkci_demo.discount import apply_discount


def test_basic():
    assert apply_discount(100.0, 10) == 90.0


def test_cents():
    assert apply_discount(19.99, 15) == 16.99
