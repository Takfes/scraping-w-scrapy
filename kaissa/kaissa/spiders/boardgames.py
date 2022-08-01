import scrapy


class BoardgamesSpider(scrapy.Spider):
    name = 'boardgames'
    allowed_domains = ['www.kaissagames.com','kaissagames.com']
    start_urls = ['https://kaissagames.com/b2c_gr/epitrapezia-kaissa.html']

    def parse(self, response):
        items = response.xpath('//div[@class="products wrapper grid products-grid"]/ol/li')
        for item in items:
            title = item.xpath('normalize-space(.//a[@class="product-item-link"]/text())').get()
            price = item.xpath('.//span[@class="price"]/text()').get()
            sku   = item.xpath('normalize-space(.//div[@class="sku"]/text())').get()
            yield{
                'title':title,
                'price':price,
                'sku'  :sku
            }
        next_page = response.xpath('(//a[@class="action  next"])[2]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse)