import lxml
from bs4 import BeautifulSoup
import ssl
from urllib import parse
import urllib.request


def main(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 "
    }

    content = ssl._create_unverified_context()  # https
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req, context=content)
    return res.read().decode('utf-8')


if __name__ == '__main__':
    # city = input('请输入城市:')
    # job = input('请输入职位:')
    search = parse.urlencode({'jl': '成都', 'kw': 'python'})
    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?' + search
    html = main(url)
    soup = BeautifulSoup(html, 'lxml')

    for tag in soup.select('td[class="gsmc"] a'):
        a = tag.get_text()
        print(a)

