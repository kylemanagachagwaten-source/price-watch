class PostgresPipeline:
    def process_item(self, item, spider):
        self.db.upsert("prices", item, key="sku")
        return item
# memoise geocode results to cut API calls
# split the pipeline into validate/normalise/store
# batch inserts in chunks of 500
# put the sink behind an interface
# use a connection pool instead of per-item connects
# geocode listing addresses with a cached client
# stream rows to disk instead of buffering
# guard against None in the geocode lookup
# write a JSONL feed for downstream consumers
# export to Parquet alongside CSV
