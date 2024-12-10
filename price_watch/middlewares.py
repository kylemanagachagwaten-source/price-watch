import random


class RotatingProxy:
    def __init__(self, pool):
        self.pool = pool

    def process_request(self, request, spider):
        request.meta["proxy"] = random.choice(self.pool)
# detect soft blocks (200 + captcha) and rotate identity
# rotating-proxy downloader middleware
# exponential backoff with jitter on 403/429/503
# refresh cookies before they expire mid-crawl
# retry on 403/429 with exponential backoff
# assign a sticky proxy per domain to keep sessions warm
# detect and skip captcha interstitials
