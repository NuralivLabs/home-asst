from monkci_demo.anagram import is_anagram


def test_simple():
    assert is_anagram("listen", "silent") is True


def test_case_and_spaces():
    assert is_anagram("Dormitory", "Dirty Room") is True
