from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
from pymongo import MongoClient


def roll(browser):
    """
    设置自动滚动 滚动条
    """
    browser.execute_script('window.scrollTo(0, 1500)')
    sleep(1)
    browser.execute_script('window.scrollTo(0, 2000)')
    sleep(1)
    browser.execute_script('window.scrollTo(0, 2500)')
    sleep(1)
    browser.execute_script('window.scrollTo(0, 3000)')
    sleep(1)
    browser.execute_script('window.scrollTo(0, 3500)')
    sleep(1)
    browser.execute_script('window.scrollTo(0, 4000)')
    sleep(1)


def write_mongodb(page_source):
    html = etree.HTML(page_source)
    title = html.xpath('//div[@class="title-row "]/a/@title')
    price = html.xpath('//strong/text()')

    maijia = html.xpath('//a[@class="seller-link"]/text()')
    conn = MongoClient('mongodb://localhost:27017')
    db = conn.test
    collection = db.taobao
    dict = {}

    for i in range(0, len(title)):
        dict['title %d' % i] = title[i]
        dict['price %d' % i] = price[i]
        dict['卖家数量 %d' % i] = maijia[i]
        # print(i)
    collection.insert(dict)

    # print(title)
    # print(price)
    # print(maijia)


def main():
    option = webdriver.ChromeOptions()  # 设置浏览器不开启运行
    option.add_argument("headless")
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('https://s.taobao.com/search?')
    search_input = browser.find_element_by_id('q')  # 获取输入框
    for keyword in ['空调', '洗衣机', '电脑', '情趣品']:
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.ENTER)
        # print(browser.page_source)
        next_page = browser.find_element_by_xpath('//a[@class="J_Ajax num icon-tag"]')
        total_pages = browser.find_element_by_xpath('//div[@class="total"]')
        a = total_pages.text
        b = int(a[2:4])
        # print(browser.page_source)
        roll(browser)
        write_mongodb(browser.page_source)
        next_page.click()
        sleep(5)
        # print(browser.page_source)
        roll(browser)
        write_mongodb(browser.page_source)
        for i in range(b-2):
            next_page = browser.find_elements_by_xpath('//a[@class="J_Ajax num icon-tag"]')[1]
            next_page.click()
            sleep(5)
            roll(browser)

            # print(browser.page_source)
            write_mongodb(browser.page_source)
        search_input = browser.find_element_by_id('q')
        search_input.clear()

    sleep(2)
    browser.close()


if __name__ == '__main__':
    main()