from monkci_demo.collections2 import unique_sorted


def test_dedupes_and_sorts_ascending():
    assert unique_sorted([3, 1, 2, 3, 1]) == [1, 2, 3]
