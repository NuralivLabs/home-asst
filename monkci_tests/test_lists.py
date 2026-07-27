from monkci_demo.lists import maximum


def test_basic():
    assert maximum([3, 1, 4, 1, 5, 9, 2, 6]) == 9


def test_last_is_largest():
    assert maximum([1, 2, 3, 10]) == 10


def test_negatives():
    assert maximum([-5, -2, -9]) == -2
