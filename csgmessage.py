import json
import uuid
from enum import Enum

#Bussiness ID Def
class BussinessID(Enum):
    login = 1
    query_patient = 4
    register_user = 9
    modify_password = 10


#Message Def
class CsgMessageBase(object):
    def __init__(self):
        self.vendor_id = "csg_client"
        self.uid = uuid.uuid1()
        self.business_id = 0
        self.status = 0
        self.in_version = "1.0.0.1"
        self.out_version = "1.0.0.1"
        self.message = "defaultmsg"

class CsgRegisterMessage(CsgMessageBase):
    def __init__(self):
        super().__init__()
        self.business_id = BussinessID.register_user.value
        self.data = {"name":"","password":""}

class CsgLoginMessage(CsgMessageBase):
    def __init__(self):
        super().__init__()
        self.business_id = BussinessID.login.value
        self.data = {"name":"","password":""}

class CsgModifyPasswordMessage(CsgMessageBase):
    def __init__(self):
        super().__init__()
        self.business_id = BussinessID.modify_password.value
        self.data = {"name":"","password":""}

class CsgQueryPatientMessage(CsgMessageBase):
    def __init__(self):
        super().__init__()
        self.business_id = BussinessID.query_patient.value

class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        d = {}
        # d['__class__'] = obj.__class__.__name__
        # d['__module__'] = obj.__module__
        d.update(obj.__dict__)
        return d

class MyJSONDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict2obj)

    def dict2obj(self, d):
        if '__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module, class_name)
            args = dict((key.encode('ascii'), value) for key, value in d.items())
            instance = class_(**args)
        else:
            instance = d
        return instance

if __name__ == "__main__":
    msg = CsgMessageBase()
    print(MyJSONEncoder().encode(msg))
    registermsg = CsgRegisterMessage()
    registermsg.data["name"] = "9527"
    registermsg.data["password"] = "9527"
    print(MyJSONEncoder().encode(registermsg))