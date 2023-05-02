import random
from framework.interfaces.consumer.NebulaConsumer import NebulaConsumer
from services.kafka.consumer.NebulaKafkaConsumer import NebulaKafkaConsumer
import time

if __name__ == '__main__':
    topic_name = input("Enter topic name: ")
    consumer:NebulaConsumer = NebulaKafkaConsumer('localhost:9092')
    print("NebulaConsumer Topic Name=%s"%(topic_name))
    message = consumer.consumeMessage(topic_name)
    time_to_sleep = random.randint(1, 11)
    time.sleep(time_to_sleep)
       