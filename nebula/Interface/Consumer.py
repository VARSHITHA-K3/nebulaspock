from abc import ABC, abstractmethod

class RabbitMQConsumer(ABC):
    @abstractmethod
    def consumeMessage(self):
        pass