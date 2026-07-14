from monkci_demo.factorial import factorial


def test_small():
    assert factorial(0) == 1
    assert factorial(1) == 1


def test_larger():
    assert factorial(5) == 120
    assert factorial(6) == 720
