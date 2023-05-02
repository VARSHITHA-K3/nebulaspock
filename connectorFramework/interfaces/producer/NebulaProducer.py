
from abc import ABC, abstractmethod


class NebulaProducer(ABC):
    @abstractmethod
    def sendMessage(self, topic, message):
        pass