from datetime import datetime
from framework.entities.enum.AuditStatus import AuditStatus
from framework.entities.enum.RuleAction import RuleAction

class AuditTrails:
    id:int = None
    requestid:int = None
    auditid:int = None
    actiontype:RuleAction()
    rulename:str = None
    status:AuditStatus()
    fields:str = None
    ruleobject:str = None
    ruleobjectvalue:str = None
    createondate:str = datetime.now()
    modifyondate:str = datetime.now()