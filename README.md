### Resources
* [Udemy](https://www.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/)
* [Youtube](https://www.youtube.com/watch?v=pSyiJKdCKtc&t=623s)
* [SelectorsHub](https://chrome.google.com/webstore/detail/selectorshub/ndgimibanhlabgdgjcpbbndiehljcpfh?hl=en)
* [css](https://www.w3schools.com/cssref/css_selectors.asp) & [xpath](https://devhints.io/xpath) selectors
### Getting Started scrapy
* pip install [scrapy](https://docs.scrapy.org/en/latest/)
* scrapy shell __<url>__
* scrapy startproject __<project-name>__
* scrapy genspider __<spider-name>__ __<link>__
* scrapy crawl __<spider-name>__ -o dataset.jon
### Getting Started splash
* pip install [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash)
* docker pull scrapinghub/splash
* docker run -it -p 8050:8050 scrapinghub/splash
* localhost:8050
### Setup splash with scrapy
* in settings.py adjust : SPLASH_URL = 'http://localhost:8050/'
* in settings.py adjust : DOWNLOADED_MIDDLEWARES, SPLASH_MIDDLEWARES, DUPEFILTER_CLASS from [splash Github page](https://github.com/scrapy-plugins/scrapy-splash)
* inside the spider file remove starts_url
* insider the spider file :
```python
import scrapy
from scrapy_splash import SplashRequest
class exampleSpider(scrapy.Spider):
    name = 'spider-name'
    allowed_domains = ['www.example.com']
    script = '''<copy script.lua in here>'''
    def start_requests(self):
        yield SplashRequest(url="https://www...", 
                            callback=self.parse,
                            endpoint="execute",args={'lua_source':self.script})
    def parse(self,response):
        print(response.body)
```