import ssl
import urllib.request
from bs4 import BeautifulSoup
from lxml import etree


def decode_html(html, charsets=('utf-8', 'gbk')):   # 解码
    page_html = ''
    for charset in charsets:
        try:
            page_html = html.decode(charset)
            break
        except:
            print('解码出错')
    return page_html


def get_html(url):    # 获取源码
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 "
    }
    content = ssl._create_unverified_context()

    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req, context=content)
    page_html = decode_html(res.read())
    return page_html


def main(url):
    page_html = get_html(url)
    # soup = BeautifulSoup(page_html, 'lxml')
    html = etree.HTML(page_html)
    url1 = html.xpath('//div[@class="col335 left"]//li//a/@href')
    result1 = html.xpath('//div[@class="col335 left"]//li//a/text()')
    url2 = html.xpath('//div[@class="col335 right"]//li//a/@href')
    result2 = html.xpath('//div[@class="col335 right"]//li//a/text()')
    url3 = html.xpath('//div[@class="col370 left"]//li//a/@href')
    result3 = html.xpath('//div[@class="col370 left"]//li//a/text()')
    basketball_urls = url1 + url2 + url3
    titles = result1 + result2 + result3
    # print(urls)
    for basketball_url in basketball_urls:

        basketball_html = get_html(basketball_url)
        # print(basketball_html)

        basketball_html_xpath = etree.HTML(basketball_html)
        content = basketball_html_xpath.xpath('//article')
        print(content)


if __name__ == '__main__':

    url = 'http://sports.sohu.com/lanqiu.shtml'
    main(url)