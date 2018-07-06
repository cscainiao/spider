import requests


def get_page(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 "
    }
    res = requests.get(url, headers=headers)
    try:
        if res.status_code == 200:
            return res.content
        return None
    except:
        return None