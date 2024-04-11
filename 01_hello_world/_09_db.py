#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import mysql.connector #ModuleNotFoundError: No module named 'MySQLdb' 表示这个module没安装

# 
mysqlconn = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="123456"   # 数据库密码
)

print(mysqlconn)

mycursor = mysqlconn.cursor()
 
mycursor.execute("SHOW DATABASES")
 
for x in mycursor:
  print(x)