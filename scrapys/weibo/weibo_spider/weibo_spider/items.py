# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    screen_name = scrapy.Field()
    profile_image_url = scrapy.Field()
    profile_url = scrapy.Field()
    verified_reason = scrapy.Field()
    close_blue_v = scrapy.Field()
    description = scrapy.Field()
    gender = scrapy.Field()
    followers_count = scrapy.Field()
    follow_count = scrapy.Field()
    avatar_hd = scrapy.Field()



