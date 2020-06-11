# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeTrainInformationItem(scrapy.Item):
    
    number = scrapy.Field()
    threeTierAC = scrapy.Field()
    twoTierAC = scrapy.Field()
    firstAC = scrapy.Field()
    sleeper = scrapy.Field()
    pantryIndicator = scrapy.Field()
    rakeType = scrapy.Field()
    origin = scrapy.Field()
    destination =scrapy.Field()
    
