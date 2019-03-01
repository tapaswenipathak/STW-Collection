from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from SWD.items import SWDItem
import re
import sys
import os

sys.path.append('path/to/project')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")

from product.models import Product


class SWDSpider (CrawlSpider):
  handle_httpstatus_list = [302]
  name = "swd"  # Your spider namme
  allowed_domains = ["swd.com"]  # Domain name
  start_urls = ['www.swd.com/abc.html']  # Start URL, can be more than one

						]
  # Can have multiple rules, exits on first rule matched
  rules = (
      Rule(SgmlLinkExtractor(allow=("", ), unique=False), callback='parse_item',  follow= True),
  )
  
  # Calls parse_item when rule matched
  def parse_item(self, response) :
    sel = Selector (response)
    item =  SWDItem ()
    item['Title'] = #Xpath for title
    item['Category'] = #xpath for some other field
    item['Product_URL'] = response.request.url #this gives the current url cralwed
    
    # Django database 

    item1 = Product() 
    item1.field_name = #assign value
    item1.save() #Save item in the database
    return item 

