
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
import scrapy
from scrapy import Selector

from qidianspider.items import doubanItem


"""
class DoubanSpider(scrapy.Spider):

    name = 'douban'

    # start_urls = {
    #     'https://movie.douban.com/top250/'
    #
    # }
    # rules = (
    #     Rule(LinkExtractor(allow='https://movie.douban.com/top250.*'),
    #          callback='parse_item'),
    # )

    def start_requests(self):
        base_url = 'https://movie.douban.com/top250?'
        for i in range(0, 10):
            url = base_url + 'start=' + str(i*25) + '&filter='
            yield scrapy.Request(url, callback=self.parse)
"""


class DoubanSpider(CrawlSpider):

    name = 'douban'

    start_urls = {
        'https://movie.douban.com/top250/'

    }
    rules = (
        Rule(LinkExtractor(allow=r'https://movie.douban.com/top250.*'),
             callback='parse_item'),
    )

    def parse_item(self, response):
        items = doubanItem()
        res = Selector(response)
        items['name'] = res.xpath('//div[@class="hd"]/a/span[1]/text()').extract()  # 电影名
        items['imgs'] = res.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div/a/img/@src').extract()
        # 导演,主演
        directors_info = res.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[1]').extract()
        # 年份, 国家,分类
        movies_info = res.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[2]').extract()
        # 评分
        items['rate'] = res.xpath('//span[@class="rating_num"]/text()').extract()
        # print(items)

        return items

