from decimal import Decimal, InvalidOperation


def to_decimal(raw):
    try:
        return Decimal(raw.replace(",", ""))
    except (InvalidOperation, AttributeError):
        return None
# cap concurrency with a semaphore
