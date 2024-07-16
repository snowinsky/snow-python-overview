import psycopg2

ssdd_pg_host = "pdc04postgrespayment.cn.prod"
ssdd_pg_port = 5002
ssdd_pg_user = "hccn_jack_ji"
ssdd_pg_pawd = "fBV_lKSM"
ssdd_pg_database = "db_pay"

def execute_query_sql(sql:str, sql_param_dict:dict)->list:
    db = psycopg2.connect(host=ssdd_pg_host,
                          port=ssdd_pg_port,
                          user=ssdd_pg_user,
                          password=ssdd_pg_pawd,
                          database=ssdd_pg_database)
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