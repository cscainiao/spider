

import scrapy

from biquge.items import biquge_url_item


class biquge_url_spider(scrapy.Spider):
    """
    负责将url存入redis
    """

    name = 'biquge_url'

    base_url = 'http://www.biquge.com.tw/{page}_{page}{num}/'
    start_urls = {
        'http://www.biquge.com.tw/'
    }  # url没有用, 只是为了去执行parse函数

    def parse(self, response):
        item = biquge_url_item()
        pages = [i for i in range(1, 20)]
        nums = [j for j in range(0, 1000)]
        for page in pages:
            for num in nums:
                s = "%03d" % num
                item['url'] = self.base_url.format(page=page, num=s)
                yield item
