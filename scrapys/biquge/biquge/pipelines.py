# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import pymongo
from scrapy.conf import settings
import redis

from biquge.items import biquge_url_item, BiqugeItem


class BiqugePipeline(object):
    """
    下载小说
    """
    def __init__(self):
        conn = pymongo.MongoClient(host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'], )
        db = conn.biquge
        self.collection = db.xiaoshuo

    def process_item(self, item, spider):
        if isinstance(item, BiqugeItem):
            base_path = '/Users/xiongxing/Desktop/biquge/'
            create_dir_path = base_path + item['xiaoshuoming']
            try:
                os.mkdir(create_dir_path)
            except:
                pass

            filename = create_dir_path + '/' + item['zhangjieming'] + '.txt'

            with open(filename, 'a', encoding='utf-8', newline='') as f:
                f.write(item['zhangjieming'])
            with open(filename, 'a', encoding='utf-8', newline='') as f:
                f.write(item['conter'])
        return item


class biquge_urlPipeline(object):
    """
    向redis中存储url
    """
    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1', port=6379)

    def process_item(self, item, spider):
        # 向redis中插入需要爬取的链接地址
        if isinstance(item, biquge_url_item):
            print(item)
            self.r.lpush('biquge:start_urls', item['url'])
            return item