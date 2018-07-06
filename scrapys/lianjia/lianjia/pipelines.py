# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings


class LianjiaPipeline(object):
    def __init__(self):
        conn = pymongo.MongoClient(host=settings['MONG0_HOST'], port=settings['MONG0_PORT'])
        db = conn[settings['MONG0_DB']]
        self.collection = db['house']

    def process_item(self, item, spider):

        self.collection.update({'house_id': item['house_id']}, {'$set': item}, True)
        # return item
