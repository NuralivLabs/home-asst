from monkci_demo.math_ops import power


def test_square():
    assert power(3, 2) == 9


def test_cube():
    assert power(2, 3) == 8


def test_zero_exponent():
    assert power(5, 0) == 1
