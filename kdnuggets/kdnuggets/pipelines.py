# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/tags/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class KdnuggetsPipeline:

    def __init__(self):
        self.con = sqlite3.connect('kdnuggets.db')
        self.cursor = self.con.cursor()
        self.create_table()

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.con.close()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS kdnuggets(
                url TEXT PRIMARY KEY,
                title TEXT,
                tag TEXT,
                year INTEGER,
                month INTEGER
            )
            """)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.cursor.execute(
            """INSERT OR IGNORE INTO kdnuggets VALUES (?,?,?,?,?)""",
            (adapter.get('url'), adapter.get('title'), adapter.get('tag'), int(adapter.get('year')), int(adapter.get('month'))))
        self.con.commit()
        return item
