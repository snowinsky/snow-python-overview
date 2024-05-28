import pika
import json
from concurrent.futures import ThreadPoolExecutor

prod_rabbit_mq = {
    'rabbit_mq_host': 'lb02-rmq02.homecreditcfc.cn',
    'rabbit_mq_port': 5673,
    'rabbit_mq_vhost': 'payment_jetcollect',
    'rabbit_mq_user': 'jetpay_ssdd_user',
    'rabbit_mq_pawd': '2pHEJYHF'
}

uat_rabbit_mq = {
    'rabbit_mq_host': 'k8s-lb.uat.homecredit.cn',
    'rabbit_mq_port': 5041,
    'rabbit_mq_vhost': 'ssdd_product_base',
    'rabbit_mq_user': 'ssdd_user',
    'rabbit_mq_pawd': 'ssdd_pass'
}

profile = {'prod': prod_rabbit_mq, 'uat': uat_rabbit_mq}

profile_active = 'uat'

rabbit_mq_product_exchange = 'ex.deduct'
rabbit_mq_product_routingkey = 'key.deduct.resp'


def send_res_json_to_router(res_json_msg_list):
    '''
    输入参数必须是一个列表类型，其中数据为字典类型，格式如下
    {"requestId": "03cd9e5b-cb7a-4eef-9849-c20ab2375923",
                   "responseTime": "2023-12-03 08:41:08",
                   "returnCode": "0000",
                   "returnInfo": "交**",
                   "vendorRequestId": "1MEVPC48382587",
                   "vendorRequestTime": "2023-12-03 08:41:08",
                   "vendorResponseId": "",
                   "vendorResponseTime": "2023-12-03 08:41:08",
                   "debitedAmount": 31452,
                   "batchFileUrl": "null",
                   "batchFileName": "null",
                   "matchingResult": "null",
                   "vendorResponseSettlementId": "null"}
    :param res_json_msg_list:
    :return:
    '''
    # print("connection to rabbitmq", profile[profile_active]['rabbit_mq_host'])
    credentials = pika.PlainCredentials(profile[profile_active]['rabbit_mq_user'], profile[profile_active]['rabbit_mq_pawd'])  # mq用户名和密码
    # 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
    with pika.BlockingConnection(
            parameters=pika.ConnectionParameters(
                host=profile[profile_active]['rabbit_mq_host'],
                port=profile[profile_active]['rabbit_mq_port'],
                virtual_host=profile[profile_active]['rabbit_mq_vhost'],
                credentials=credentials,
                channel_max=5)
    ) as connection:
        with ThreadPoolExecutor(max_workers=3) as t:
            for res_msg in res_json_msg_list:
                t.submit(send_rabbitmq_msg, connection, res_msg)
        t.shutdown()


def send_rabbitmq_msg(connection, msg):
    channel = connection.channel()
    message = json.dumps(msg)
    # 向队列插入数值 routing_key是队列名。delivery_mode = 2 声明消息在队列中持久化，delivery_mod = 1 消息非持久化。routing_key 不需要配置
    channel.basic_publish(exchange=rabbit_mq_product_exchange, routing_key=rabbit_mq_product_routingkey,
                          body=message,
                          properties=pika.BasicProperties(delivery_mode=2))
    print("send msg complete", msg["requestId"])


if __name__ == '__main__':
    send_res_json_to_router([])
