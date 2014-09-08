from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from Try.items import TryItem
import re

class TrySpider (CrawlSpider) :
  handle_httpstatus_list = [302]
  name = "try" #Name of your spider
  allowed_domains = ["Try.in"] #Add allowed domains, leave it blank to allow everything
  start_urls = ['http://www.Try.in/'] #Has the start URL

  #allow add some regex or links to allow those
  #callback function for a url when allowed by the rul
  rules = (
      Rule(SgmlLinkExtractor(allow=(".*", ), unique=True), callback='parse_item', follow= True),
  )
  def parse_item(self, response) :
    sel = Selector (response)
    items = []
    item = TryItem ()
    item['Source_Website'] = "http://www.Try.in/"
    item['Title'] = sel.xpath ('Your_x_path').extract()
    return item

