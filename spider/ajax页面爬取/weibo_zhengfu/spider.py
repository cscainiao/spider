import random
import re
from time import sleep
import requests
import csv
import pandas as pd

from pymongo import MongoClient


def get_page(keyword, page):
    params = {
        'containerid': '100103type%3D3%26q%3D{}%26t%3D0'.format(keyword),
        'page_type': 'searchall',
        'page': page
    }
    url = 'https://m.weibo.cn/api/container/getIndex?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Referer': 'https://m.weibo.cn/p/searchall?containerid=100103type%3D1%26q%3D%E9%9D%92%E7%BE%8A%E5%8C%BA',
    }
    try:
        response = requests.get(url, params=params, headers=headers, timeout=20)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        pass


def get_areas():
    data = pd.read_csv('df_2861_gaode_geo_spider.csv')
    areas = data.loc[:, 'full_name']
    return areas


def save_data_mongdb(data):
    # conn = MongoCLient('mongodb://username:password@localhost:port')
    conn = MongoClient('mongodb://localhost:27017')
    db = conn.test
    collection = db.weibo_test
    dict = {}
    try:
        cards_group = data['data']['cards'][-1]['card_group']
        for card in cards_group:
            user = card['user']
            dict['user_id'] = user['id']
            dict['screen_name'] = user['screen_name']
            dict['verified'] = user['verified']
            dict['verified_type'] = user['verified_type']
            if dict['verified_type'] == 1:
                collection.update({'user_id': dict['user_id']}, {'$set': dict}, True)
    except:
        pass

def main():
    areas = get_areas()
    for area in areas:
        area_clear = area.replace('|', '')
        info = get_page(area_clear, 1)
        save_data_mongdb(info)
        print('已保存{}相关用户到mongdb中'.format(area_clear))
        sleep(0.3)


if __name__ == '__main__':
    main()
#
# a = get_page('成都市青羊区')
# print(a)