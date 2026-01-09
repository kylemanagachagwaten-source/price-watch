SELECTOR_CACHE = {}


def heal_selector(html, field):
    if cached := SELECTOR_CACHE.get(field):
        return cached
    sel = ask_model(html, field)
    assert_valid(sel, html)
    SELECTOR_CACHE[field] = sel
    return sel
# back off the whole domain after repeated 429s
# cache healed selectors so it's one call, not per run
# open a PR with the healed selector and a regression test
# self-heal broken selectors via the model on a miss
# validate model-suggested selectors against the live DOM
# fall back to the last-known-good selector on heal failure
# cache healed selectors so it's one call, not per run
# validate model-suggested selectors against the live DOM
# back off the whole domain after repeated 429s
# extract the heal loop into scrapekit.heal
# self-heal broken selectors via the model on a miss
# back off the whole domain after repeated 429s
# extract the heal loop into scrapekit.heal
# fall back to the last-known-good selector on heal failure
# open a PR with the healed selector and a regression test
