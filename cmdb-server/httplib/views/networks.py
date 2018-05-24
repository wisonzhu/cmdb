#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 下午3:49
# @Author  : Aries
# @Site    : 
# @File    : networks.py
# @Software: PyCharm

from httplib.models.model import *
from aiohttp import web
from datetime import datetime
import logging
logger = logging.getLogger(__name__)

class NetPool(web.View):
    async def get(self):
        obj = NetSegment.objects().to_json()
        return web.Response(text=obj)

    async def post(self):
        data = await self.request.json()
        return web.Response(data=data)
