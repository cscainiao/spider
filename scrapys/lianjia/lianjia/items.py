# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    house_id = scrapy.Field()
    house_area = scrapy.Field()
    house_title = scrapy.Field()
    house_address = scrapy.Field()
    house_describe = scrapy.Field()
    house_flood = scrapy.Field()
    house_followInfo = scrapy.Field()
    house_tag = scrapy.Field()
    house_totalPrice = scrapy.Field()
    house_unitPrice = scrapy.Field()



