from monkci_demo.fizz import fizzbuzz


def test_basics():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(7) == "7"


def test_fifteen():
    assert fizzbuzz(15) == "FizzBuzz"
