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
from httplib.views.networks import *

def setup_router(app):

    app.router.add_route("GET", '/asset/{serverid}/', Assets)
    app.router.add_route("POST", '/asset/update/', webupdate)
    app.router.add_route("*", "/idc/", Idcinfo)
    app.router.add_route("*", "/pallet/", Palletinfo)
    app.router.add_route("*", "/rack/", Rackinfo)
    app.router.add_route("*", "/bandwidth/", Bandwidthinfo)
    app.router.add_route("*", "/asset/project/",Project)

    app.router.add_route("*", "/", Index)
    app.router.add_route('*', '/asset/', Assets)
    app.router.add_route('*', '/auth/mytest/',mytest)
    app.router.add_route("*", "/view/", mytestview)

    #######网段管理#######
    app.router.add_route("*", "/net/", NetPool)

    #######用户管理#######
    app.router.add_route("*", "/user/", Userinfo)
    app.router.add_route("*", "/user/userinfo/", myinfo)
    app.router.add_route("*", "/group/", Department)
    app.router.add_route("*","/user/role/",role)
    app.router.add_route("*", "/user/permission/",Authority)
    app.router.add_route("*", '/auth/token/', token)
    app.router.add_route('*', '/auth/login/', login)
    app.router.add_route('*', '/auth/logout/', logout)


    ######workflow########
    app.router.add_route('*', '/workerorder/', WorkerOrder)
    app.router.add_route('*', '/workerorder/{bid}/', WorkerOrder)
    app.router.add_route("*", "/workflow/", Workerflow)
    app.router.add_route("*", "/workflow/update/", execflow)

    #####项目管理########
    app.router.add_route("*", "/project/", ProjectInfo)



    ##static file#####

    app.router.add_static("/static/", path="ui/", name='static')
    app.router.add_static("/css/", path="ui/assets/css/", name='css')
    app.router.add_static("/js/", path="ui//assets/js/", name='js')
    app.router.add_static("/img/", path="ui/assets/img/", name='img')

    app.router.add_static("/front/", path="cmdbui/", name='static1')
    app.router.add_static("/front/css/", path="cmdbui/css/", name='css1')
    app.router.add_static("/front/js/", path="cmdbui/js/", name='js1')
    app.router.add_static("/front/img/", path="cmdbui/img/", name='img1')

    app.router.add_route("*", "/asset1/", ajax)









