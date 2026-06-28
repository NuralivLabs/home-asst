from monkci_demo.text import truncate


def test_no_truncation_needed():
    assert truncate("hello", 10) == "hello"


def test_respects_limit():
    # result including the ellipsis must be <= limit
    result = truncate("hello world", 8)
    assert result == "hello..."
    assert len(result) <= 8
