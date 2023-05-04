import json
from framework.interfaces.consumer.NebulaConsumer import NebulaConsumer
from framework.services.rabbitMQ.utilities.NebulaRabbitMQCommon import NebulaRabbitMQCommon


class NebulaRabbitMQConsumer(NebulaConsumer):
     def __init__(self, servers: str, port: str, username: str, password: str, exchangename: str, vhost: str):
        self.exchangeName = exchangename
        self.rabbitMQCommon: NebulaRabbitMQCommon = NebulaRabbitMQCommon(
            servers=servers, userName=username, password=password, port=port, vhost=vhost)

     

     def consumeMessage(self, topic,messageCallBack):
         channel = self.rabbitMQCommon.createExchange(exchangeName=self.exchangeName)
         self.rabbitMQCommon.createQueue(queueName=topic, routingKey="*."+topic+".*",
                                        exchangeName=self.exchangeName)
         channel.basic_consume(queue=topic, on_message_callback=messageCallBack, auto_ack=True)
         channel.start_consuming()



