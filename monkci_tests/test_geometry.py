from monkci_demo.geometry import box_volume


def test_unit_cube():
    assert box_volume(1, 1, 1) == 1


def test_box():
    assert box_volume(2, 3, 4) == 24
