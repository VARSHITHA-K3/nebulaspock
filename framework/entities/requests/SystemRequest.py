from datetime import datetime

class SystemRequest:
    id:int = None
    isprocessed:bool = None
    requestor:str = None
    requesttype:str = None
    requestStatus:requeststatus()
    requestjson:str = None
    requesteddate:str = datetime.now()
    requestcomments:str = None
    entityid:int = None
    entitytype:str = None
    createondate:str = datetime.now()
    modifyondate:str = datetime.now()
    objectid:int = None
    requestactions:str = None
    requestoperation:requestoperation()
    originalrequest:bool = None
    forcebroadcast:bool = None
    updatecount:int = None

    auditTrails:list = AuditTrailsModel()
