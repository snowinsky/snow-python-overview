from s3_sdk_resource import Boto3_S3_Resource
from datetime import date

if __name__ == '__main__':
    print("请输入要下载的日志的日期格式yyyy-MM-dd：")
    log_date_str = input()
    print("请输入要下载日志的服务名，就是rancher上的node的前半段名字：")
    app_name = input()

    print(f"你是想要下载{app_name}在{log_date_str}这一天的日志，是吗？【y/n】")
    yes_no = input()
    if yes_no != 'y':
        exit()


    print("开始查找日志，因为日志超级多，查找速度会有点慢。。。。等。。。。耐着性子等。。。。。")
    s3resource = Boto3_S3_Resource()
    l = s3resource.list_log_file(bucket_name='k8s-log', log_date_yyyyMMdd=log_date_str, app_name=app_name)
    print("多谢等待，终于有结果了", l)
    if not l:
        raise FileNotFoundError("没找到log日志文件，联系运维组帮忙看一下吧")

    for f in l:
        s3resource.download('k8s-log', f)