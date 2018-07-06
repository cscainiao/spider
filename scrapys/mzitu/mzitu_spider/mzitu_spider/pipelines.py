# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class MzituSpiderPipeline(ImagesPipeline):
    """
    图片下载管道, 需要安装pillow
    """

    def file_path(self, request, response=None, info=None):
        """
        :param request: 每一个图片下载管道请求
        :param response:
        :param info:
        :return: 每套图的分类目录
        """
        item = request.meta['item']
        folder = item['name']

        image_guid = request.url.split('/')[-1]
        filename = u'full/{0}/{1}'.format(folder, image_guid)
        return filename

    def get_media_requests(self, item, info):

        for img_url in item['img_urls']:
            referer = item['url']
            # sleep(0.1)
            yield scrapy.Request(img_url, meta={'item': item, 'referer': referer})  # meta 传递参数用

    def item_completed(self, results, item, info):           # 固定写法
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

