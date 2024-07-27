import os
import platform
import oracledb

d = None  # default suitable for Linux
if platform.system() == "Darwin" and platform.machine() == "x86_64":  # macOS
    d = os.environ.get("HOME") + ("/Downloads/instantclient_19_8")
elif platform.system() == "Windows":
    d = r"D:/download/instantclient-basic-windows.x64-19.23.0.0.0dbru/instantclient_19_23"
oracledb.init_oracle_client(lib_dir=d)

user = 'app_mini_plum'
pawd = 'JaJs9NSNM_ks0'
db_url = 'DBCN00C1.CN.INFRA:1521/CN00C1.CN.INFRA'

def execute_query_sql(sql:str, sql_param_dict:dict)->list:
    with oracledb.connect(user=user, password=pawd, dsn=db_url) as connection:
        with connection.cursor() as cursor:
            l = []
            for r in cursor.execute(statement=sql, parameters=sql_param_dict):
                l.append(r)
            return l


def execute_update_sql(sql:str, sql_param_tuple:tuple):
    with oracledb.connect(user=user, password=pawd, dsn=db_url) as db:
        try:
            with db.cursor() as cursor:
                cursor.execute(sql, sql_param_tuple)
                db.commit()
                return cursor.rowcount
        except Exception as e:
            print('db error', e)
            db.rollback()
        finally:
            db.close()

def batch_execute_update_sql(sql:str, sql_param_tuple_list:list):
    with oracledb.connect(user=user, password=pawd, dsn=db_url) as db:
        try:
            with db.cursor() as cursor:
                cursor.executemany(sql, sql_param_tuple_list)
                db.commit()
                return cursor.rowcount
        except Exception as e:
            print('db error', e)
            db.rollback()
        finally:
            db.close()



if __name__ == '__main__':
    print(execute_query_sql('select * from bank_account', None))