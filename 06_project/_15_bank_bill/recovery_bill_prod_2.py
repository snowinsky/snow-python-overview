import os
import platform

import oracledb
import requests
import datetime
import asyncio

d = None  # default suitable for Linux
if platform.system() == "Darwin" and platform.machine() == "x86_64":  # macOS
    d = os.environ.get("HOME") + ("/Downloads/instantclient_19_8")
elif platform.system() == "Windows":
    d = r"D:/download/instantclient-basic-windows.x64-19.23.0.0.0dbru/instantclient_19_23"
oracledb.init_oracle_client(lib_dir=d)


user = 'app_reconcile'
pawd = 'rEJvMi6#9tdhafe'
db_url = 'DBPAYCN.CN.PROD:1521/SRV_PAYDBCN.HOMECREDIT.CN'


def get_bill_load_error_records(start_date, end_date):
    with oracledb.connect(user=user, password=pawd, dsn=db_url) as connection:
        with connection.cursor() as cursor:
            sql_get_error_trade_status = '''
            SELECT
                b.id,
                b.TRADE_TIME AS trade_date,
                b.TRADE_STATUS ,
                b.HCC_ACCOUNT AS bank_acct,
                b.CREATOR AS bank_code
            FROM
                T_RECON_S_DETAIL_B b
            WHERE
                b.TRADE_STATUS = 'E'
                AND b.TRADE_TIME >= to_date(:start_date, 'yyyymmdd')
                AND b.TRADE_TIME < to_date(:end_date, 'yyyymmdd')
            '''
            sql_parameter_map = {'start_date': start_date, 'end_date': end_date}
            l = []
            print(sql_get_error_trade_status, sql_parameter_map)
            for r in cursor.execute(statement=sql_get_error_trade_status, parameters=sql_parameter_map):
                l.append(r)
            return l

def call_api_reload_bill(recon_date):
    print(f're-load the bill for all bank code on {recon_date} in process......')
    res = requests.get(url=f"https://reconcile-bank-web.prod.hccn/re-load/error-trade-status/{recon_date}", verify=False)
    # res = requests.get(url=f"http://localhost:8080/load/{bank_code}/{recon_date}", verify=False)
    print(res.text)
def recovery_bill(start_date, end_date):
    l = get_bill_load_error_records(start_date, end_date)
    date_list = set([a[1] for a in l])
    for ba in date_list:
        call_api_reload_bill(ba.strftime('%Y%m%d'))



if __name__ == '__main__':
    recovery_bill('20240714', '20240716')
    