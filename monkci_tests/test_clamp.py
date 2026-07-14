from monkci_demo.clamp import clamp


def test_within_range():
    assert clamp(5, 0, 10) == 5


def test_clamps_bounds():
    assert clamp(-3, 0, 10) == 0
    assert clamp(42, 0, 10) == 10
