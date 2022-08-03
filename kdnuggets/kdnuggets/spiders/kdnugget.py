import scrapy
import pandas as pd
from datetime import datetime
import re
from ..items import KdnuggetsItem
from scrapy.loader import ItemLoader


def extract_title(string):
    rgx = '\\d{4}\\/\\d{2}\\/(.*)\\.html'
    try:
        return re.search(rgx, string).groups()[0].replace('-', ' ')
    except:
        return None


class KdnuggetSpider(scrapy.Spider):
    name = 'kdnugget'
    allowed_domains = ['www.kdnuggets.com']
    start_urls = ['https://www.kdnuggets.com/']

    def start_requests(self):
        url = 'https://www.kdnuggets.com/{year}/{month}'
        start_year = 2015
        daterange = pd.date_range(
            start=f"{start_year}-01-01", end=f"{str(datetime.today().year)}-{str(datetime.today().month).zfill(2)}-01", freq='M')
        for dt in daterange:
            year, month = str(dt.year), str(dt.month).zfill(2)
            urlformatted = url.format(year=year, month=month)
            yield scrapy.Request(url=urlformatted, callback=self.parse, meta = {'year':year,'month':month})

    def parse(self, response):
        articles = response.xpath("//ul[@class='three_ul']/li")
        year,month = response.request.meta['year'],response.request.meta['month']
        for article in articles:
            
            # il = ItemLoader(item=KdnuggetsItem, selector=article)
            # il.add_xpath('url', "(.//a/@href)[1]")
            # il.add_xpath('title', "(.//a/@href)[1]")
            # il.add_xpath('tag', "(.//a)[2]/")
            # yield il.load_item()
            
            url = article.xpath(".//a/@href")[0].get()
            title = extract_title(url)
            tag = article.xpath("(.//a)[2]/text()").get()
            yield {
                'url':url,
                'title':title,
                'tag':tag,
                'year':year,
                'month':month
            }
