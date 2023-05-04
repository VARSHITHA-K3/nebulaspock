from redis import Redis


class NebulaRedisCommon():
     def __init__(self, servers: str, port: str):
          self.redisSever = Redis(servers, port, retry_on_timeout=True)
