import json
from interfaces.producer.NebulaProducer import NebulaProducer
from kafka import KafkaProducer



class NebulaKafkaProducer(NebulaProducer):
     def __init__(self, servers):
          self.servers = servers

     def serializer(self,message):
          return json.dumps(message).encode('utf-8')
     
     def sendMessage(self, topic, message):
          producer = KafkaProducer(bootstrap_servers=[self.servers],
                                   value_serializer=self.serializer)
          producer.send(topic, message)
     
