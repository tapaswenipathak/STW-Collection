# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TryItem(Item):
    # define the fields for your item here like:
    # name = Field()
    Title = Field ()
    Price = Field ()
    Description = Field ()      
    Image_URL = Field ()
    Source_Website = Field ()
    Product_URL = Field ()
    Category = Field ()
    Details = Field ()
    pass
