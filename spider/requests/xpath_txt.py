from time import sleep

import requests
from lxml import etree


def get_page(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 "
    }
    res = requests.get(url, headers=headers)
    try:
        if res.status_code == 200:
            return res.text
        return None
    except:
        return None


def xpath_html(htmls):
    html = etree.HTML(htmls)
    return html


def main(url):
    html1 = get_page(url)
    xpath_html1 = xpath_html(html1)
    url1 = xpath_html1.xpath('//div[@class="col335 left"]//li//a/@href')
    url2 = xpath_html1.xpath('//div[@class="col335 right"]//li//a/@href')
    url3 = xpath_html1.xpath('//div[@class="col370 left"]//li//a/@href')
    basketball_urls = url1 + url2 + url3
    for basketball_url in basketball_urls:
        sleep(0.5)
        basketball_html = get_page(basketball_url)
        basketball_html_xpath = xpath_html(basketball_html)
        content = basketball_html_xpath.xpath('//article//p/text()')
        if content:
            title = basketball_html_xpath.xpath('//title/text()')
            with open('shouhu.txt', 'a', encoding='utf-8') as f:
                f.write('\n' + str(title) + '\n')

            for i in content:
                with open('shouhu.txt', 'a', encoding='utf-8') as f:
                    f.write('\n' + str(i))


if __name__ == '__main__':
    url = 'http://sports.sohu.com/lanqiu.shtml'
    main(url)