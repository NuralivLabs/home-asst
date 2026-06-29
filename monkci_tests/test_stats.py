from monkci_demo.stats import average


def test_average():
    assert average([1, 2, 4]) == 7 / 3
