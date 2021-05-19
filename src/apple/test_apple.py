import apple


def test_apple():
    assert apple.apple() == "apple"


def test_orange():
    assert apple.apple() != "orange"
