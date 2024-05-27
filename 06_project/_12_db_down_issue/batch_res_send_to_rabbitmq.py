import pika
import json

def send_res_json_to_router(res_json_msg_list):
    credentials = pika.PlainCredentials('jetpay_ssdd_user', '2pHEJYHF')  # mq用户名和密码
    # 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='lb02-rmq02.homecreditcfc.cn', port=5673, virtual_host='payment_jetcollect', credentials=credentials))
    channel = connection.channel()
    # 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
    # channel.exchange_declare(exchange='ex.deduct', durable=True, exchange_type='fanout')

    for res_msg in res_json_msg_list:
        # msg_dic = {"requestId": "03cd9e5b-cb7a-4eef-9849-c20ab2375923",
        #            "responseTime": "2023-12-03 08:41:08",
        #            "returnCode": "0000",
        #            "returnInfo": "交**",
        #            "vendorRequestId": "1MEVPC48382587",
        #            "vendorRequestTime": "2023-12-03 08:41:08",
        #            "vendorResponseId": "",
        #            "vendorResponseTime": "2023-12-03 08:41:08",
        #            "debitedAmount": 31452,
        #            "batchFileUrl": "null",
        #            "batchFileName": "null",
        #            "matchingResult": "null",
        #            "vendorResponseSettlementId": "null"}
        message = json.dumps(res_msg)
        # 向队列插入数值 routing_key是队列名。delivery_mode = 2 声明消息在队列中持久化，delivery_mod = 1 消息非持久化。routing_key 不需要配置
        channel.basic_publish(exchange='ex.deduct', routing_key='key.deduct.resp', body=message,
                              properties=pika.BasicProperties(delivery_mode=2))
        print("send msg complete", res_msg["requestId"])
    connection.close()


if __name__ == '__main__':
    send_res_json_to_router([])