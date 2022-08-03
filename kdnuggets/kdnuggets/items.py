# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
import re
# from w3lib.html import remove_tags


def extract_title(string):
    rgx = '\\d{4}\\/\\d{2}\\/(.*)\\.html'
    try:
        return re.search(rgx, string).groups()[0].replace('-', ' ')
    except:
        return None


class KdnuggetsItem(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(input_processor=MapCompose(extract_title), output_processor=TakeFirst())
    tag = scrapy.Field(output_processor=TakeFirst())
