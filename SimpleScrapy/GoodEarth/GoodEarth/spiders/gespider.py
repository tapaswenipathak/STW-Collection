from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from GoodEarth.items import GoodearthItem
import re

class GoodEarthSpider (CrawlSpider) :
  handle_httpstatus_list = [302]
  name = "ge"
  allowed_domains = ["goodearth.in"]
  start_urls = ['http://www.goodearth.in/']

  rules = (
      Rule(SgmlLinkExtractor(allow=(".*http://www.goodearth.in/.*", ), unique=True), callback='parse_item', follow= True),
  )
  def parse_item(self, response) :
    sel = Selector (response)
    items = []
    item = GoodearthItem ()
    item['Source_Website'] = "http://www.goodearth.in/"
    item['Title'] = sel.xpath ('//h1[@id="Ptitle"][@class="product-title"]/text()').extract()
    item['Product_Code'] = sel.xpath ('//span[@id="item_code"]/text()').extract()
    item['Category'] = sel.xpath ('//title/text()').extract()
    item['Product_URL'] = response.request.url
    desc = str(sel.xpath ('//div[@id="tab1"][@class="tab_content"]/div/text()').extract ())
    item['Dimensions_Care'] = sel.xpath ('//div[@id="tab2"][@class="tab_content"][@style="display:none;"]/div/text()').extract ()
    desc1 = ""

    for i in range (len (desc)) :
      if desc[i] == '\r\n' or desc[i] == '\n':
        continue
      else :
        desc1 += desc[i]
    item['Product_Details'] = desc1
    item['Image_URL'] =  sel.xpath ('//div[@class="product-img-box"]//ul/li/a/@href').extract()
    category = sel.xpath ('//ul[@class="breadcrum"]/li/a/text()').extract ()
    item['Category'] = category
    price = str (sel.xpath ("//div[@id='product_price']/text()").extract())
    price = re.findall ('\d+', price)
    item['Price'] = price

    if item['Product_Code'] :
        return item

