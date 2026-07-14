from monkci_demo.dedup import dedup


def test_removes_duplicates():
    assert dedup([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_strings_preserve_order():
    assert dedup(["b", "a", "b", "c", "a"]) == ["b", "a", "c"]
