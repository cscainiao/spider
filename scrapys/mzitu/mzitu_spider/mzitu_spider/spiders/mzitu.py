
from scrapy.linkextractor import LinkExtractor
import scrapy
from scrapy.spiders import Rule, CrawlSpider

from mzitu_spider.items import MzituSpiderItem


class mzitu_spider(CrawlSpider):
    name = 'mzitu'

    start_urls = {
        'http://www.mzitu.com/all/'
    }

    rules = {
        Rule(LinkExtractor(allow=r'http://www.mzitu.com/\d{1,6}', deny=r'http://www.mzitu.com/\d{1,6}/\d{1,6}'),
             callback='parse_item', follow=True)
    }
    img_urls = []

    def parse_item(self, response):
        item = MzituSpiderItem()
        total_pages = response.xpath('/html/body/div[2]/div[1]/div[4]/a[5]/span/text()').extract()[0]  # str
        item['name'] = response.xpath('/html/body/div[2]/div[1]/h2/text()').extract()
        item['url'] = response.url  # 用来设置中间件里面浏览器请求头的referer参数,
        for i in range(1, int(total_pages)-1):
            page_url = response.url + '/' + str(i)  # 每页的图片地址
            yield scrapy.Request(page_url, callback=self.img_url)
        item['img_urls'] = self.img_urls
        yield item

    def img_url(self, response):
        img_urls = response.xpath("/html/body/div[2]/div[1]/div[3]/p/a/img/@src").extract()
        for img_url in img_urls:
            self.img_urls.append(img_url)