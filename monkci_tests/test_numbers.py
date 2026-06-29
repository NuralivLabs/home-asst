from monkci_demo.numbers import gcd


def test_gcd():
    assert gcd(12, 8) == 4
    assert gcd(17, 5) == 1
