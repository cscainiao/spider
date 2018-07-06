from time import sleep

import requests
import threading


def get_tags():
    url_tag = 'https://movie.douban.com/j/search_tags?type=movie&tag=%E7%BB%8F%E5%85%B8&source='
    tags = requests.get(url_tag).json()['tags']
    return tags


g = []


def get_page(tag):

    global g
    params = {
        'type': 'move',
        'tag': tag,
        'sort': 'recommend',
        'page_limit': 20,
        'page_start': 20
    }
    url = 'https://movie.douban.com/j/search_subjects?'
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 "
    }
    res = requests.get(url, params=params, headers=headers).json()
    g.append(res)
    return res


def main():
    tags = get_tags()
    print(tags)
    # for tag in tags:
    #     html = get_page(tag)
    #     print(html)
    for tag in tags:
        t = threading.Thread(target=get_page, args=(tag, )).start()


if __name__ == '__main__':
    main()
    sleep(20)
    print()