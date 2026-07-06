from monkci_demo.batching import batch_items


def test_even_chunks():
    assert batch_items([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_remainder_chunk():
    assert batch_items([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
