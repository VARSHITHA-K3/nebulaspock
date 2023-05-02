
import json
from framework.interfaces.producer.NebulaProducer import NebulaProducer
from services.kafka.producer.NebulaKafkaProducer import NebulaKafkaProducer


if __name__ == '__main__':
    topic_name = input("Enter topic name: ")
    employee_string = input("Enter topic payload: ")
    #employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'
    json_object = json.loads(employee_string)
    #check new data type
    #print(type(json_object))

    #print(msg)

    producer:NebulaProducer = NebulaKafkaProducer('localhost:9092')
    producer.sendMessage(topic_name,json_object)
