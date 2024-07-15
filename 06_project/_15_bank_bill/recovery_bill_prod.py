all_bank = '''
BOC
ICBC
CCB
ABC
CIB
CMB
PSBC
'''


# pw = getpass.getpass(f'Enter password for {un}@{cs}: ')
# print(pw)

db_result = '''
|TRUNC(B.TRADE_TIME)    |COUNT(DISTINCTB.CREATOR)|BANK_LIST               |
|-----------------------|------------------------|------------------------|
|2023-12-31 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-01-01 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-01-02 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-03 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-04 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-05 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-06 00:00:00.000|4                       |ABC,BOC,CCB,ICBC        |
|2024-01-07 00:00:00.000|4                       |ABC,BOC,CCB,ICBC        |
|2024-01-08 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-09 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-10 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-11 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-12 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-13 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-01-14 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-01-15 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-16 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-17 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-18 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-19 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-20 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-01-21 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-01-22 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-23 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-24 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-25 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-26 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-27 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-01-28 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-01-29 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-30 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-01-31 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-01 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-02 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-03 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-02-04 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-05 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-06 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-07 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-08 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-09 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-10 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-02-11 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-02-12 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-02-13 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-02-14 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-02-15 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-02-16 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-02-17 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-02-18 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-19 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-20 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-21 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-22 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-23 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-24 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-02-25 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-02-26 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-27 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-28 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-02-29 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-01 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-02 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-03-03 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-03-04 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-05 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-06 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-07 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-08 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-09 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-03-10 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-03-11 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-12 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-13 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-14 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-15 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-16 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-03-17 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-03-18 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-19 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-20 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-21 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-22 00:00:00.000|5                       |ABC,BOC,CCB,CIB,ICBC    |
|2024-03-23 00:00:00.000|3                       |ABC,CCB,ICBC            |
|2024-03-24 00:00:00.000|4                       |ABC,BOC,CCB,ICBC        |
|2024-03-25 00:00:00.000|5                       |ABC,BOC,CCB,CIB,ICBC    |
|2024-03-26 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-27 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-28 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-29 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-03-30 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-03-31 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-04-01 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-02 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-03 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-04 00:00:00.000|4                       |ABC,BOC,CMB,ICBC        |
|2024-04-05 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-04-06 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-04-07 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-08 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-09 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-10 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-11 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-12 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-13 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-04-14 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-04-15 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-16 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-17 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-18 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-19 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-20 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-04-21 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-04-22 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-23 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-24 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-25 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-26 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-27 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-04-28 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-29 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-04-30 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-05-01 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-05-02 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-05-03 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-05-04 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-05-05 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-05-06 00:00:00.000|5                       |ABC,BOC,CIB,CMB,ICBC    |
|2024-05-07 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-05-08 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-05-09 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-10 00:00:00.000|3                       |BOC,CMB,ICBC            |
|2024-05-11 00:00:00.000|3                       |BOC,CMB,ICBC            |
|2024-05-12 00:00:00.000|3                       |BOC,CMB,ICBC            |
|2024-05-13 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-14 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-15 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-16 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-17 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-18 00:00:00.000|2                       |CMB,ICBC                |
|2024-05-19 00:00:00.000|3                       |BOC,CMB,ICBC            |
|2024-05-20 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-21 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-22 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-23 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-24 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-25 00:00:00.000|3                       |BOC,CMB,ICBC            |
|2024-05-26 00:00:00.000|3                       |BOC,CMB,ICBC            |
|2024-05-27 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-28 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-29 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-30 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-05-31 00:00:00.000|4                       |BOC,CIB,CMB,ICBC        |
|2024-06-01 00:00:00.000|3                       |BOC,CMB,ICBC            |
|2024-06-02 00:00:00.000|3                       |BOC,CMB,ICBC            |
|2024-06-03 00:00:00.000|5                       |BOC,CCB,CIB,CMB,ICBC    |
|2024-06-04 00:00:00.000|5                       |BOC,CCB,CIB,CMB,ICBC    |
|2024-06-05 00:00:00.000|5                       |BOC,CCB,CIB,CMB,ICBC    |
|2024-06-06 00:00:00.000|5                       |BOC,CCB,CIB,CMB,ICBC    |
|2024-06-07 00:00:00.000|4                       |BOC,CCB,CIB,ICBC        |
|2024-06-08 00:00:00.000|3                       |BOC,CCB,ICBC            |
|2024-06-09 00:00:00.000|3                       |BOC,CCB,ICBC            |
|2024-06-10 00:00:00.000|3                       |BOC,CCB,ICBC            |
|2024-06-11 00:00:00.000|4                       |BOC,CCB,CIB,ICBC        |
|2024-06-12 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-06-13 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-06-14 00:00:00.000|5                       |ABC,BOC,CIB,CMB,ICBC    |
|2024-06-15 00:00:00.000|4                       |ABC,BOC,CMB,ICBC        |
|2024-06-16 00:00:00.000|5                       |ABC,BOC,CCB,CMB,ICBC    |
|2024-06-17 00:00:00.000|5                       |ABC,BOC,CIB,CMB,ICBC    |
|2024-06-18 00:00:00.000|5                       |ABC,BOC,CIB,CMB,ICBC    |
|2024-06-19 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-06-20 00:00:00.000|5                       |ABC,BOC,CIB,CMB,ICBC    |
|2024-06-21 00:00:00.000|5                       |ABC,BOC,CIB,CMB,ICBC    |
|2024-06-22 00:00:00.000|3                       |ABC,CMB,ICBC            |
|2024-06-23 00:00:00.000|4                       |ABC,BOC,CMB,ICBC        |
|2024-06-24 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-06-25 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
|2024-06-26 00:00:00.000|6                       |ABC,BOC,CCB,CIB,CMB,ICBC|
'''

all_bank_set = set(filter(lambda a: len(a) > 0, all_bank.split('\n')))
un = 'APP_RECONCILE'
cs = 'DBCN00C1PY.CN.INFRA:1521/CN00C1PY.CN.INFRA'
pw = 'Tres$u4ex3KL'

user = 'app_reconcile'
pawd = 'rEJvMi6#9tdhafe'
db_url = 'DBPAYCN.CN.PROD:1521/SRV_PAYDBCN.HOMECREDIT.CN'

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

def check_bill_load_status(start_date, end_date):
    with oracledb.connect(user=user, password=pawd, dsn=db_url) as connection:
        with connection.cursor() as cursor:
            sql_get_current_bill_status = '''
                SELECT
                    trunc(b.TRADE_TIME),
                    count(DISTINCT b.CREATOR),
                    listagg(DISTINCT b.CREATOR, ',')  AS bank_list
                FROM
                    T_RECON_S_DETAIL_B b
                WHERE
                    b.TRADE_TIME >= to_date(:start_date, 'yyyymmdd')
                    and b.TRADE_TIME < to_date(:end_date, 'yyyymmdd')
                GROUP BY
                    trunc(b.TRADE_TIME)
                ORDER BY trunc(b.TRADE_TIME)
                '''
            sql_parameter_map = {'start_date': start_date, 'end_date': end_date}
            l = []
            print(sql_get_current_bill_status, sql_parameter_map)
            for r in cursor.execute(statement=sql_get_current_bill_status, parameters=sql_parameter_map):
                l.append(r)

            return l

def re_load_bill(recon_date, bank_code):
    print(f're-load the bill for {bank_code} on {recon_date} in process......')
    res = requests.get(url=f"https://reconcile-bank-web.prod.hccn/load/{bank_code}/{recon_date}", verify=False)
    # res = requests.get(url=f"http://localhost:8080/load/{bank_code}/{recon_date}", verify=False)
    print(res.text)

def re_load_bill_by_bankacct(recon_date, bank_code, bank_acct):
    print(f're-load the bill for {bank_code}.{bank_acct} on {recon_date} in process......')
    # res = requests.get(url=f"https://reconcile-bank-web.prod.hccn/load/{bank_code}/{recon_date}", verify=False)
    res = requests.get(url=f"http://localhost:8080/load/{bank_code}/{recon_date}/{bank_acct}", verify=False)
    print(res.text)
def recover_lack_bank_on_date():
    l = check_bill_load_status('20230101', '20240101')
    print(l)
    for one_day in l:
        recon_date_str = datetime.datetime.strftime(one_day[0], '%Y%m%d')
        recon_bank_cnt = int(one_day[1])
        recon_bank_code = str(one_day[2]).split(',')
        print(recon_date_str, recon_bank_cnt, recon_bank_code)
        if recon_bank_cnt == 7:
            continue

        tasks = [re_load_bill(recon_date_str, bc) for bc in all_bank_set.difference(set(recon_bank_code))]
        # break

def recover_lack_bank_on_date_range(bank_code):
    start_date = datetime.datetime(2024, 7, 8)
    end_date = datetime.datetime(2024, 7, 9)

    time_delta = end_date - start_date

    for i in range(time_delta.days):
        curr_date = start_date + datetime.timedelta(days=i)
        curr_date_str =curr_date.strftime('%Y%m%d')
        re_load_bill(curr_date_str, bank_code)

if __name__ == '__main__':
    # all_bank_set = set(filter(lambda a: len(a) > 0, all_bank.split('\n')))
    # cur_set = set(['ICBC', 'CCB'])
    # print(all_bank_set.difference(cur_set))

    # main()
    
    # check_bill_load_status('20240101', '20240101')

    recover_lack_bank_on_date_range('PSBC')

    #re_load_bill('20240628', 'PSBC')
