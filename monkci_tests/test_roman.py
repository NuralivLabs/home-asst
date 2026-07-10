from monkci_demo.roman import to_roman


def test_additive():
    assert to_roman(3) == "III"
    assert to_roman(2026) == "MMXXVI"


def test_subtractive():
    assert to_roman(4) == "IV"
    assert to_roman(9) == "IX"
    assert to_roman(94) == "XCIV"
