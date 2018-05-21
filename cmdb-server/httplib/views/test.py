#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 上午7:35
# @Author  : Aries
# @Site    : 
# @File    : testview.py
# @Software: PyCharm
from httplib.base.webbase import *
import aiohttp_jinja2

class mytest(webbase):
    async def get(self):
            username = await self.check_session()
            if username:
                return web.Response(text=f'this is test {username}')
            else:
                return web.HTTPFound('/asset/')

class mytestview(webbase):
    @aiohttp_jinja2.template('tmpl.jinja2')
    async def get(self):
        return {'name': 'test123', 'host': 'localhost'}

    async def post(self):
        return web.Respone(text='this is post')