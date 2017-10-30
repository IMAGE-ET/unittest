# -*- coding: utf-8 -*-
import requests
import urllib.request
import json
import ssl
import unittest
import zipfile
import time
# from Orthanc import OrthancTestCase
from msgcenter import MsgcenterTestCase
import asyncio


class Test(object):
    def __call__(self, *args, **kwargs):
        print("in call")
    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)
    def __init__(self):
        print("init")
    def print_args(*args,**kwagrs):
        for v in args:
            print(v)
        for i in kwagrs.items():
            print(i)

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=Singleton):
    pass

class singleton(object):
    pass
singleton=singleton()

class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob

class MyClass2(Borg):
    a = 1
    def setname(self,name):
        self.name = name


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None) #当send方法的参数为None时，它与next方法完全等价
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


def gen():
    value=0
    while True:
        print("before receive")
        receive=yield value
        print("receive = " + receive)
        if receive=='e':
            break
        value = 'got: %s' % receive

def countdown(n):
    print ("Counting down from", n)
    while n >= 0:
        newvalue = (yield n)
        print('newvalue:',newvalue)
        print('n:',n)
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1

async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect #相当于 for c in connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")

if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()

    # c = countdown(5)
    # for x in c:
    #     print('x:', x)
    #     if x == 5:
    #         c.send(3)
    #         c.send(2)

    # g = gen()
    # print(g.send(None))
    # print(g.send("abc"))
    # print(g.send(3))
    # print(g.send('e'))
    # mygenerator = (x * x for x in range(3))
    # for i in mygenerator:
    #     print(i)
    # for j in mygenerator:
    #     print(j)

    # c = consumer()
    # next(c)
    # c.send(3)

    # produce(c)
    # f = zipfile.ZipFile("e:/test.zip", 'r')
    # for file in f.namelist():
    #     f.extract(file, "temp/")

    # a = singleton
    # b = singleton
    # print(id(a))
    # print(id(a))

    # s1 = MyClass()
    # s2 = MyClass()
    # print(id(s1))
    # print(id(s2))
    # print(s1 is s2)

    # m1 = MyClass2()
    # m1.setname("aaa")
    # m2 = MyClass2()
    # m2.setname("bbb")
    # print(m1.name)
    # print(m2.name)
    # print(m1.__dict__ == m2.__dict__)
    # print(m2.__dict__)
    # t = Test()
    # t()
    # args = [1,3,"2222"]
    # kwargs = {"arg3": 3, "arg2": "two"}
    # t.print_args(*args,**kwargs)



    # ssl._create_default_https_context = ssl._create_unverified_context
    # context = ssl._create_unverified_context()
    # print(urllib.request.urlopen("https://127.0.0.1:8080",context=context).read())
    # print(requests.get('https://127.0.0.1:8080').text)

    # f = urllib.request.urlopen("https://www.baidu.com/")
    # buf = f.read()
    # print(buf)
    # f.close()
    unittest.main()
    pass