from monkci_demo.palindrome import is_palindrome


def test_simple():
    assert is_palindrome("racecar") is True


def test_ignores_case_and_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True
