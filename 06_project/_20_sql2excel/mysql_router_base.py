# !/usr/bin/python3
import pymysql
from datetime import datetime as dt
import datetime

ssdd_mysql_host = "pdc04mysqlssdd.cn.prod"
ssdd_mysql_port = 3233
ssdd_mysql_user = "app_ssdd"
ssdd_mysql_pawd = "Kjs6G_ks7fs"
ssdd_mysql_database = "db_ssdd"


def selectFromRouterMySql(sql: str, sql_param_dict: dict) -> tuple:
    # 打开数据库连接
    db = pymysql.connect(host=ssdd_mysql_host,
                         port=ssdd_mysql_port,
                         user=ssdd_mysql_user,
                         password=ssdd_mysql_pawd,
                         database=ssdd_mysql_database)
    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql, sql_param_dict)
        # 使用 fetchone() 方法获取单条数据.
        return cursor.fetchall()
    finally:
        # 关闭数据库连接
        db.close()
