import uuid

import pika
from pika.delivery_mode import DeliveryMode
from pika.exceptions import UnroutableError, ChannelClosedByBroker
from pika.exchange_type import ExchangeType
import time


class RabbitMQ_Client(object):
    def __init__(self, host, port, vhost, user, password):
        self.host = host
        self.port = port
        self.vhost = vhost
        self.user = user
        self.password = password
        credentials = pika.PlainCredentials(self.user, self.password)  # mq用户名和密码
        # 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
        self.conn = pika.BlockingConnection(
            parameters=pika.ConnectionParameters(
                host=self.host,
                port=self.port,
                virtual_host=self.vhost,
                credentials=credentials,
                channel_max=5)
        )

    def __del__(self):
        self.conn.close()

    def create_exchange(self, exchange):
        channel = self.conn.channel()
        channel.exchange_declare(exchange=exchange, exchange_type=ExchangeType.direct, durable=True)

    def create_queue(self, queue):
        channel = self.conn.channel()
        channel.queue_declare(queue=queue, durable=True)

    def bind_exchange_queue(self, exchange, routing_key, queue):
        channel = self.conn.channel()
        channel.queue_bind(queue=queue, exchange=exchange, routing_key=routing_key)

    def producer(self, exchange, routing_key, body):
        channel = self.conn.channel()
        channel.confirm_delivery()
        pika.spec.BasicProperties(delivery_mode=DeliveryMode.Persistent, priority=12, correlation_id=uuid.uuid1(),
                                  message_id=uuid.uuid4(), timestamp=time.time())
        try:
            channel.basic_publish(exchange=exchange,
                                  routing_key=routing_key,
                                  body=body,
                                  properties=None,
                                  mandatory=True)
        except ChannelClosedByBroker as e1:
            print("channel closed by broker:", type(e1), e1)
        except UnroutableError as e2:
            print("router error:", e2)

    def consumer(self, queue, callback_fun):
        channel = self.conn.channel()
        channel.basic_consume(queue, callback_fun, False)
        channel.start_consuming()


if __name__ == '__main__':
    uat_rabbit_mq = {
        'rabbit_mq_host': 'k8s-lb.uat.homecredit.cn',
        'rabbit_mq_port': 5041,
        'rabbit_mq_vhost': 'ssdd_product_yuxin',
        'rabbit_mq_user': 'ssdd_user',
        'rabbit_mq_pawd': 'ssdd_pass'
    }
    rabbitmq_client = RabbitMQ_Client(uat_rabbit_mq['rabbit_mq_host'], uat_rabbit_mq['rabbit_mq_port'],
                                      uat_rabbit_mq['rabbit_mq_vhost'], uat_rabbit_mq['rabbit_mq_user'],
                                      uat_rabbit_mq['rabbit_mq_pawd'])

    rabbitmq_client.producer('ex.py', 'key.ex.py.to.q.py', b'asdfafssfd')
    rabbitmq_client.consumer("q_py",
                             lambda channel, deliver, msg_properties, msg_body: channel.basic_ack(deliver.delivery_tag,
                                                                                                  False))
