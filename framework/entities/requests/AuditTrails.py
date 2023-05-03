from datetime import datetime

class AuditTrails:
    id:int = None
    requestid:int = None
    auditid:int = None
    #actiontype: RuleAction()
    rulename:str = None
    #status:AuditStatus()
    fields:str = None
    ruleobject:str = None
    ruleobjectvalue:str = None
    createondate:str = datetime.now()
    modifyondate:str = datetime.now()