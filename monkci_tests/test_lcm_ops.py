from monkci_demo.lcm_ops import lcm


def test_lcm_basic():
    assert lcm(4, 6) == 12


def test_lcm_coprime():
    assert lcm(3, 5) == 15
