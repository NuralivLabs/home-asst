from monkci_demo.versions import compare_versions, latest


def test_compare_patch():
    assert compare_versions("1.2.10", "1.2.9") == 1


def test_compare_minor():
    assert compare_versions("1.2.3", "1.10.0") == -1


def test_equal():
    assert compare_versions("2.0.0", "2.0.0") == 0


def test_latest():
    assert latest(["1.2.9", "1.2.10", "1.2.2"]) == "1.2.10"
