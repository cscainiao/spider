# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import settings   # 导入settings  也可以直接导入文件


class DouBanSpiderPipeline(object):

    def __init__(self):
        conn = pymongo.MongoClient(host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'], )
        db = conn.douban
        self.collection = db.movie

    def process_item(self, item, spider):

        for i in range(len(item['name'])):
            data = {}
            data['name'] = item['name'][i]
            data['imgs'] = item['imgs'][i]
            data['rate'] = item['rate'][i]
            # print(data)
            # self.collection.insert(data)
            self.collection.update({'name': data['name']}, {'$set': data}, True)
        return item

