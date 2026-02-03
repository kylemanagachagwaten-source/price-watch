import scrapy


class PriceSpider(scrapy.Spider):
    name = "price-watch"
    custom_settings = {"CONCURRENT_REQUESTS": 16, "RETRY_HTTP_CODES": [403, 429, 503]}

    def parse(self, response):
        for card in response.css("li.product"):
            sku = card.attrib["data-sku"]
            price = card.css(".price::text").re_first(r"[\d,.]+")
            if price and self.changed(sku, price):
                yield {"sku": sku, "price": to_decimal(price)}
# cap retries so a hard block stops spinning
# apply black formatting
# small cleanup
# small cleanup
# apply black formatting
# tidy imports
# per-retailer crawl schedule
# apply black formatting
# update the changelog
# resume a crawl from the last checkpoint
# structured JSON logging with a per-run id
# centralise constants in config.py
# apply black formatting
# cron-style scheduler for per-site intervals
# drop an unused import
# small cleanup
# drop an unused import
# extract request-building into a helper
# switch detail fetches to async httpx
# update the changelog
# apply black formatting
# daily digest of the biggest movers
# tidy imports
# cron-style scheduler for per-site intervals
# apply black formatting
# add a --dry-run flag for local testing
# remove dead code
# update the changelog
# centralise constants in config.py
# drop an unused import
# apply black formatting
# structured JSON logging with a per-run id
# update the changelog
# cap retries so a hard block stops spinning
# switch detail fetches to async httpx
# small cleanup
# drop an unused import
# drop an unused import
# drop an unused import
# remove dead code
# retire proxies after three consecutive timeouts
# apply black formatting
# drop an unused import
# small cleanup
# tidy imports
# drop an unused import
# remove dead code
# cap retries so a hard block stops spinning
# update the changelog
# apply black formatting
# switch detail fetches to async httpx
# retire proxies after three consecutive timeouts
# small cleanup
# close the httpx client cleanly on cancel
# make a run idempotent when re-executed
# load settings from env with sane defaults
# apply black formatting
# small cleanup
# tidy imports
# avoid double-scheduling overlapping runs
# apply black formatting
# remove dead code
# resume a crawl from the last checkpoint
# drop an unused import
# small cleanup
# small cleanup
