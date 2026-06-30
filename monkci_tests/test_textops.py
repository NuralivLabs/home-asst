from monkci_demo.textops import reverse_words


def test_reverse_words():
    assert reverse_words("the quick fox") == "fox quick the"


def test_two():
    assert reverse_words("hello world") == "world hello"
