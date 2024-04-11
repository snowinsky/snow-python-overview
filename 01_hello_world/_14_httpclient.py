#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
##################  get  ######################
resp = requests.get("https://wwww.baidu.com")
print(type(resp))
print(dict(resp.headers))

print(resp.text)
##################  post  ######################
headers = {'User-Agent': 'Mozilla/5.0'}  # 设置请求头
params = {'key1': 'value1', 'key2': 'value2'}  # 设置查询参数
bodyData = {'username': 'example', 'password': '123456'}  # 设置请求体
response = requests.post('https://www.runoob.com', headers=headers, params=params, data=bodyData)

print(response.status_code)