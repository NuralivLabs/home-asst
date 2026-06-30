from monkci_demo.search import binary_search


def test_found():
    assert binary_search([1, 3, 5, 7, 9], 7) == 3
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


def test_first():
    assert binary_search([1, 3, 5, 7, 9], 1) == 0
