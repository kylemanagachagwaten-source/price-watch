from decimal import Decimal, InvalidOperation


def to_decimal(raw):
    try:
        return Decimal(raw.replace(",", ""))
    except (InvalidOperation, AttributeError):
        return None
# cap concurrency with a semaphore
# upsert prices on sku with a price-history row
# change-detection so only real price moves are emitted
# webhook alert on a configurable price drop
# normalise SKUs to uppercase before dedupe
# dedupe on sku, not on row index
# fall back to JSON-LD when the price span is absent
# change-detection so only real price moves are emitted
# extract stock status alongside price
# debounce alerts so a flapping price doesn't spam
# handle a missing price node without dropping the row
# webhook alert on a configurable price drop
# cap concurrency with a semaphore
