from monkci_demo.brackets import is_balanced


def test_balanced():
    assert is_balanced("(a[b]{c})") is True


def test_unclosed():
    assert is_balanced("(a[b]") is False
