### Notes
* pip install [scrapy](https://docs.scrapy.org/en/latest/)
* scrapy startproject __project-name__
* scrapy genspider __spider-name__ __link__
* pip install [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash)
* docker run -it -p 8050:8050 scrapinghub/splash
* settings.py SPLASH_URL = 'http://localhost:8050/' (http://192.168.99.100:8050/)
* add DOWNLOADED_MIDDLEWARES, SPLASH_MIDDLEWARES, DUPEFILTER_CLASS from GIthub to settings.py
* inside the spider file remove starts_url
* inside the spider file add a variable 'scripts' equal to the lua script
* from scrapy_splash import SplashRequest
```python
* def start_requests(self):
    yield SplashRequest(url="https://www...", 
                        callback=self.parse,
                        endpoint="execute",
                        args={'lua_source':self.script})
```