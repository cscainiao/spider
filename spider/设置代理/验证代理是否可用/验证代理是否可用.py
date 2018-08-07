import urllib
import urllib.request
import time

def validateIp(ip,port):
    #头文件
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent':user_agent}
    proxy = {'http':'http://%s:%s'%(ip,port)}

    #代理设置
    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    #请求网址
    validateUrl = 'https://www.baidu.com'
    req = urllib.request.Request(url=validateUrl,headers=headers)
    # 延时,等待反馈结果
    time.sleep(4)

    #判断结果
    try:
        res = urllib.request.urlopen(req)
        # 延时,等待反馈结果
        time.sleep(2)
        content = res.read()
        # 写入文件
        if content:
            print('is ok')
            with open('data2.txt', 'a') as wd:
                wd.write(ip + u':' + port + u'\n')
        else:
            # 未通过
            print('is not ok')
    except urllib.request.URLError as e:
        print(e.reason)


if __name__ == '__main__':
    with open('data.txt','r') as rd:
        iplist = rd.readlines()
        for ip in iplist:
            # print(ip.split(u':')[0])
            validateIp(ip.split(u':')[0],ip.split(u':')[1])