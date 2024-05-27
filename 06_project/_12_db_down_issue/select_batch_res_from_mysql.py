vendor_mysql_sql = '''
SELECT *
FROM t_deduct_response_info bres
WHERE bres.cdate >= %(start_date)s
AND bres.cdate < %(end_date)s 
AND bres.request_id = %(request_id)s
'''

vendor_mysql_host = "pdc02mysqlvendorproxy.cn.prod"
vendor_mysql_port = 3133
vendor_mysql_user = "app_vendor"
vendor_mysql_pawd = "Hns_0u8ys1Sa"
vendor_mysql_database = "db_vendor"

# !/usr/bin/python3
import pymysql
from datetime import datetime as dt
import datetime


def selectFromMySql(request_id, audit_date_str):
    start_date = dt.strptime(audit_date_str, '%Y%m%d')
    end_date = start_date + datetime.timedelta(days=1)
    sql_param_map = {
        'request_id': request_id,
        'start_date': start_date,
        'end_date': end_date
    }

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
        cursor.execute(vendor_mysql_sql, sql_param_map)
        # 使用 fetchone() 方法获取单条数据.
        return cursor.rowcount > 0, cursor.fetchall()
    finally:
        # 关闭数据库连接
        db.close()

if __name__ == '__main__':
    print(selectFromMySql("00540841-7cc2-4193-b217-414aee73e0f4", '20240527'))