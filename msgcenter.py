import unittest
import requests
import random
import hashlib
import string
import base64
import json
import csgmessage

class MsgcenterTestCase(unittest.TestCase):
    host_url = "http://localhost:8042"
    username = "undefined"
    password = "undefined"
    encrypt_password = "undefined"

    def encode_password(self,rawpassword):
        s512 = hashlib.sha512(rawpassword.encode()).hexdigest()
        b64 = base64.b64encode(s512.encode())
        return hashlib.md5(b64).hexdigest()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01_registeruser(self):
        MsgcenterTestCase.username = ''.join(random.sample(string.ascii_letters,6))
        MsgcenterTestCase.password = "111111"
        MsgcenterTestCase.encrypt_password = self.encode_password(MsgcenterTestCase.password)
        msg = csgmessage.CsgRegisterMessage()
        msg.data["name"] = MsgcenterTestCase.username
        msg.data["password"] = MsgcenterTestCase.encrypt_password
        print(csgmessage.MyJSONEncoder().encode(msg))
        res = requests.post(self.host_url,data=json.dumps(msg, cls=csgmessage.MyJSONEncoder))
        print(res)
        self.assertEquals(res.status_code,200)
        print(f"user:{MsgcenterTestCase.username} register success!")

    def test02_login(self):
        pass

    def test03_modify_password(self):
        pass

    def test04_get_patient_info(self):
        pass


if __name__ == "__main__":
    test = MsgcenterTestCase()
    test.test01_registeruser()

    # unittest.main()