

from framework.interfaces.consumer.NebulaConsumer import NebulaConsumer
from framework.services.redis.utilities.NebulaRedisCommon import NebulaRedisCommon


class NebulaRedisConsumer(NebulaConsumer):
    def __init__(self, servers: str, port: str):
        self.redisCommon = NebulaRedisCommon(servers=servers, port=port)

    def consumeMessage(self, topic,messageCallBack):
        last_id = 0
        sleep_ms = 5000
        while True:
            try:
                resp = self.redisCommon.redisSever.xread(
                    {topic: last_id}, count=1, block=sleep_ms
                )
                if resp:
                    key, messages = resp[0]
                    last_id, data = messages[0]
                    messageCallBack(None,None,None,data)
                    

            except ConnectionError as e:
                print("ERROR REDIS CONNECTION: {}".format(e))
