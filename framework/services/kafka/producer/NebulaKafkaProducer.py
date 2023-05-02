import json

from kafka import KafkaProducer
from framework.interfaces.producer.NebulaProducer import NebulaProducer



class NebulaKafkaProducer(NebulaProducer):
     def __init__(self, servers):
          self.servers = servers

     def serializer(self,message):
          return json.dumps(message).encode('utf-8')
     
     def sendMessage(self, topic, message):
          producer = KafkaProducer(bootstrap_servers=[self.servers],
                                   value_serializer=self.serializer)
          producer.send(topic, message)
     
