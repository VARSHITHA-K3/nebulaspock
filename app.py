

import random
import time
from framework.services.rabbitMQ.consumer.NebulaRabbitMQConsumer import NebulaRabbitMQConsumer
from framework.services.redis.consumer.NebulaRedisConsumer import NebulaRedisConsumer


if __name__ == "__main__":
    consumer = NebulaRedisConsumer("localhost","6379")
    topic_name = "test"
    message = consumer.consumeMessage(topic_name)
    time_to_sleep = random.randint(1, 1000)
    time.sleep(time_to_sleep)