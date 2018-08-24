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
from httplib.base.webbase import *
from httplib.services.service import *
logger = logging.getLogger(__name__)

class Idcinfo(webbase):
    async def get(self):
        data = Idc.objects.to_json()
        logging.info(data)
        return web.Response(text=data)

    async def post(self):
        info = await self.request.json()
        obj = IdcManager()
        result = obj.excutor(name=info['name'],data=info['data'])
        return web.Response(text=result)

class Rackinfo(webbase):
    async def get(self):
        data = MachineRack.objects.to_json()
        return web.Response(text=data)


class Palletinfo(webbase):
    async def get(self):
        data = Pallets.objects.to_json()
        return web.Response(text=data)


class Bandwidthinfo(webbase):
    async def get(self):
        obj = IdcBandWidth.objects.to_json()
        return web.Response(text=obj)

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
        try:
            if  obj.get('project'):
                if Project.objects.filter(name=obj['project']['name']):
                    obj['project'] = Project.objects.filter(name=obj['project']['name'])[0]
                else:
                    Project(**obj['project']).save()
                    obj['project'] = Project.objects.filter(name=obj['project']['name'])[0]
            if Asset.objects.filter(servernums=obj['servernums']):
                Asset.objects(servernums=obj['servernums']).update(set__systeminfo=obj['systeminfo']
                                                            ,set__updatetime=datetime.now() )
            else:
                obj['updatetime'] = datetime.now()
                Asset(**obj).save()
            result = "create sucessful"
        except:
            result = "insert fail"
        return  web.Response(text = result)

class webupdate(webbase):
    async def post(self):
        obj = await self.request.post()
        data =dict()
        data['servernums'] = obj.get('servernums')
        data['status'] = obj.get('status')
        data['env'] = obj.get('env')
        logging.info(data)
        obj = Asset.objects.filter(servernums=data['servernums'])
        if obj:
            obj.update(**data)
        return web.Response(text='updated')

class ProjectInfo(webbase):
    async def get(self):
        info = Project.objects.to_json()
        return web.Response(text=info)

    async def post(self):
        info = await self.request.json()
        Project(**info).save()
        return web.Response(text="project create successful")



class ajax(webbase):
        async def get(self):
            obj = json.loads(Asset.objects.to_json())
            logger.info(obj)
            data = dict()
            data['data']= obj
            return web.json_response(data)








