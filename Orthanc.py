import unittest
import urllib.request
import json


class OrthancTestCase(unittest.TestCase):
    def setUp(self):
        self._host = "http://localhost:8042/"
        self.__patientids = []

    def tearDown(self):
        self.__patientids.clear()
    def test01_getallpatientid(self):
        res = urllib.request.urlopen(self._host + "patients").read()
        self.__patientids = json.loads(res)
        self.assertIsNotNone(self.__patientids)
    def test02_getpatientinformation(self):
        for id in self.__patientids:
            res = urllib.request.urlopen(self._host + "patients/" + id).read()
            self.assertIsNotNone(res)

    def test03_getstruidies(self):
        pass