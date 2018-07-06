from time import sleep

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

fenleis = browser.find_elements_by_xpath('//ul[@class="service-bd"]/li/a')

for fenlei in fenleis:
    fenlei.click()
    browser.switch_to_window(browser.window_handles[1])
    sleep(5)
    browser.close()
    browser.switch_to_window(browser.window_handles[0])
    sleep(5)