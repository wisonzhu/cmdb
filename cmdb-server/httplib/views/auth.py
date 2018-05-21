#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 下午11:32
# @Author  : Aries
# @Site    : 
# @File    : testauth.py
# @Software: PyCharm
from httplib.base.webbase import *
from uuid import uuid4
from httplib.models.model import *


class token(webbase):
    async def get(self):
        username = await  self.check_session()
        if username:
            obj = User.objects.filter(username=username)
            token = obj[0]['token']
            if token is None:
                Token = uuid4().hex
                User.objects.filter(username=username).update(token=Token)
            data=obj[0].to_json()
            return web.Response(text=data)
        else:
            return web.HTTPFound('/static/login.html')


class login(webbase):
    async def get(self):
        session = await get_session(self.request)
        username = session['username'] if 'username' in session else None
        if username:
            return web.Response(text=f'hello,{username}')
        else:
            return web.Response(text="please login")

    async def post(self):
            session = await get_session(self.request)
            header = self.request.headers
            user = header.get('username')
            token = header.get('token')
            password = header.get('password')
            if self.request.content_type.startswith('application/json'):
                    userinfo = await self.request.json()
            else:
                    userinfo = await self.request.post()
                    user = userinfo.get('username')
                    password = userinfo.get('password')

            logging.info(user)
            logging.info(password)
            if user and token:
                ret = User.objects.filter(username = user).filter(token = token)
            if user and password:
                ret = User.objects.filter(username = user).filter(password = password)

            if ret:
                session['username'] = user
                data = 'login success'
            else:
                data = 'login fail'
            return web.Response(text=data)


class logout(webbase):
    async def get(self):
        session = await get_session(self.request)
        session.invalidate()
        return web.Response(text='user is logout')


class Userinfo(webbase):
    async def get(self):
            userinfo = User.objects.to_json()
            return web.Response(text=userinfo)

    async def post(self):
        #data = self.check_session()
        #admin=['admin','zhuxz','root']
        userinfo = await self.request.json()
        obj = userinfo.pop('roleid')
        userinfo['role']=UserRole.objects.filter(roleid=obj)
        User(**userinfo).save()
        return web.Response(text="user add successful")

class Authority(webbase):
    async def get(self):
        obj = UserPermisson.objects.to_json()
        return web.Response(text=obj)

    async def post(self):
        obj = await self.request.json()
        logging.info(obj)
        UserPermisson(**obj).save()
        return web.Response(text="ttt")

class role(webbase):
    async def post(self):
        obj = await self.request.json()
        typeid = obj.pop("typeid")
        roletype = UserPermisson.objects.filter(typeid=typeid)
        obj['roleitem'] = roletype
        UserRole(**obj).save()
        return web.Response(text='add successfull')

    async  def get(self):
        obj = UserRole.objects(roleid=101)
        data=dict()
        data['i']=obj[0]['roleid']
        data['roleitem']=obj[0]['roleitem'][0]['peritem']
        logging.info(data)

        return web.json_response(data)







