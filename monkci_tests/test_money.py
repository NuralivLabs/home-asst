from monkci_demo.money import to_cents


def test_exact():
    assert to_cents(19.99) == 1999


def test_rounds_half_up():
    assert to_cents(0.105) == 11
