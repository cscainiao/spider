from base64 import b64encode

import requests


def img_base64():
    """
    图片编码成base64文件
    """
    with open('123.png', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    return data


def get_yanzhengma(url):
    appcode = 'bebba1739a3a49c9b512a32db32b325c'
    headers = {
        'Authorization': 'APPCODE ' + appcode,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    data = {
        'image': 'data:image/jpeg;base64,%s' % img_base64(),
        'type': '1001'
    }
    response = requests.post(url=url, data=data, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None


def main(url):
    content = get_yanzhengma(url)['data']['captcha']
    print(content)


if __name__ == '__main__':
    url = 'https://302307.market.alicloudapi.com/ocr/captcha'
    main(url)