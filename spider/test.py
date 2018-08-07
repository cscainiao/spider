import requests

pages = [page for page in range(1, 3)]
print(pages)
url = 'https://www.lagou.com/jobs/positionAjax.json?'
params = {
    'city': '北京',
    'needAddtionalResult': 'false',

}
headers = {
        'User-Agent': "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 ",
        # 'Cookie': '_ga=GA1.2.1103330704.1531965623; user_trace_token=20180719100023-7f7ad7f4-8af7-11e8-9e68-525400f775ce; LGUID=20180719100023-7f7add1c-8af7-11e8-9e68-525400f775ce; index_location_city=%E6%88%90%E9%83%BD; LG_LOGIN_USER_ID=b7aeacb37f1106424dd46cf5247c466370bb683a5764b37898c47ee62ad94e44; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=2; WEBTJ-ID=20180806093425-1650cdeff82633-02f5880f9e9816-163d6952-1296000-1650cdeff839b1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532433014,1532510006,1533120547,1533519266; _gid=GA1.2.1619830488.1533519266; LGSID=20180806093425-da8ea6b9-9918-11e8-a339-5254005c3644; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Ks0000j8x7qYrYl4qvuQNgT_5hf6Y-clUh2iMdXYLVI0uSXQYWa5XbQ8mvgKHLmxUMSoJdwbPFYqGG0pt8pXpo6lBxwwiaZrCCHnrYDsNqC4GW2sEBGpZ-pASLn9b_xypBJABLjYAuTerSFcsM0hMwiOrsBQKNGa98YPJqj93Jr4WGQ1E6.DR_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsT8rZoG4XL6mEukmryZZjzsLT84MuYqhH-8zNqrw5Q9tSMj_qTr1x9tqvZul3xg1ONsSxH9vUnrS1j4etr1W9qxbGJIGHz3qis1f_U8MGlTB60.U1Yk0ZDqs2v4_sK9uZ745TaV8Un0mywkIjYz0ZKGm1Yk0Zfqs2v4VaRznQ5FVos0pyYqnWcd0ATqmhNsT1D0Iybqmh7GuZR0TA-b5Hc30APGujYznWm0UgfqnH0kPdtknjD4g1DsnWPxnH0YP7t1PW0k0AVG5H00TMfqnWbY0ANGujYzPWRzPNtkPjmvg1cvrH04g1cknH04g1cvrHcdg1csrHc40AFG5HcsP7tkPHR0UynqP1m1nW03PjRLg1Dsnj7xnNtknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5HR1n1mzP1bznfK8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0IZN15HDdn1Dsnj0dn1bknHfLnjbkrHDz0ZF-TgfqnHR1n1RkrHcvnHm3nsK1pyfquyP-myR1nWTsnj0snjbsnsKWTvYqn1czwW0kwHcvfWIDn19Af6K9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqnfKVmdqhThqV5HKxn7tsg1DsPjuxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7t1nH6vrH7xn0Ksmgwxuhk9u1Ys0AwWpyfqnWm3PjndPjRv0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqnHm0uhPdIjYs0AulpjYs0Au9IjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00mLFW5HR4PjRv%26ck%3D3769.7.80.317.149.438.295.367%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.1.0.1.303.0%26wd%3D%25E6%258B%2589%25E9%2592%25A9%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D2680%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_cd_5a8642_d2162e_%25E6%258B%2589%25E5%258B%25BE%2B%25E6%2588%2590%25E9%2583%25BD; _putrc=27DF895BA8047F24123F89F2B170EADC; JSESSIONID=ABAAABAAAFCAAEG702899603FFC9211E90AB273B1D67FCF; login=true; unick=%E7%86%8A%E6%98%9F; gate_login_token=93fb44df440e4d090809990756ceabe63c6fa03e5201592f56d6e57246e96157; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533519317; LGRID=20180806093517-f93826f7-9918-11e8-a339-5254005c3644; TG-TRACK-CODE=search_code; SEARCH_ID=0bfb041853f94223b286c63da2c5e233',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput='

    }

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'java'
}

res = requests.post(url,headers=headers,params=params,data=data)
# print(res.text)

