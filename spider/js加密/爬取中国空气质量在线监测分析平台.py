# 需要安装PyExecJS   pip install PyExecJS
# 通过分析 JavaScript 并进行反混淆，然后用 Python 模拟运行 JavaScript 的方式实现了数据抓取

import execjs
import requests

print(execjs.get().name)

# Init environment
node = execjs.get()

# Params
method = 'GETCITYWEATHER'
city = '北京'
type = 'HOUR'
start_time = '2018-01-25 00:00:00'
end_time = '2018-01-25 23:00:00'

# Compile javascript
file = 'encryption.js'
ctx = node.compile(open(file).read())

# Get params
js = 'getEncryptedData("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)
params = ctx.eval(js)  # 加密传给服务器的参数

api = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
response = requests.post(api, data={'d': params})  # 返回加密的结果


js = 'decodeData("{0}")'.format(response.text)  # 调用js的decodeData方法对结果解密
decrypted_data = ctx.eval(js)

print(decrypted_data)
