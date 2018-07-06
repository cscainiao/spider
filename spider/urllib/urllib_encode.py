import ssl
import urllib.request
from urllib import parse


def main(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 "
    }

    content = ssl._create_unverified_context()  # https

    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req, context=content)
    return res.read().decode('utf-8')


if __name__ == '__main__':
    msg = input('请输入搜索信息')
    search = parse.urlencode({'wd': msg})
    url = 'https://www.baidu.com/s?%s' % search
    print(main(url))