# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field
from scrapy import Item

class DoubanItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    year = Field()
    score = Field()
    director = Field()
