#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
'''
json在python中还是比较简单的，就是一个字符串，而转换成对象就是dictionary类型
双方互转只需要import json即可
'''
 
# Python 字典类型转换为 JSON 字符串
pyDicData = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'https://www.runoob.com'
}
 
json_str = json.dumps(pyDicData)
print(type(json_str))
print ("Python 原始数据：", repr(pyDicData))
print ("JSON 对象：", json_str)

# 将 JSON 字符串 转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])