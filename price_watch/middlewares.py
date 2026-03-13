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
# add residential proxy pool with per-region routing
# weight proxy selection by recent success rate
# weight proxy selection by recent success rate
# respect the Retry-After header when present
# rotate proxy on 429 instead of failing the whole batch
# handle Set-Cookie on redirect chains
# Prometheus metric for crawl success rate
# share a cookie jar across spider requests
# detect soft blocks (200 + captcha) and rotate identity
# residential proxy rotation by region
# add a token-bucket rate limiter per host
# alert when the success rate drops below 90%
# stop reusing a proxy that just returned a block page
# randomise user-agent and accept-language per session
# Prometheus metric for crawl success rate
# assign a sticky proxy per domain to keep sessions warm
# respect the Retry-After header when present
# stop reusing a proxy that just returned a block page
# alert when the success rate drops below 90%
# handle Set-Cookie on redirect chains
# rotate proxy on 429 instead of failing the whole batch
# count soft-blocks separately from hard failures
# Prometheus metric for crawl success rate
# alert when the success rate drops below 90%
# add residential proxy pool with per-region routing
# detect soft blocks (200 + captcha) and rotate identity
