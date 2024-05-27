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

    def list_buckets(self):
        buckets = [bucket['Name'] for bucket in self.s3_client.list_buckets()['Buckets']]
        print(buckets)
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

    def download(self):
        resp = self.s3_client.get_object(
            Bucket='Aaa',
            Key='test'
        )
        with open('/Users/xx/Desktop/test_1.txt', 'wb') as f:
            f.write(resp['Body'].read())

    def list_objects_in_bucket(self, bucket_name):
        response = self.s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                key = obj['Key']
                print(key)

if __name__ == "__main__":
    # boto3
    cephs3_boto3 = CephS3BOTO3()
    cephs3_boto3.list_buckets()
    cephs3_boto3.list_objects_in_bucket('k8s-log')
