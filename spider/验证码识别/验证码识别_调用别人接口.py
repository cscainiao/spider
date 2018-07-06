import urllib.request
import ssl
from base64 import b64encode
from urllib import parse


host = 'https://302307.market.alicloudapi.com'
path = '/ocr/captcha'
# method = 'POST'
appcode = 'bebba1739a3a49c9b512a32db32b325c'
querys = ''
bodys = {}
url = host + path


def img_base64():
    """
    图片编码成base64文件
    """
    with open('123.png', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')

    return data

data = img_base64()
# print(data)


bodys['image'] = '''data:image/jpeg;base64,%s''' % data
bodys['type'] = '''1001'''
post_data = parse.urlencode(bodys).encode('utf-8')
request = urllib.request.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
# //根据API的要求，定义相对应的Content-Type
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
ctx = ssl._create_unverified_context()
response = urllib.request.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)