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
        for obj in bucket.objects.filter(Prefix="newmetalog"):
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
    # print("请输入要下载的日志的日期格式yyyy-MM-dd：")
    # log_date_str = input()
    # print("请输入要下载日志的服务名，就是rancher上的node的前半段名字：")
    # app_name = input()
    #
    # print(f"你是想要下载{app_name}在{log_date_str}这一天的日志，是吗？【y/n】")
    # yes_no = input()
    # if yes_no != 'y':
    #     exit()
    #
    # print("开始查找日志，因为日志超级多，查找速度会有点慢。。。。等。。。。耐着性子等。。。。。")
    # s3resource = Boto3_S3_Resource()
    # l = s3resource.list_log_file(bucket_name='k8s-log', log_date_yyyyMMdd=log_date_str, app_name=app_name)
    # print("多谢等待，终于有结果了", l)
    # if not l:
    #     raise FileNotFoundError("没找到log日志文件，联系运维组帮忙看一下吧")
    #
    # for f in l:
    #     s3resource.download('k8s-log', f)

    print("请输入要下载的日志的key：")
    log_file_key = input()
    s3resource = Boto3_S3_Resource()
    s3resource.download('k8s-log', log_file_key)