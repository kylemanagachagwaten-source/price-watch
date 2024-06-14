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
