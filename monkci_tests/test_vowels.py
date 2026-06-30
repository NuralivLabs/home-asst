from monkci_demo.vowels import count_vowels


def test_lower():
    assert count_vowels("hello") == 2


def test_mixed_case():
    assert count_vowels("HELLO World") == 3
