from monkci_demo.nested import flatten


def test_flatten():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_single():
    assert flatten([[9]]) == [9]
