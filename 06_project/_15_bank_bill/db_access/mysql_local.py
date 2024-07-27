import pymysql

ssdd_mysql_host = "127.0.0.1"
ssdd_mysql_port = 3306
ssdd_mysql_user = "root"
ssdd_mysql_pawd = "123456"
ssdd_mysql_database = "app_recon"


def execute_query_sql(sql: str, sql_param_dict: dict) -> list:
    db = pymysql.connect(host=ssdd_mysql_host,
                         port=ssdd_mysql_port,
                         user=ssdd_mysql_user,
                         password=ssdd_mysql_pawd,
                         database=ssdd_mysql_database)
    try:
        cursor = db.cursor()
        cursor.execute(sql, sql_param_dict)
        return [a for a in cursor.fetchall()]
    finally:
        db.close()


def execute_update_sql(sql: str, sql_param_tuple: tuple) -> int:
    db = pymysql.connect(host=ssdd_mysql_host,
                         port=ssdd_mysql_port,
                         user=ssdd_mysql_user,
                         password=ssdd_mysql_pawd,
                         database=ssdd_mysql_database)
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


def execute_insert_sql(sql: str, sql_param_tuple: tuple):
    db = pymysql.connect(host=ssdd_mysql_host,
                         port=ssdd_mysql_port,
                         user=ssdd_mysql_user,
                         password=ssdd_mysql_pawd,
                         database=ssdd_mysql_database)
    try:
        with db.cursor() as cursor:
            cursor.execute(sql, sql_param_tuple)
            db.commit()
            print('cursor.lastrowid=', cursor.lastrowid)
            return cursor.rowcount, cursor.lastrowid
    except Exception as e:
        print('db error', e)
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    insert_sql = '''insert 
                    t_local_credit_bank_debit(
                        credit_date,credit_channel,credit_acct,credit_amt,
                        debit_date, debit_channel, debit_acct, debit_amt,
                        recon_balance
                    ) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    insert_sql_param = (20230101, 'aasdf', 'asdfasdf', 154525, None, None, None, None, None)

    execute_insert_sql(insert_sql, insert_sql_param)

