from datetime import datetime

class EntityProperties:
    id:int = None
    entityid:int = None
    name:str = None
    sourcename:str = None
    destname:str = None
    datatype:str = None
    length:str = None
    isidentifier:bool = None
    defaultvalue:str = None
    createondate:str = datetime.now()
    modifyondate:str = datatype.now()