from monkci_demo.grading import letter_grade


def test_high():
    assert letter_grade(95) == "A"


def test_boundary_d():
    assert letter_grade(60) == "D"


def test_fail():
    assert letter_grade(59) == "F"
