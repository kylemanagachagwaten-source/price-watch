import random


class RotatingProxy:
    def __init__(self, pool):
        self.pool = pool

    def process_request(self, request, spider):
        request.meta["proxy"] = random.choice(self.pool)
