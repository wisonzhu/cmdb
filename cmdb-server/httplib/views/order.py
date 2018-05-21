#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 下午1:33
# @Author  : Aries
# @Site    : 
# @File    : orders.py
# @Software: PyCharm
from aiohttp import web
from datetime import datetime
from httplib.base.webbase import *
from httplib.models.model import *

class WorkerOrder(web.View):
    async def get(self):
        obj = Ticket.objects().to_json()
        return web.Response(text = obj)

    async def post(self):
        obj = await self.request.json()
        order = Ticket.objects.filter(bid=obj['bid'])
        obj['note'] = [{'content': obj['note'],"date":
            datetime.now().strftime('%Y/%m/%d-%H:%M:%S')}]
        if obj and order:
            order.update(push__note=obj['note'] )
            order.update(update_time = datetime.now(),status = obj['status'])
        elif obj:
            obj['create_time'] = datetime.now()
            Ticket(**obj).save()
        else:
            logger.info('insert error')
        return web.Response(text='finished')


class Task(webbase):
    async def get(self):
            pass

    async def post(self):
            pass



