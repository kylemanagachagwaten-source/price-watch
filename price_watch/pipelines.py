class PostgresPipeline:
    def process_item(self, item, spider):
        self.db.upsert("prices", item, key="sku")
        return item
