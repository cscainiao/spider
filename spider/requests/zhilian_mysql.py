
import re
from time import sleep
from threading import Thread

import pymysql
import requests


def save_mysql(zhiweilianjie, jobname, response, gongshilianjie, company, salary, time, address):
    db = pymysql.connect(host='10.7.152.57', user='root', password='123456', port=3306, db='spider', charset='utf8')
    cursor = db.cursor()

    try:
        cursor.execute('insert into zhilian values (%(zhiweilianjie)s, %(jobname)s, %(response)s, '
                       '%(gongshilianjie)s, %(company)s, %(salary)s, %(time)s, %(address)s)',
                       {'zhiweilianjie':zhiweilianjie,
                        'jobname': jobname,
                        'response': response,
                        'gongshilianjie': gongshilianjie,
                        'company': company,
                        'salary': salary,
                        'time': time,
                        'address': address
                        }
                       )
        db.commit()
    except:
        db.rollback()
    db.close()


def get_page(city, keyword, page):
    params = {
        'jl': city,  # 搜索城市
        'kw': keyword,  # 搜索关键词
        'isadv': 0,
        'p': page          # 搜索页数
    }
    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 "
    }
    response = requests.get(url, params=params, headers=headers)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except:
        return None


def parse_page_write_mysql(html):
    pattern = re.compile(
                         '<td class="zwmc".*? href="(.*?)" target="_blank">(.*?)</a>.*?' # 职位链接和职位名称
                         '<td.*? class="fk_lv".*?<span>(.*?)</span>.*?'                  # 反馈率
                         '<td class="gsmc".*? href="(.*?)" target="_blank">(.*?)</a>.*?'  # 公司链接和公司名称  
                         '<td class="zwyx">(.*?)</td>.*?'                                # 月薪
                         '<td class="gzdd">(.*?)</td>.*?'                                # 地点  
                         '<td class="gxsj".*?<span>(.*?)</span>.*?'                      # 发布时间
                         , re.S)
    data = re.findall(pattern, html)
    _, _, _, _,_, _, _, _,_, _, *items = data
    for item in items:

        jobname = item[1]
        jobname = jobname.replace('<b>', '')
        jobname = jobname.replace('</b>', '')
        zhiweilianjie = item[0]
        response = item[2]
        gongshilianjie = item[3]
        company = item[4]
        salary = item[5]
        address = item[6]
        time = item[7]
        save_mysql(zhiweilianjie, jobname, response, gongshilianjie, company, salary, time, address)


def main(city, keyword, page):
    for i in range(page):
        html = get_page(city, keyword, i)
        Thread(target=parse_page_write_mysql, args=(html,)).start()
        print(i)
        sleep(0.5)


if __name__ == '__main__':
    main('成都', '会计', 20)  # 可更换搜索条件
