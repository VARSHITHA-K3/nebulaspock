from EntityProperties import EntityProperties
from SystemRequest import SystemRequest
from Entities import Entities

class RequestPayload:
    systemRequests: SystemRequest()
    properties:list = EntityProperties()
    entities: list = Entities()
