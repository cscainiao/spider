
import requests


def get_data(city, kd, pg):
    url = 'https://www.lagou.com/jobs/positionAjax.json?'
    params = {
        'city': city,
        'needAddtionalResult': 'false',
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 ",
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput='
    }
    pages = [page for page in range(1, pg+1)]

    for page in pages:
        if page == 1:
            data = {
                'first': 'true',
                'pn': page,
                'kd': kd
            }
        else:
            data = {
                'first': 'false',
                'pn': page,
                'kd': kd
            }

        res = requests.post(url, headers=headers, params=params, data=data)
        print(res.text)


get_data('成都','python',3)