#This codes need some cleaning


from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from Try.items import TryItem
from selenium import selenium
from selenium import webdriver
from scrapy.http import FormRequest
from scrapy import log
from time import strftime
from datetime import timedelta
from datetime import datetime
import datetime
from time import sleep
import time
import re

class TrySpider (CrawlSpider) :
  handle_httpstatus_list = [302]
  name = "try"
  allowed_domains = ["try.com"] #Add allowed domains, leave blank to allow all
  start_urls = [''] #Add start urls in this
  
  rules = (
      Rule(SgmlLinkExtractor(allow=(".*", ), unique=True), callback='parse_item', follow= True),
  )
  def __init__(self):
    CrawlSpider.__init__(self)
    self.verificationErrors = []
    self.selenium = selenium("localhost", 4444, "*chrome", "http://www.try.com")
    self.selenium.start()

  def __del__(self):
    self.selenium.stop()
    print self.verificationErrors
    CrawlSpider.__del__(self)

  def parse_item(self, response) :
    sel = Selector (response)
    item = TryItem ()
    sel1 = self.selenium
    sel1.open(response.url)
    #Wait for javscript to load in Selenium
    time.sleep(2.5)
    #Do some crawling of javascript created content with Selenium
    item['Source_Website'] = "https://www.try.com"
    item['Title'] = sel1.get_text ('') #write your xpath, it's a bit different for selenium
    
    #return or yield when you are done
    return item






