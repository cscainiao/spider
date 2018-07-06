

import scrapy

from lianjia.items import LianjiaItem


class lianJiaSpider(scrapy.Spider):

    name = 'lianjia'

    loupan_url = 'https://cd.fang.lianjia.com/loupan/'
    ershoufang_url = 'https://cd.lianjia.com/ershoufang/{area}/'

    areas_list = ['jinjiang', 'qingyang', 'wuhou', 'gaoxin7', 'chenghua', 'jinniu',
                  'tianfuxinqu', 'gaoxinxi1', 'shuangliu', 'wenjiang', 'pidou', 'longquanyi',
                  'xindou', 'tianfuxinqunanqu'
                  ]

    def start_requests(self):
        for area in self.areas_list:
            yield scrapy.Request(self.ershoufang_url.format(area=area), self.parse)

    def parse(self, response):
        total_nums = response.xpath('/html/body/div[4]/div[1]/div[2]/h2/span/text()').extract()[0]
        total_pages = int(total_nums) // 30 + 1
        if total_pages <= 100:
            for num in range(1, total_pages + 1):
                base_url = response.url
                url = base_url + 'pg' + str(num) + '/'
                yield scrapy.Request(url, self.parse_house_info)
        if total_pages > 100:
            for num in range(1, 101):
                base_url = response.url
                url = base_url + 'pg' + str(num) + '/'
                yield scrapy.Request(url, self.parse_house_info)

    def parse_house_info(self, response):
        lis = response.xpath('/html/body/div[4]/div[1]/ul/li')
        item = LianjiaItem()
        for li in lis:
            item['house_id'] = li.xpath('./div[1]/div[1]/a/@data-housecode').extract()[0]
            item['house_area'] = response.xpath('/html/body/div[4]/div[1]/div[8]/div[1]/h1/a/text()').extract()[0].split('二')[0]
            item['house_title'] = li.xpath('./div[1]/div[1]/a/text()').extract()[0]
            item['house_address'] = li.xpath('./div[1]/div[@class="address"]/div/a/text()').extract()[0]
            item['house_describe'] = li.xpath('./div[1]/div[@class="address"]/div[1]/text()').extract()[0]
            item['house_flood'] = li.xpath('./div[1]/div[@class="flood"]/div[1]/text()').extract()[0]
            item['house_followInfo'] = li.xpath('./div[1]/div[@class="followInfo"]/text()').extract()[0]
            item['house_tag'] = li.xpath('./div[1]/div[@class="tag"]/span/text()').extract()
            item['house_totalPrice'] = li.xpath('./div[1]/div[@class="priceInfo"]/div[1]/span/text()').extract()[0]
            item['house_unitPrice'] = li.xpath('./div[1]/div[@class="priceInfo"]/div[2]/span/text()').extract()[0]
            yield item
