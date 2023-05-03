import json
import pika
from interfaces.producer.NebulaProducer import NebulaProducer


class NebulaRabbitMQProducer(NebulaProducer):
     def __init__(self, host, port):
          self.host = host
          self.port = port
          self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
          self.channel = self.connection.channel()
          self.channel.exchange_declare(exchange='logs', exchange_type='fanout')

     def serializer(self, message):
          return json.dumps(message).encode('utf-8')

     def sendMessage(self, message):
          self.channel.basic_publish(exchange='logs', routing_key='', body=self.serializer(message))
          print("Sent message: %r" % message)

     def close(self):
          self.connection.close()