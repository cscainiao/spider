from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from lxml import etree

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

input = browser.find_element_by_id('q')
# print(input_first)
input.send_keys('洗衣机')
input.send_keys(Keys.ENTER)
wait = WebDriverWait(browser, 10)
# print(browser.page_source)


ele = etree.HTML(browser.page_source)
# print(ele)
title = ele.xpath('//div[@class="title-row "]/a/@title')
print(title)
price = ele.xpath('//strong/text()')
print(price)
browser.back()

browser.close()