import os
import time

from boto3.session import Session
import boto3


# 新版本boto3

class CephS3BOTO3():

    def __init__(self):
        access_key = 'VCLOGVYM8UUHS0UXVJCF'
        secret_key = 'fPNgN55AV9juwZCAKj98ApLZCF44F99c8lLEEujd'
        self.session = Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        self.url = 'http://10.29.44.2:8080'
        self.s3_client = self.session.client('s3', endpoint_url=self.url)
        self.download_base_path = "D:/data/applogs/"

    def list_buckets(self):
        buckets = [bucket['Name'] for bucket in self.s3_client.list_buckets()['Buckets']]
        return buckets

    def create_bucket(self):
        # 默认是私有的桶
        self.s3_client.create_bucket(Bucket='hy_test')
        # 创建公开可读的桶
        # ACL有如下几种"private","public-read","public-read-write","authenticated-read"
        self.s3_client.create_bucket(Bucket='hy_test', ACL='public-read')

    def upload(self):
        resp = self.s3_client.put_object(
            Bucket="Aaa",  # 存储桶名称
            Key='test',  # 上传到
            Body=open("/Users/xx/Desktop/test.txt", 'rb').read()
        )
        print(resp)
        return resp

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

    def list_objects_in_bucket(self, bucket_name):
        response = self.s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            return [{'file_path': obj['Key'],
                     'file_size': obj['Size']} for obj in response['Contents']]


if __name__ == "__main__":

    while True:
        times = time.time()
        print(f'sssss={times}', end='\r\n')

    # boto3
    cephs3_boto3 = CephS3BOTO3()
    # bucket_name_list = cephs3_boto3.list_buckets()
    # print(bucket_name_list)
    # obj_list = cephs3_boto3.list_objects_in_bucket('k8s-log')
    # print(obj_list)
    cephs3_boto3.download('k8s-log', 'es/20230117/cn-app-bank-vendor-2023.01.05.json')
