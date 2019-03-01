from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from SS.items import SSItem
import re


class SSSpider (CrawlSpider):
    handle_httpstatus_list = [302]
    name = "ss"  # Name of your spider
    # Add allowed domains, leave it blank to allow everything
    allowed_domains = ["SS.in"]
    start_urls = ['http://www.SS.in/']  # Has the start URL

    # allow add some regex or links to allow those
    # callback function for a url when allowed by the rul
    rules = (
        Rule(SgmlLinkExtractor(allow=(".*", ), unique=True),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        sel = Selector(response)
        items = []
        item = SSItem()
        item['Source_Website'] = "http://www.SS.in/"
        item['Title'] = sel.xpath('Your_x_path').extract()
        return item
