import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class BarmanSpider(CrawlSpider):
    name = 'barman'
    allowed_domains = ['sipwhiskey.com']
    start_urls = ['https://sipwhiskey.com/collections/alcohol']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//a[@class='product-link']")),callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//a[@class='next']")))
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath("//h1[@class='title']/text()").get()
        price = response.xpath("//span[@class='price theme-money']/text()").get()
        item['price'] = price.replace('$','')
        item['vendor'] = response.xpath("//div[@class='vendor']/a/text()").get()
        description = response.xpath("//div[@class='description user-content']/descendant-or-self::node()/text()").getall()
        item['description'] = re.sub('[\n\s]+',' '," ".join(description)).strip()
        return item
