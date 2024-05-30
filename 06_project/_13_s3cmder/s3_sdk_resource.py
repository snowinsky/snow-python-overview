import boto3
import time
import os


class Boto3_S3_Resource(object):
    '''
    https://creodias.docs.cloudferro.com/en/latest/s3/How-to-access-private-object-storage-using-S3cmd-or-boto3-on-Creodias.html
    日志被存放在ceph上，需要s3cmd工具来拿取
    现在使用boto3这个sdk去尝试拿取对应的日志

    具体的boto3的doc可以参考https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
    分两种，一种是low-level的api，是.client('s3')这种，另一种是high-level的api，是.resource('s3')这种

    很奇怪的是，生产上用client的list_object获取不到足够的数据，而resource的object.filter居然可以，不知道为什么
    '''

    def __init__(self):
        access_key = 'VCLOGVYM8UUHS0UXVJCF'
        secret_key = 'fPNgN55AV9juwZCAKj98ApLZCF44F99c8lLEEujd'
        url = 'http://10.29.44.2:8080'
        self.s3_resource = boto3.resource('s3',
                                          aws_access_key_id=access_key,
                                          aws_secret_access_key=secret_key,
                                          endpoint_url=url)
        self.download_base_path = "D:/data/applogs/"

    def s3Resource(self):
        return self.s3_resource

    def list_objects_in_bucket(self, bucket_name='k8s-log', key_words=None):
        bucket = self.s3_resource.Bucket(bucket_name)
        if not bucket:
            raise FileNotFoundError(f"{bucket_name} not found in the s3")
        obj_key_list = []
        for obj in bucket.objects.filter("newmetalog"):
            obj_key = obj.key
            if key_words:
                if all(key_word in obj_key for key_word in key_words):
                    obj_key_list.append(obj_key)
                    return obj_key_list
            else:
                obj_key_list.append(obj_key)
        return obj_key_list

    def list_log_file(self, bucket_name='k8s-log', log_date_yyyyMMdd=None, app_name=None):
        return self.list_objects_in_bucket(bucket_name, key_words=('newmetalog', log_date_yyyyMMdd, app_name))

    def object(self, bucket_name, object_key):
        return self.s3_resource.Object(bucket_name, object_key)

    def download(self, bucket_name, object_key):
        block_size = 10240
        obj = self.s3_resource.Object(
            bucket_name,
            object_key
        )
        download_file_path = os.path.join(self.download_base_path, object_key)
        os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
        with open(download_file_path, 'wb') as f:
            obj.download_fileobj(f)
            print("download file complete", download_file_path)


if __name__ == '__main__':
    # print(all(k in 'metalog/2022/03/17/whdck8s004.cn.prod.log' for k in ('metalog', '2022/03/17')))
    s3resource = Boto3_S3_Resource()
    # obj_key_list = s3resource.list_objects_in_bucket(bucket_name='k8s-log',
    #                                                  key_words=('newmetalog', '2023/12/31', 'cashier-wechat-api'))
    # result:['newmetalog/2023/12/31/whdck8s059.cn.prod/data/logs/dddt/cashier-wechat-api/cashier-wechat-api--deployment--a-5dd486b647-2hgp5/logs/applicationlog/cashier-wechat-api.2023-12-29.log.tar.gz']
    # print(s3resource.object('k8s-log',
    #                         'newmetalog/2023/12/31/whdck8s059.cn.prod/data/logs/dddt/cashier-wechat-api/cashier-wechat-api--deployment--a-5dd486b647-2hgp5/logs/applicationlog/cashier-wechat-api.2023-12-29.log.tar.gz'))
    #
    # bucket = s3resource.s3_resource.Bucket('k8s-log')
    # obj = bucket.Object(
    #     'newmetalog/2023/12/31/whdck8s059.cn.prod/data/logs/dddt/cashier-wechat-api/cashier-wechat-api--deployment--a-5dd486b647-2hgp5/logs/applicationlog/cashier-wechat-api.2023-12-29.log.tar.gz')
    # print(obj)
    #
    # s3resource.download('k8s-log',
    #                     'newmetalog/2023/12/31/whdck8s059.cn.prod/data/logs/dddt/cashier-wechat-api/cashier-wechat-api--deployment--a-5dd486b647-2hgp5/logs/applicationlog/cashier-wechat-api.2023-12-29.log.tar.gz')

    bucket = s3resource.s3Resource().Bucket("k8s-log")

    i = 0
    obj_name_list = [obj.key for obj in bucket.objects.filter(Prefix="newmetalog")]
    print(obj_name_list)