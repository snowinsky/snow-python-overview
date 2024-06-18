import requests
import os
import datetime
import time

in_base_path = 'D:/IN-SQL/in-306508'

def download(batch_name):
    download_url = f"https://jetpay-proxy-batch-runtime-icbc-tj-api.prod.hccn/vendor/proxy/batch/file/download/{batch_name}/REQ/DATA"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    res = requests.get(url=download_url, auth=('proxy', 'vendor'),
                       verify=False, headers=headers)
    if res.status_code == 200:
        file_folder = os.path.join(in_base_path, datetime.date.today().strftime('%Y-%m-%d'))
        os.makedirs(file_folder, exist_ok=True)
        file_name = os.path.join(file_folder, batch_name + '.TXT')
        if os.path.exists(file_name):
            os.remove(file_name)
        with open(file_name, 'wb') as f:
            f.write(res.content)
            time.sleep(1)
        return file_name


def rename(batch_name):
    new_batch_name = str(batch_name).replace('JX20240616500', 'JX20240616510')
    old_batch_file = os.path.join(in_base_path, datetime.date.today().strftime('%Y-%m-%d'), batch_name + '.TXT')
    new_batch_file = os.path.join(in_base_path, datetime.date.today().strftime('%Y-%m-%d'), new_batch_name + '.TXT')
    new_file = open(new_batch_file, 'w', encoding='GBK')
    with open(old_batch_file, 'r', encoding='GBK') as old_file:
        for line in old_file:
            if batch_name in line:
                new_file.write(line.replace(batch_name, new_batch_name))
            else:
                new_file.write(line)
        new_file.flush()
        new_file.close()

    return new_batch_file

def upload(batch_name):
    new_batch_name = str(batch_name).replace('JX20240616500', 'JX20240616510')
    upload_url = f'https://jetpay-proxy-batch-runtime-icbc-tj-api.prod.hccn/vendor/proxy/batch/file/upload?batchName={batch_name}&dataType=REQ&fileType=DATA'
    new_batch_file = os.path.join(in_base_path, datetime.date.today().strftime('%Y-%m-%d'), new_batch_name + '.TXT')
    new_file = open(new_batch_file, 'rb')
    print(upload_url)
    print(new_batch_file)
    res = requests.post(url=upload_url, auth=('proxy', 'vendor'),
                  verify=False, files={'file':new_file})
    print(res.text)


# !/usr/bin/python3
import pymysql

vendor_mysql_host = "pdc01mysqlvendorproxy.cn.prod"
vendor_mysql_port = 3133
vendor_mysql_user = "app_vendor"
vendor_mysql_pawd = "Hns_0u8ys1Sa"
vendor_mysql_database = "DB_VENDOR"
def update_db():
    db = pymysql.connect(host=vendor_mysql_host,
                         port=vendor_mysql_port,
                         user=vendor_mysql_user,
                         password=vendor_mysql_pawd,
                         database=vendor_mysql_database)

    mysql_sql_001 = '''
    UPDATE 
      t_vendor_trx_batch b 
    SET 
      b.process_status = 1, 
      b.path_req_file = REPLACE(
        b.path_req_file, 'JX2024061650', 
        'JX2024061651'
      ), 
      b.batch_name = REPLACE(
        b.batch_name, 'JX2024061650', 'JX2024061651'
      ), 
      b.editor = 'IN-306509' 
    WHERE 
      b.channel_code = 'icbc_batch' 
      AND b.cdate >= '2024-06-16' 
      AND b.batch_name LIKE 'JX2024061650%' 
      AND b.process_status NOT IN (1, 7, 8)
    '''

    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(mysql_sql_001)
        # update, insert, delete需要commit
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        return cursor.rowcount > 0
    finally:
        # 关闭数据库连接
        db.close()

def execute_by_id(batch_id):
    exe_url = f'https://jetpay-proxy-batch-runtime-icbc-tj-api.prod.hccn/vendor/proxy/batch?batchId={batch_id}'
    res = requests.post(exe_url, auth=('proxy','vendor'),verify=False)
    print(res.text)


if __name__ == '__main__':
    '''
    JX20240616500001
    ...
    JX20240616500069
    '''
    for a in range(2,70):
        if a in (2,14,15,16,17):
            print("skip", a)
            continue
        batch_name = 'JX202406165' + str(a).rjust(5, '0')
        #file_name = download(batch_name)
        #new_file_name = rename(batch_name)
        #upload(batch_name)
        # break

    for b in range(109501255901, 109501255969):
        execute_by_id(str(b))