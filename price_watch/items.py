from decimal import Decimal, InvalidOperation


def to_decimal(raw):
    try:
        return Decimal(raw.replace(",", ""))
    except (InvalidOperation, AttributeError):
        return None
# cap concurrency with a semaphore
# upsert prices on sku with a price-history row
# change-detection so only real price moves are emitted
