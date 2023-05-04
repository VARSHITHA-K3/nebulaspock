import pika
import json
from Interface.Consumer import RabbitMQConsumer
class RabbitMQConsumer:
    def __init__(self, host, queue_name):
        self.host = host
        self.queue_name = queue_name

    def callback(self, ch, method, properties, body):
        print("Received message: ", json.loads(body))

    def consumeMessage(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name)
        channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)
        print("Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()
