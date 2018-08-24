#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 下午5:40
# @Author  : Aries
# @Site    : 
# @File    : index.py
# @Software: PyCharm
from aiohttp import web
from httplib.base.webbase import *

class Index(webbase):
    async def get(self):
        return await self.response(data='index')



