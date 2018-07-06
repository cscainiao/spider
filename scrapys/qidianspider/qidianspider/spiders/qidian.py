
import scrapy
from scrapy import Selector


class QiDianSpider(scrapy.Spider):

    name = 'qidian'     # 启动项目指定 的name参数

    # 需要爬取的url
    start_urls = {
        'https://www.qidian.com/',
    }

    def parse(self, response):
        # print(response)
        # print(response.body)  源码信息
        res = Selector(response)
        menu_type = res.xpath('//cite/span/i/text()').extract()
        print(menu_type)
        return response
