from Interface.preducer import RabbitMQProducer
from Server.Serverapp import RabbitMQProducer
import json
if __name__ == '__main__':
    # Create a producer and send a message
    producer = RabbitMQProducer(host='localhost', queue_name='my_queue')
    message_string = input("Enter a message: ")
    message = {'message': message_string}
    producer.sendMessage(message)