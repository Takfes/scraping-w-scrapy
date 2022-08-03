### Resources
* [Udemy](https://www.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/) - [Youtube](https://www.youtube.com/watch?v=aIHTgF6polk&list=PLRzwgpycm-Fjvdf7RpmxnPMyJ80RecJjv) - [SelectorsHub](https://chrome.google.com/webstore/detail/selectorshub/ndgimibanhlabgdgjcpbbndiehljcpfh?hl=en) - [cloudfare](https://checkforcloudflare.selesti.com/) - [scrapy](https://docs.scrapy.org/en/latest/)
* [css](https://www.w3schools.com/cssref/css_selectors.asp) & [xpath](https://devhints.io/xpath) selectors
___
### Scrapy CLI
* scrapy startproject <__project-name__>
* scrapy genspider __<spider-name>__ __www.worldometers.info/world-population/population-by-country/__ _add -l flag to list spiders_ & _[crawl with basic spider](https://www.youtube.com/watch?v=-mkewdn9JdU&list=PLRzwgpycm-Fjvdf7RpmxnPMyJ80RecJjv&index=9)_
* scrapy genspider -t crawl __<spider-name>__ __sipwhiskey.com__ _traverse a catalogue, visit links, extract info, continue with the rest of the catalogue_
* adjust __allowed_domains__ to __exclude http(s)__ protocol and __start_urls__ to start with __https__ instead of _http_
* scrapy crawl __<spider-name>__ -o dataset.json _[how to pass argument](https://youtu.be/yrv9V7ZG5hI)_ & _[spoofing user-agent](https://youtu.be/-mkewdn9JdU)_
* [how to pass information across spider functions](/worldometers/worldometers/spiders/countries.py) :

> _yield response.follow(url=link,callback=self.parse_country,meta = {'country_name':name})_

> _scrapy shell_

```python
# Open 'scrapy shell' ; from inside the scrapy shell
# r = scrapy.Request(url="https://www.worldometers.info/world-population/population-by-country/")
# fetch(r)
fetch("https://www.worldometers.info/world-population/population-by-country/")
view(response)
response.body
countries = response.xpath("//td/a/text()").getall()
```
___
### CSS Selectors
```css
div.intro
div#location
.bold.italic
li[data-identifier=7]
a[href^='start']
a[href$='end']
a[href~='between']
div.intro p, span#location
div.intro > p
div.intro + p
div.intro ~ p
li:nth-child(1),li:nth-child(3)
li:nth-child(odd)
```
### XPATH Selectors
```xpath
<!-- general -->
//a/@href
//div[@class="classname"]/p
//div[@class="intro" or @class='outro']/p/text()
//a[starts-with(@href,'start')]
//a[ends-with(@href,'end')]
//a[contains(@href,'google')]
//a[contains(text(),'text')]
//ul[@id='items']/li[1]
//ul[@id='items']/li[position()>1 or position()=last()]
//li[position()=1 and contains(@text,'hello')]
<!-- move up axes -->
//p[@id='unique']/parent::div
//p[@id='unique']/parent::node()
//p[@id='unique']/ancestor::node()
//p[@id='unique']/ancestor-or-self::node()
//p[@id='unique']/preciding::node()
//p[@id='outside']/preceding-sibling::node()
<!-- move down axes -->
//div[@class='intro']/child::p
//div[@class='intro']/child::node()
//div[@class='intro']/following::node()
//div[@class='intro']/following-sibling::node()
//div[@class='intro']/descendant::node()
//div[@class='description user-content']/descendant-or-self::node()/text()
```
___
### Scrapy And JavaScript
* [scrapy-selenium](https://github.com/clemfromspace/scrapy-selenium)
* [scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) [Youtube](https://www.youtube.com/watch?v=0wO7K-SoUHM&list=PLRzwgpycm-Fjvdf7RpmxnPMyJ80RecJjv&index=14)
* [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash) [Youtube](https://www.youtube.com/watch?v=mTOXVRao3eA&list=PLRzwgpycm-Fjvdf7RpmxnPMyJ80RecJjv&index=6)

___
### Splash in Docker
* pip install [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash) ipython
* docker pull scrapinghub/splash
* docker run -it -p 8050:8050 scrapinghub/splash
* localhost:8050
* in settings.py adjust : SPLASH_URL = 'http://localhost:8050/'
* in settings.py adjust : DOWNLOADED_MIDDLEWARES, SPLASH_MIDDLEWARES, DUPEFILTER_CLASS from [splash Github page](https://github.com/scrapy-plugins/scrapy-splash)
* inside the spider file remove starts_url
* insider the spider file :
<br>

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