from monkci_demo.ranges import sum_range


def test_inclusive():
    assert sum_range(1, 5) == 15


def test_single():
    assert sum_range(3, 3) == 3
