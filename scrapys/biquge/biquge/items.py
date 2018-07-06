# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):
    # define the fields for your item here like:
    xiaoshuoming = scrapy.Field()   # 小说名称
    zhangjieming = scrapy.Field()   # 小说章节名
    conter = scrapy.Field()         # 章节内容


class biquge_url_item(scrapy.Item):
    url = scrapy.Field()  # 需要爬取的url
