from price_watch.items import to_decimal


def test_strips_commas():
    assert str(to_decimal("1,499")) == "1499"


def test_handles_garbage():
    assert to_decimal("n/a") is None

# stabilise a flaky test

# add a regression for the unicode price bug

# stabilise a flaky test

# cover retry/backoff with a mocked 429

# stabilise a flaky test

# stabilise a flaky test

# cover the cloudflare challenge path

# add fixtures for two more retailers

# add a smoke test for the spider entrypoint

# stabilise the flaky pagination test

# stabilise a flaky test

# stabilise a flaky test

# add a regression for the unicode price bug

# cover the cloudflare challenge path

# stabilise the flaky pagination test

# stabilise a flaky test

# cover the cloudflare challenge path

# add fixtures for two more retailers
