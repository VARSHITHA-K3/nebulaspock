from datetime import datetime

class Entities:
    id:int = None
    name:str = None
    type:str = None
    systemid:int = None
    createondate:str = datetime.now()
    modifyondate:str = datetime.now()
    applycondition:str = None
    raiserequest:int = None
    broadcastprocedure:str = None
    forcebroadcast:bool = None