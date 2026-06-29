from monkci_demo.metrics import percent_change


def test_increase():
    assert percent_change(200, 250) == 25.0


def test_decrease():
    assert percent_change(200, 150) == -25.0
