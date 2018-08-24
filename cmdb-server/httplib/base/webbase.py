#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 下午9:41
# @Author  : Aries
# @Site    : 
# @File    : webbase.py
# @Software: PyCharm

from aiohttp import web
from abc import ABCMeta
from aiohttp_session import get_session
import logging
import json
class webbase(web.View):
    
    async def check_session(self):
            session = await get_session(self.request)
            logging.info(session)
            if session :
                data = session['username']
            else:
                data = None
            return data

    async def response(self, data=None, status=None, code=None, error=None):
        return web.json_response(data={
            "code": code or status or 200,
            "data": data,
            "error": error,
        }, status=200, dumps=json.dumps, content_type="application/json")







