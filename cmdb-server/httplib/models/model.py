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

#####IDC带宽信息#######
class IdcBandWidth(Document):
    uid = StringField(unique=True)
    idcname = StringField()
    billinfo = StringField()
    purchasedate = DateTimeField()
    expiredate = DateTimeField()
    status = StringField()
    note = StringField()

class Pallets(Document):
    palletid = StringField(unique=True)
    name = StringField()
    note = StringField()

######机柜信息############
class MachineRack(Document):
    rackid = StringField(unique=True)
    rackname =  StringField(max_length=200)
    billinfo = StringField()
    purchasedate = DateTimeField()
    expiredate = DateTimeField()
    palletinfo = ListField(ReferenceField(Pallets))
    status = StringField()
    note = StringField()


#######IDC######
class Idc(Document):
    idcid = StringField(unique=True)
    idcname = StringField()
    contact = StringField()
    owner = StringField()
    link = StringField()
    address = StringField()
    status = StringField()
    note = StringField()
    bandwidth = ReferenceField(IdcBandWidth)
    rackinfo = ListField(ReferenceField(MachineRack))


class Project(Document):
    name = StringField(unique=True,max_length=120)
    start_date = DateTimeField(default=datetime.now())
    end_date = DateTimeField()
    status = StringField()
    owner = StringField(default="admin")
    note = StringField()

class Asset(Document):
    servernums = StringField(required=True,unique=True)
    hostname = StringField(max_length=200)
    status = StringField(max_length=200,default="online")
    ownner = StringField(max_length=200,default="admin")
    createtime = DateTimeField(default=datetime.now)
    updatetime = DateTimeField(default=datetime.now)
    ip  = StringField(max_length=50,null=True)
    systeminfo = DictField(null=True)
    env = StringField(max_length=200,default="prod")
    idcinfo = ReferenceField(Idc)
    idrac_ip = StringField(max_length=50,null=True)
    project = ReferenceField(Project,null=True)

class UserPermisson(Document):
    typeid = IntField(required=True,unique=True)
    peritem = StringField(required=True,max_length=120)


class UserRole(Document):
    roleid = IntField(required=True,unique=True)
    roleitem = ListField(ReferenceField(UserPermisson))


class UserGroup(Document):
    uid = StringField(unique=True)
    name = StringField(max_length=120)
    datatime = DateTimeField(default=datetime.now)

class User(Document):
    uid = StringField(primary_key=True)
    username = StringField(max_length=30,required=True, unique=True)
    token = StringField()
    password = StringField()
    role =  ListField(ReferenceField(UserRole))
    group = ListField(ReferenceField(UserGroup))


class NetSegment(Document):
    net_name = StringField(max_length=200)
    ip_net = StringField(max_length=200)
    type = StringField(max_length=200)
    ip_list = ListField(null=True)
    status =  StringField(choices=('enable','disable'),default='disable')


class Ticket(Document):
    bid = StringField(unique=True)
    type = StringField()
    content = StringField(required=True)
    note = ListField(DictField())
    status = StringField(choices=("start","pending","doing","done"),default="start")
    update_time = DateTimeField(default=datetime.now)
    create_time = DateTimeField(null=False)

class Workflow(Document):
    name = StringField(unique=True)
    stage = ListField(required=True)
    tasks = ListField(DictField())

class Order(Document):
    bid = StringField(unique=StringField)
    type = StringField()
    status = ListField(DictField())
    stage_status = StringField()















