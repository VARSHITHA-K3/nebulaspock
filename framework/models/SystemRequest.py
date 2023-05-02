from datetime import datetime

class SystemRequestModel:
    id:int = None
    isProcessed:bool = None
    requestor:str = None
    requestType:str = None
    #requestStatus:requeststatus = None
    requestjson:str = None
    requestedDate:str = datetime.now()
    requestComments:str = None
    entityId:int = None
    entityType:str = None
    createonDate:str = datetime.now()
    modifyondate:str = datetime.now()
    objectid:int = None
    requestactions:str = None
    #requestoperation:requestoperation = None
    originalrequest:bool = None
    forcebroadcast:bool = None
    updatecount:int = None
