from monkci_demo.roman import to_roman


def test_simple():
    assert to_roman(3) == "III"
    assert to_roman(7) == "VII"


def test_subtractive():
    assert to_roman(4) == "IV"
    assert to_roman(9) == "IX"
    assert to_roman(40) == "XL"
