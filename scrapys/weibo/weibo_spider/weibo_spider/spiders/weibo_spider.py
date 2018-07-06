import json

import scrapy
from scrapy import Selector

from weibo_spider.items import WeiboSpiderItem


class weibo_spider(scrapy.Spider):

    name = 'weibo'

    user_info_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&containerid=100505{uid}'
    followers_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}'
    follow_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{uid}&lfid=107603{uid}'
    start_user_id = '5055034462'

    def start_requests(self):
            yield scrapy.Request(self.user_info_url.format(uid=self.start_user_id), callback=self.parse)
            yield scrapy.Request(self.followers_url.format(uid=self.start_user_id), callback=self.parse_followers)
            yield scrapy.Request(self.follow_url.format(uid=self.start_user_id), callback=self.parse_follow)

    def parse(self, response):
        """
        获取用户信息
        :param response:
        :return:
        """
        item = WeiboSpiderItem()
        res = json.loads(response.text)
        results = res.get('data').get('userInfo')
        for field in item.fields:
            item[field] = results.get(field)
        yield item
        yield scrapy.Request(self.follow_url.format(uid=results.get('id')), callback=self.parse_follow)
        yield scrapy.Request(self.followers_url.format(uid=results.get('id')), callback=self.parse_followers)

    def parse_followers(self, response):
        """
        获取粉丝信息
        """
        res = json.loads(response.text)
        card_group = res['data']['cards'][-1]['card_group']
        for data in card_group:
            uid = data['user']['id']
            yield scrapy.Request(self.user_info_url.format(uid=uid), callback=self.parse)

    def parse_follow(self, response):
        res = json.loads(response.text)
        card_group = res['data']['cards'][-1]['card_group']
        for data in card_group:
            # print(data)
            uid = data['user']['id']
            yield scrapy.Request(self.user_info_url.format(uid=uid), callback=self.parse)