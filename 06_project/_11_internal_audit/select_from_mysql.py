ssdd_mysql_sql = '''
select
	req.contract_number ,
	dreq.request_time ,
	res.debited_amount,
	dreq.id_vendor,
	v.code as vendor_code,
	res.vendor_batch_file_name,
	dres.vendor_request_id,
	dres.vendor_response_id
from
	db_ssdd.t_dd_request req
join db_ssdd.t_dd_response res
	on
	req.id = res.id_dd_request
join db_ssdd.t_deduct_request dreq 
	on
	dreq.id_dd_request = req.id
join db_ssdd.t_deduct_response dres
	on
	dres.id_deduct_request = dreq.id
join db_ssdd.t_vendor v on
	dreq.id_vendor = v.id
where
	req.contract_number = %(contract_nbr)s
	and req.cdate >= %(start_date)s
	and req.cdate < %(end_date)s
	and res.return_code = '0000'
	and dres.return_code = '0000'
'''

ssdd_mysql_host = "pdc04mysqlssdd.cn.prod"
ssdd_mysql_port = 3233
ssdd_mysql_user = "app_ssdd"
ssdd_mysql_pawd = "Kjs6G_ks7fs"
ssdd_mysql_database = "db_ssdd"

# !/usr/bin/python3
import pymysql
from datetime import datetime as dt
import datetime


def selectFromMySql(contract_nbr, audit_date_str):
    start_date = dt.strptime(audit_date_str, '%Y%m%d')
    end_date = start_date + datetime.timedelta(days=1)
    sql_param_map = {
        'contract_nbr': contract_nbr,
        'start_date': start_date,
        'end_date': end_date
    }

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
        cursor.execute(ssdd_mysql_sql, sql_param_map)
        # 使用 fetchone() 方法获取单条数据.
        return cursor.rowcount > 0, cursor.fetchall()
    finally:
        # 关闭数据库连接
        db.close()
