from monkci_demo.collections2 import unique_sorted
from monkci_demo.numbers2 import is_prime
from monkci_demo.strings2 import word_count


def test_pipeline_summary():
    text = "the quick brown   fox"
    n = word_count(text)
    assert n == 4
    assert is_prime(n) is False
    assert unique_sorted([n, 2, 3]) == sorted({n, 2, 3})
