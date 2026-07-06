from monkci_demo.numbers2 import is_prime


def test_known_primes():
    assert is_prime(2) is True
    assert is_prime(7) is True


def test_one_and_composites_are_not_prime():
    assert is_prime(1) is False
    assert is_prime(9) is False
