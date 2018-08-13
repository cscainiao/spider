import scrapy
from scrapy.spiders import CrawlSpider, Rule

from biquge.items import BiqugeItem
from scrapy_redis.spiders import RedisSpider


class biquge_spider(RedisSpider):
    name = 'biquge'

    # base_url = 'http://www.biquge.com.tw/{page}_{page}{num}/'
    redis_key = 'biquge:start_urls'
    # pages = [i for i in range(1, 20)]
    # nums = [j for j in range(0, 1000)]
    #
    # def start_requests(self):
    #     for page in self.pages:
    #         for num in self.nums:
    #             s = "%03d" % num
    #             yield scrapy.Request(self.base_url.format(page=page, num=s), self.parse)

    def parse(self, response):

        zhangjie_url = response.url
        xiaoshuoming = response.xpath('//*[@id="info"]/h1/text()').extract()[0]  # ectract_first(）里面可以传入取不到值时，默认的数据
        # print(xiaoshuoming)
        zhangjielianjie = response.xpath('//*[@id="list"]/dl/dd/a/@href').extract()

        for lianjie in zhangjielianjie:
            url = lianjie.split('/')[-1]
            content_url = zhangjie_url+url
            # print(content_url)
            yield scrapy.Request(content_url, self.parse_content, meta={
                            'xiaoshuoming': xiaoshuoming
                            }
                     )

    def parse_content(self, response):
        item = BiqugeItem()
        contents = response.xpath('//*[@id="content"]/text()').extract()
        item['xiaoshuoming'] = response.meta['xiaoshuoming'].strip()
        item['zhangjieming'] = response.xpath('/html/head/title/text()').extract()[0]
        conter = ''
        for content in contents:
            conter += content
        item['conter'] = conter
        yield item
