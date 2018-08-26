import requests


url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D3%26q%3D%E9%9D%92%E7%BE%8A%E5%8C%BA%26t%3D0&page_type=searchall'

res = requests.get(url=url)
data = res.json()

card_group = data['data']['cards'][-1]['card_group']
for i in card_group:
    user = i['user']
    id = user['id']
    screen_name = user['screen_name']
    verified = user['verified']
    verified_type = user['verified_type']
    print(id)
    print(screen_name)
    print(verified)
    print(verified_type)
    print('--------------------')
