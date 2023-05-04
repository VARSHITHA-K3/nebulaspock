from Interface.Consumer import RabbitMQConsumer
from Server.Servercom import RabbitMQConsumer
consumer = RabbitMQConsumer(host='localhost', queue_name='my_queue')
consumer.consumeMessage()