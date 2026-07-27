from monkci_demo.primes import is_prime


def test_small_primes():
    assert [is_prime(n) for n in (2, 3, 5, 7, 11, 13)] == [True] * 6


def test_non_primes():
    assert [is_prime(n) for n in (0, 1, 4, 6, 8, 9)] == [False] * 6


def test_square_of_prime():
    assert is_prime(25) is False
    assert is_prime(49) is False
