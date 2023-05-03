from datetime import datetime
from AuditTrails import AuditTrails
from framework.entities.enum.Operation import Operation
from framework.entities.enum.RequestStatus import RequestStatus

class SystemRequest:
    id:int = None
    isprocessed:bool = None
    requestor:str = None
    requesttype:str = None
    requestStatus:RequestStatus()
    requestjson:str = None
    requesteddate:str = datetime.now()
    requestcomments:str = None
    entityid:int = None
    entitytype:str = None
    createondate:str = datetime.now()
    modifyondate:str = datetime.now()
    objectid:int = None
    requestactions:str = None
    requestoperation:Operation()
    originalrequest:bool = None
    forcebroadcast:bool = None
    updatecount:int = None
    auditTrails:list = AuditTrails()
