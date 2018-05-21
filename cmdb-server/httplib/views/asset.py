#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 下午5:34
# @Author  : Aries
# @Site    : 
# @File    : views.py
# @Software: PyCharm
import logging

from httplib.models.model import *
from aiohttp import web
from datetime import datetime
logger = logging.getLogger(__name__)


class Assets(web.View):
    async def get(self):
        serverid = self.request.match_info.get('serverid')
        if serverid:
            result = Asset.objects.filter(servernums=serverid).to_json()
        else:
            result = Asset.objects().to_json()
        return  web.Response(body=f'{result}')

    async def post(self):
        obj = await self.request.json()
        result = Asset.objects.filter(servernums=obj['servernums'])
        try:
            if result:
                obj['updatetime'] = datetime.now()
                result = 'insert success'
            Asset(**obj).save()
        except:
            result = "insert fail"
        return  web.Response(body = result)

    async def put(self):
         data = await self.request.json()
         Asset.objects.filter(serverid=data['serverid']).update(systeminfo=data['systeminfo'])
         return  web.Response(text='updated')


class NetPool(web.View):
    async def get(self):
        obj = NetSegment.objects().to_json()
        return web.Response(text=obj)

    async def post(self):
        data = await self.request.json()
        return web.Response(data=data)





