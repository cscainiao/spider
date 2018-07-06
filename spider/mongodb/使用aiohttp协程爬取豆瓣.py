import json

import aiohttp
import asyncio

from pymongo import MongoClient


class DoubanMovie():
    def __init__(self):
        self.tag_url = 'https://movie.douban.com/j/search_tags?type=movie&source='
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        self.tags = []
        self.movie_url = 'http://movie.douban.com/j/search_subjects?type=movie&tag=%s&sort=recommend&page_limit=20&page_start=0'
        conn = MongoClient('mongodb://localhost:27017')
        db = conn.test
        self.collection = db.collection

    async def get_html_info(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.tag_url, verify_ssl=False, headers=self.headers) as response:
                tags = await response.json()
                self.tags = tags['tags']

        for tag in self.tags:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.movie_url % tag, verify_ssl=False, headers=self.headers) as response:
                    data = await response.json()
                    # print(data)
                    for movie_info in data['subjects']:
                        await self.insert_mongodb(movie_info)

    async def insert_mongodb(self, data):
        self.collection.insert_one(data)

    def run(self):
        loop = asyncio.get_event_loop()
        task = asyncio.wait([self.get_html_info()])
        loop.run_until_complete(task)


if __name__ == '__main__':
    dbm = DoubanMovie()
    dbm.run()

