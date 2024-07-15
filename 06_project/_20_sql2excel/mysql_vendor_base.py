# !/usr/bin/python3
import pymysql
import datetime
import date_util

vendor_mysql_host = "pdc02mysqlvendorproxy.cn.prod"
vendor_mysql_port = 3133
vendor_mysql_user = "app_vendor"
vendor_mysql_pawd = "Hns_0u8ys1Sa"
vendor_mysql_database = "db_vendor"


def selectFromVendorMySql(sql: str, sql_param_dict: dict) -> tuple:
    # 打开数据库连接
    db = pymysql.connect(host=vendor_mysql_host,
                         port=vendor_mysql_port,
                         user=vendor_mysql_user,
                         password=vendor_mysql_pawd,
                         database=vendor_mysql_database)
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





if __name__ == '__main__':
    sql = '''
    SELECT *
        FROM t_deduct_response_info bres
        WHERE bres.cdate >= %(start_date)s
        AND bres.cdate < %(end_date)s
        limit 3
    '''

    sql_param_dict = {
        "start_date": date_util.datetime_util.string2datetime('20240705', '%Y%m%d'),
        "end_date": date_util.datetime_util.datetime_plus_days(date_util.datetime_util.string2datetime('20240705', '%Y%m%d'), 1)
    }
    print(sql_param_dict)
    sql_result = selectFromVendorMySql(sql, sql_param_dict)
    print(sql_result)
