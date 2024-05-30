import boto3
import os
import time


class Boto3_S3_Client(object):
    '''
    https://creodias.docs.cloudferro.com/en/latest/s3/How-to-access-private-object-storage-using-S3cmd-or-boto3-on-Creodias.html
    日志被存放在ceph上，需要s3cmd工具来拿取
    现在使用boto3这个sdk去尝试拿取对应的日志

    具体的boto3的doc可以参考https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
    分两种，一种是low-level的api，是.client('s3')这种，另一种是high-level的api，是.resource('s3')这种
    client的这种是一次只搜出一千个结果，不是都搜出来
    '''

    def __init__(self):
        access_key = 'VCLOGVYM8UUHS0UXVJCF'
        secret_key = 'fPNgN55AV9juwZCAKj98ApLZCF44F99c8lLEEujd'
        url = 'http://10.29.44.2:8080'
        self.s3_client = boto3.client('s3',
                                      aws_access_key_id=access_key,
                                      aws_secret_access_key=secret_key,
                                      endpoint_url=url)
        self.download_base_path = "D:/data/applogs/"

    def s3Client(self):
        return self.s3_client

    def list_buckets(self):
        return (n['Name'] for n in self.s3_client.list_buckets()['Buckets'])

    def list_objects_by_page(self, bucket_name='k8s-log', key_words=None):
        paginator = self.s3_client.get_paginator('list_objects_v2')

        with open("bank-vendor_jetpay__log.txt", 'w') as f:
            # Create a PageIterator from the Paginator
            page_iterator = paginator.paginate(Bucket=bucket_name, Prefix='newmetalog')
            obj_key_list = []
            page = 1
            for objs in page_iterator:
                print("批量处理中，，第", page, '页', end='\n')
                page += 1
                for obj in objs['Contents']:
                    obj_key = obj['Key']
                    if key_words:
                        if all(key_word in obj_key for key_word in key_words):
                            f.write(obj_key + '\n')
                            obj_key_list.append(obj_key)
                    else:
                        obj_key_list.append(obj_key)
            return obj_key_list

    def list_objects_in_bucket(self, bucket_name='k8s-log', key_words=None):
        objs = self.s3_client.list_objects_v2(Bucket=bucket_name, Prefix='newmetalog')
        obj_key_list = []
        for obj in objs['Contents']:
            obj_key = obj['Key']
            if key_words:
                if all(key_word in obj_key for key_word in key_words):
                    obj_key_list.append(obj_key)
                    return obj_key_list
            else:
                obj_key_list.append(obj_key)
        return obj_key_list

    def list_log_file(self, bucket_name='k8s-log', log_date_yyyyMMdd=None, app_name=None):
        return self.list_objects_in_bucket(bucket_name, key_words=('newmetalog', log_date_yyyyMMdd, app_name))

    def download(self, bucket_name, object_key):
        block_size = 10240
        resp = self.s3_client.get_object(
            Bucket=bucket_name,
            Key=object_key
        )
        file_size = resp['ContentLength']
        print('will download file_size', file_size)
        download_file_path = os.path.join(self.download_base_path, object_key)
        os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
        with open(download_file_path, 'wb') as f:
            downloaded_size = 0
            start = time.perf_counter()
            while True:
                buffer = resp['Body'].read(block_size)
                if not buffer:
                    break

                downloaded_size += len(buffer)
                f.write(buffer)

                progress = downloaded_size / file_size * 100
                print(f"Progress: {progress:.2f}%", end='\r')

            print("download file complete", download_file_path)


if __name__ == '__main__':
    # print(all(k in 'metalog/2022/03/17/whdck8s004.cn.prod.log' for k in ('metalog', '2022/03/17')))
    s3client = Boto3_S3_Client()
    # obj_key_list = s3resource.list_objects_in_bucket(bucket_name='k8s-log', key_words=('newmetalog', '2023/12/31', 'cashier-wechat-api'))
    # print(obj_key_list)
    # print(s3client.list_log_file('k8s-log','2023/12/31', 'cashier-wechat-api'))
    print(s3client.list_objects_by_page(bucket_name='k8s-log', key_words=('bank-vendor', 'jetpay')))

