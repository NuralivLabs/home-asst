from monkci_demo.pagination import paginate, page_count


def test_first_page():
    assert paginate(list(range(10)), 1, 3) == [0, 1, 2]


def test_second_page():
    assert paginate(list(range(10)), 2, 3) == [3, 4, 5]


def test_page_count():
    assert page_count(10, 3) == 4
