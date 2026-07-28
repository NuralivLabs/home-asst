from monkci_demo.lru import LRUCache


def test_basic_put_get():
    c = LRUCache(1)
    c.put("x", 10)
    assert c.get("x") == 10


def test_get_marks_recently_used():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") == 1
    c.put("c", 3)
    assert c.get("b") is None
    assert c.get("a") == 1
    assert c.get("c") == 3
