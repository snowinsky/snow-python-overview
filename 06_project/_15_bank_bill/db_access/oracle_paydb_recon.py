import os
import platform
import oracledb

d = None  # default suitable for Linux
if platform.system() == "Darwin" and platform.machine() == "x86_64":  # macOS
    d = os.environ.get("HOME") + ("/Downloads/instantclient_19_8")
elif platform.system() == "Windows":
    d = r"D:/download/instantclient-basic-windows.x64-19.23.0.0.0dbru/instantclient_19_23"
oracledb.init_oracle_client(lib_dir=d)

user = 'app_reconcile'
pawd = 'rEJvMi6#9tdhafe'
db_url = 'DBPAYCN.CN.PROD:1521/SRV_PAYDBCN.HOMECREDIT.CN'

def execute_query_sql(sql:str, sql_param_dict:dict)->list:
    with oracledb.connect(user=user, password=pawd, dsn=db_url) as connection:
        with connection.cursor() as cursor:
            l = []
            for r in cursor.execute(statement=sql, parameters=sql_param_dict):
                l.append(r)
            return l