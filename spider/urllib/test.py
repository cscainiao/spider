
import threading

# def finbo(n):  # 斐波那契
#     a, b = 0, 1
#     print(a)
#     for i in range(n):
#             a, b = b, a+b
#             print(a)
#
#
# finbo(5)
import time

"""
生成器实现斐波那契
def f(n):
    a, b, c = 0, 1, 0
    while c < n:
        yield a
        a, b = b, a+b
        c += 1

result = f(10)
for i in range(10):
    print(result.__next__())

"""



"""
多线程
class myThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)  # 初始化threading.Thread
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('开启线程: ' + self.name)
        thread_lock.acquire()
        print_time(self.name, self.counter, 4)
        thread_lock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


thread_lock = threading.Lock()  # 给线程加互斥锁, 让一个线程的锁释放后另一个线程才能访问第一个线程访问的资源
threads = []


thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 1)
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)


for t in threads:
    t.join()
print("退出主线程")

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()

browser.get('https://www.baidu.com')
input = browser.find_element_by_id('kw')
input.send_keys('Python')
input.send_keys(Keys.ENTER)
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
print(browser.current_url)
print(browser.get_cookies())
print(browser.page_source)
