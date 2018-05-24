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
from httplib.services.service import *
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
            data = "update successful"
        elif obj:
            obj['create_time'] = datetime.now()
            try:
                Order(bid=obj['bid'], type=obj['type'], stage_status="application",
                    status = [{"task1": "ok" }]).save()

                Ticket(**obj).save()
                data = "create1 order success"
            except:
                 data = "create1 order fail"

        else:
             data = "create order fail"

        return web.Response(text=data)


class Task(webbase):
    async def get(self):
            pass

    async def post(self):
            pass


class Workerflow(webbase):
    async def get(self):
       data = Workflow.objects.to_json()
       return web.Response(text=data)

    async def post(self):
        data = await self.request.json()
        data['tasks'] = [data['tasks']]
        data['stage'] = [data['stage']]
        obj = data
        try:
            if Workflow.objects(name = data['name']).count():
                result = "workflow is exist."
            else:
                Workflow(**obj).save()
                result = "workflow is create"
        except:
                result = "workflow create error"

        return  web.Response(text=result)

class execflow(webbase):
        async def get(self):
            obj = Order.objects.to_json()
            return web.Response(body=obj)

        async def post(self):
             data = await self.request.json()
             workflow = exec_workflow(bid=data['bid'], type=data['type'], task=data['task'],status=data['status'])
             data = workflow.execflow()
             return web.Response(text=data)



