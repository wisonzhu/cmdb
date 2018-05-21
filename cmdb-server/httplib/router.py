#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 下午5:35
# @Author  : Aries
# @Site    : 
# @File    : routers.py
# @Software: PyCharm
from httplib.views.asset import *
from httplib.views.index import *
from httplib.views.auth import *
from httplib.views.test import *
from httplib.views.order import *

def setup_router(app):
    app.router.add_route("*", "/", Index)
    app.router.add_route("*","/net/",NetPool)
    app.router.add_route('*', '/asset/', Assets)
    app.router.add_route("GET", '/asset/{serverid}/', Assets)
    app.router.add_route("PUT", '/asset/{serverid}/', Assets)
    app.router.add_route('*', '/workerorder/', WorkerOrder)
    app.router.add_route('*', '/auth/mytest/',mytest)
    app.router.add_route("*", "/view/", mytestview)
    
    ###用户管理###
    app.router.add_route("*", "/user/", Userinfo)
    app.router.add_route("*","/user/role/",role)
    app.router.add_route("*", "/user/permission/",Authority)
    app.router.add_route("*", '/auth/token/', token)
    app.router.add_route('*', '/auth/login/', login)
    app.router.add_route('*', '/auth/logout/', logout)

    ##static file#####
    app.router.add_static("/static/", path="cmdb-ui/",name='static')
    app.router.add_static("/css/", path="cmdb-ui/css/",name='css')
    app.router.add_static("/js/", path="cmdb-ui/js/", name='js')



