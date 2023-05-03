import pika
import json
from Interface.preducer import RabbitMQProducer
class RabbitMQProducer:
    def __init__(self, host, queue_name):
        self.host = host
        self.queue_name = queue_name

    def sendMessage(self, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name)
        channel.basic_publish(exchange='', routing_key=self.queue_name, body=json.dumps(message))
        print("Message sent to the queue")
        connection.close()
