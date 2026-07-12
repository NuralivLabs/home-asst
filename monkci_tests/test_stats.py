from monkci_demo.stats import mean


def test_simple_mean():
    assert mean([2, 4, 6]) == 4.0


def test_single_value():
    assert mean([10]) == 10.0
