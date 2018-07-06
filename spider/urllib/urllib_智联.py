import re
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
    city = input('请输入城市:')
    job = input('请输入职位:')
    search = parse.urlencode({'jl': city, 'kw': job})
    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?' + search
    html = main(url)
    job_nums = re.findall(r'<em>(.*?)</em>', html)
    print(job_nums)
    print('城市:%s 职位: %s 需求量:%s' % (city, job, job_nums[0]))