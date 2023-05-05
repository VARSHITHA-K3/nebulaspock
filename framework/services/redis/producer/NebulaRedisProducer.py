import json

from framework.interfaces.producer.NebulaProducer import NebulaProducer
from framework.services.redis.utilities.NebulaRedisCommon import NebulaRedisCommon


class NebulaRedisProducer(NebulaProducer):
    def __init__(self, servers: str, port: str):
        self.redisCommon = NebulaRedisCommon(servers=servers, port=port)

    def serializer(self, message):
        return json.dumps(message).encode('utf-8')

    def sendMessage(self, topic, message):
        self.redisCommon.redisSever.xadd(topic, message)
