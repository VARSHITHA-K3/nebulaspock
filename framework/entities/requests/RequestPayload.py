from EntityProperties import EntityProperties
from Entities import Entities

class RequestPayload:
    systemRequests:list = SystemRequest()
    properties:list = EntityProperties()
    entities: list = Entities()

print(properties.isidentifier)
