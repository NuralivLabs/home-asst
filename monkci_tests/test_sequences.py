from monkci_demo.sequences import fib


def test_zero():
    assert fib(0) == 0


def test_one():
    assert fib(1) == 1


def test_ten():
    assert fib(10) == 55


def test_small_sequence():
    assert [fib(i) for i in range(6)] == [0, 1, 1, 2, 3, 5]
