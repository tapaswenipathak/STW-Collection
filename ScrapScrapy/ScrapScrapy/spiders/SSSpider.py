from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from ScrapScrapy.items import ScrapscrapyItem

class ScrapyscrapSpider (BaseSpider) :
  name = "ss"
  allowed_domains = ["scrapy.org"]
  start_urls = ['http://scrapy.org/']

  def parse(self, response) :
    sel = Selector (response)
    item = ScrapscrapyItem ()
    item['Heading'] = str (sel.xpath ('//*[@id="content"]/h3/text()').extract ()) + str (sel.xpath ('//*[@id="content"]/dl/h3/text()').extract ())
    item['Content'] = str (map (unicode.strip, sel.xpath ('//*[@id="content"]/p/text()').extract ()))
    item['Content'] += str (map (unicode.strip, sel.xpath ('//dl//text()').extract ()))
    item['Source_Website'] = "http://scrapy.org"
    return item

