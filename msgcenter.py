# -*- coding: utf-8 -*-
import unittest
import requests
import random
import hashlib
import string
import base64
import uuid
import json
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from models import *  # sqlacodegen mysql://root:root@127.0.0.1:3306/csgdicomsnalysisdb>D:\py\UnitTest\models.py
import csgmessage

mongo_conn = MongoClient('127.0.0.1', 27017)
db_ut = mongo_conn.ut_output
mongodb_collection = db_ut.output
msgcenter_url = "http://58.247.53.14:8080"
mysql_engine = create_engine('mysql+pymysql://root:root@localhost:3306/csgdicomsnalysisdb')
MysqlDBSession = sessionmaker(bind=mysql_engine) # DBSession 对象可视为当前数据库连接

def save_ut_result(msg):
    mongodb_collection.insert_one(eval(msg))

class MsgcenterTestCase(unittest.TestCase):
    username = "undefined"
    password = "undefined"
    encrypt_password = "undefined"
    mysql_session = MysqlDBSession()
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
        jsonmsg = json.dumps(msg, cls=csgmessage.MyJSONEncoder)
        res = requests.post(msgcenter_url,data=jsonmsg)
        self.assertEqual(res.status_code,200)
        save_ut_result(jsonmsg)
        dbuser = self.mysql_session.query(UserRegisterInfo).filter(UserRegisterInfo.name == MsgcenterTestCase.username).one()
        self.assertEqual(MsgcenterTestCase.username,dbuser.name)
        self.assertEqual(MsgcenterTestCase.encrypt_password, dbuser.password)
        print(f"user:{MsgcenterTestCase.username} register success!")

    def test02_login(self):
        msg = csgmessage.CsgLoginMessage()
        msg.data["name"] = MsgcenterTestCase.username
        msg.data["password"] = MsgcenterTestCase.encrypt_password
        # print(csgmessage.MyJSONEncoder().encode(msg))
        res = requests.post(msgcenter_url,data=json.dumps(msg, cls=csgmessage.MyJSONEncoder))
        print(res.text)
        self.assertEqual(res.status_code,200)
        print(f"user:{MsgcenterTestCase.username} login success!")

    def test03_modify_password(self):
        msg = csgmessage.CsgModifyPasswordMessage()
        MsgcenterTestCase.password = "222222"
        MsgcenterTestCase.encrypt_password = self.encode_password(MsgcenterTestCase.password)
        msg.data["name"] = MsgcenterTestCase.username
        msg.data["password"] = MsgcenterTestCase.encrypt_password
        print(csgmessage.MyJSONEncoder().encode(msg))
        res = requests.post(msgcenter_url,data=json.dumps(msg, cls=csgmessage.MyJSONEncoder))
        self.assertEqual(res.status_code,200)
        print(f"user:{MsgcenterTestCase.username} password has been changed success!")

    def test04_get_patient_info(self):
        pass

    # def test05_analyze_study(self):
    #     msg = csgmessage.CsgAnalyzeStudyMessage()
    #     msg.data["publicid"] = "studyid"
    #     print(csgmessage.MyJSONEncoder().encode(msg))
    #     res = requests.post(msgcenter_url,data=json.dumps(msg, cls=csgmessage.MyJSONEncoder))
    #     self.assertEqual(res.status_code,200)
    #     print(f"user:{MsgcenterTestCase.username} password has been changed success!")

    def test06_get_fudan_config(self):
        config_msg = csgmessage.CsgGetFudanConfigMessage()
        config_msg.data["context"] = "test"
        print("发送:" + csgmessage.MyJSONEncoder().encode(config_msg))
        res = requests.post(msgcenter_url, data=json.dumps(config_msg, cls=csgmessage.MyJSONEncoder))
        print(f"返回: {res.text}")
        # send {"vendor_id": "fd_plugin", "uid": "e277acac-bde7-11e7-afc7-509a4c215466", "business_id": 2, "status": 0, "in_version": "1.0.0.1", "out_version": "1.0.0.1", "message": "defaultmsg", "data": {"context": "test"}}
        # receive {"business_id":2,"data":{"context":"{\"Password\":\"root\",\"Username\":\"root\"}\n"},"in_version":"1.0.0.1","message":"defaultmsg","out_version":"1.0.0.1","status":1,"uid":"509A4C215466","vendor_id":"csg_cc"}

    def test07_notify_analyze_progress(self):
        progress_msg = csgmessage.CsgProgressMessage()
        progress_msg.data["publicid"] = str(uuid.uuid1())
        progress_msg.data["progress"] = 27
        print("发送:" + csgmessage.MyJSONEncoder().encode(progress_msg))
        res = requests.post(msgcenter_url, data=json.dumps(progress_msg, cls=csgmessage.MyJSONEncoder))
        self.assertEqual(res.status_code,200)
        print(f"返回: {res.text}")

    def test08_report(self):
        report_msg = csgmessage.CsgReportMessage()
        report_msg.data["publicid"] = str(uuid.uuid1())
        report_msg.data["file"] = "samplefile"
        report_msg.data["context"] = "sth"
        print("发送:" + csgmessage.MyJSONEncoder().encode(report_msg))
        res = requests.post(msgcenter_url, data=json.dumps(report_msg, cls=csgmessage.MyJSONEncoder))
        self.assertEqual(res.status_code,200)
        print(f"返回: {res.text}")

if __name__ == "__main__":
    print({i: el for i, el in enumerate(["one", "two", "three"])})
    list1 = ["这", "是", "一个", "测试"]
    for index, item in enumerate(list1):
        print(index, item)
    # test = MsgcenterTestCase()
    # test.test08_report()

    # unittest.main()

    # config_msg = csgmessage.CsgGetFudanConfigMessage()
    # config_msg.data["context"] = "test"
    # print("发送:" + csgmessage.MyJSONEncoder().encode(config_msg))
    # res = requests.post(msgcenter_url, data=json.dumps(config_msg, cls=csgmessage.MyJSONEncoder))
    # print(f"返回: {res.text}")
    #
    #
    # print("发送进度")
    # progress_msg = csgmessage.CsgProgressMessage()
    # progress_msg.data["publicid"] = "id1"
    # progress_msg.data["progress"] = 27
    # print("发送:" + csgmessage.MyJSONEncoder().encode(progress_msg))
    # res = requests.post(msgcenter_url, data=json.dumps(progress_msg, cls=csgmessage.MyJSONEncoder))
    # print(f"返回: {res.text}")