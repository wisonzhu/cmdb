#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 下午5:34
# @Author  : Aries
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from mongoengine import *
from datetime import datetime
from config.settings import  *
database = parseconfig()
dbname = database['db_name']
host = database['mongo_host']
port = database['mongo_port']
connect(dbname, host=host, port=port)


class Asset(Document):
    servernums = StringField(required=True,primary_key=True)
    hostname = StringField(max_length=200)
    status = StringField(max_length=200,default="online")
    ownner = StringField(max_length=200,default="admin")
    createtime = DateTimeField(default=datetime.now)
    updatetime = DateTimeField(null=False)
    ip  = StringField(max_length=50,null=True)
    systeminfo = DictField(null=True)

class Derpartment(Document):
        name = StringField(max_length=100)

class UserPermisson(Document):
    typeid = IntField(required=True,unique=True)
    peritem = StringField(required=True,max_length=120)


class UserRole(Document):
    roleid = IntField(required=True,unique=True)
    roleitem = ListField(ReferenceField(UserPermisson))


class User(Document):
    uid = StringField(primary_key=True)
    username = StringField(max_length=30,required=True, unique=True)
    token = StringField()
    password = StringField()
    role =  ListField(ReferenceField(UserRole))


class NetSegment(Document):
    net_name = StringField(max_length=200)
    ip_net = StringField(max_length=200)
    ip_list = StringField(null=True)
    status =  StringField(choices=('enable','disable'),default='disable')


class Ticket(Document):
    bid = StringField(unique=True)
    type = StringField(unique=True, default="undefine")
    note = ListField(DictField())
    status = StringField(choices=("start","pending","doing","done"),default="start")
    update_time = DateTimeField(default=datetime.now)
    create_time = DateTimeField(null=False)


class Task(Document):
     taskid = StringField(max_length=200)
     task = StringField()






