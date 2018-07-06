import ssl
import urllib.request

url = 'http://www.baidu.com'
headers = {
    'User-Agent': "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 "
}

content = ssl._create_unverified_context()

re = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(re, context=content)
print(res.read().decode('utf-8'))