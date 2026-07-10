from monkci_demo.slugify import slugify


def test_simple():
    assert slugify("Hello World") == "hello-world"


def test_collapses_and_trims_separators():
    assert slugify("  Hello,   World!  ") == "hello-world"
