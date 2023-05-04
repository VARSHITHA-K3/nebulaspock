

import random
import time
from framework.services.rabbitMQ.consumer.NebulaRabbitMQConsumer import NebulaRabbitMQConsumer


if __name__ == "__main__":
    consumer = NebulaRabbitMQConsumer("localhost","5672","user","Nebula=2020","nebula.exchange","nebula.vhost")
    topic_name = "test"
    message = consumer.consumeMessage(topic_name)
    time_to_sleep = random.randint(1, 1000)
    time.sleep(time_to_sleep)