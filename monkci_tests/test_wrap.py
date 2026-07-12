from monkci_demo.wrap import wrap_words


def test_no_line_exceeds_width():
    # Two 5-char words at width 10: "gamma delta" is 11 chars — must wrap.
    words = ["gamma", "delta", "alpha", "stone"]
    width = 10
    lines = wrap_words(words, width)
    assert all(len(line) <= width for line in lines), lines


def test_reassembles_all_words():
    words = ["one", "two", "three", "four"]
    assert " ".join(wrap_words(words, 9)).split() == words
