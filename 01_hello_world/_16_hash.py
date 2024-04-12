#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 哈希（Hash）是一种将任意长度的输入数据映射为固定长度输出数据的算法。
# hashlib 模块提供了常见的哈希算法的实现，如 MD5、SHA-1、SHA-256 等。

import hashlib

for x in dir(hashlib):
    print(x)
    
print('aa1' in ['aa', 'bb'])

aa = 2342.11
print(type(aa))