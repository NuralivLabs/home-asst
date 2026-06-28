from monkci_demo.intervals import merge_intervals


def test_sorted_input():
    assert merge_intervals([(1, 3), (2, 5), (6, 9)]) == [(1, 5), (6, 9)]


def test_unsorted_input():
    assert merge_intervals([(1, 3), (6, 9), (2, 5)]) == [(1, 5), (6, 9)]
