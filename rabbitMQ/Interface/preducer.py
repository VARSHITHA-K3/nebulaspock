from abc import ABC, abstractmethod

class RabbitMQProducer(ABC):
    @abstractmethod
    def sendMessage(self, message):
        pass