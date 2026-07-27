from monkci_demo.dates import is_leap_year


def test_regular_leap():
    assert is_leap_year(2024) is True


def test_non_leap():
    assert is_leap_year(2023) is False


def test_century_not_leap():
    assert is_leap_year(1900) is False


def test_400_leap():
    assert is_leap_year(2000) is True
