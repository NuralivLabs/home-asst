from monkci_demo.titlecase import title_case


def test_basic():
    assert title_case("the lord of the rings") == "The Lord of the Rings"


def test_all_caps_words():
    assert title_case("war and peace") == "War and Peace"
