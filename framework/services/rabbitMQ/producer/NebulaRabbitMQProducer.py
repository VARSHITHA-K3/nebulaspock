import json

from framework.interfaces.producer.NebulaProducer import NebulaProducer
from framework.services.rabbitMQ.utilities.NebulaRabbitMQCommon import NebulaRabbitMQCommon


class NebulaRabbitMQProducer(NebulaProducer):
    def __init__(self, servers: str, port: str, username: str, password: str, exchangename: str, vhost: str):
        self.exchangeName = exchangename
        self.rabbitMQCommon: NebulaRabbitMQCommon = NebulaRabbitMQCommon(
            servers=servers, userName=username, password=password, port=port, vhost=vhost)

    def serializer(self, message):
        return json.dumps(message).encode('utf-8')

    def sendMessage(self, topic, message):
        
        channel = self.rabbitMQCommon.createExchange(exchangeName=self.exchangeName)
        self.rabbitMQCommon.createQueue(queueName=topic, routingKey="*."+topic+".*",
                                        exchangeName=self.exchangeName)
        channel.basic_publish(exchange=self.exchangeName,
                                         routing_key="*."+topic+".*", body=self.serializer(message))

        channel.close()


if __name__ == "__main__":
    producer: NebulaRabbitMQProducer = NebulaRabbitMQProducer(
        "localhost", "user", "Nebula=2020", "nebula.exchange")
    payload: any = []
    payload["name"] = "employee-1"
    payload["employeeid"] = "N144112"
    payload["email"] = "name@name.com"
    producer.sendMessage("sample.post", json.dumps(payload))
