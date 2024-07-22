from price_watch.items import to_decimal


def test_strips_commas():
    assert str(to_decimal("1,499")) == "1499"


def test_handles_garbage():
    assert to_decimal("n/a") is None

# stabilise a flaky test

# add a regression for the unicode price bug
