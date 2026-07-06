from monkci_demo.strings2 import word_count


def test_simple():
    assert word_count("hello world") == 2


def test_multiple_spaces():
    assert word_count("hello   world  foo") == 3
