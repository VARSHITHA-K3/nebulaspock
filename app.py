

import json
import random
import time
import types
from framework.services.kafka.consumer.NebulaKafkaConsumer import NebulaKafkaConsumer
from framework.services.rabbitMQ.consumer.NebulaRabbitMQConsumer import NebulaRabbitMQConsumer
from framework.services.redis.consumer.NebulaRedisConsumer import NebulaRedisConsumer


def callback(ch, method, properties, body):
    if isinstance(body,bytes):
        print("correct")
        body = json.loads(body)
    elif isinstance(body,dict):
        print("dict")
    
    print("type of payload: ", type(body))
    print("Received message: ", body)


if __name__ == "__main__":
    consumer = NebulaRabbitMQConsumer("localhost","5672","user","Nebula=2020","nebula.exchange","nebula.vhost")
    topic_name = "test"
    message = consumer.consumeMessage(topic_name, callback)
    time_to_sleep = random.randint(1, 1000)
    time.sleep(time_to_sleep)
