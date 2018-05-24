#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 下午5:34
# @Author  : Aries
# @Site    : 
# @File    : startweb.py
# @Software: PyCharm
import logging
import asyncio
import aiohttp_jinja2
import jinja2
from aiohttp import web
from httplib.views.asset import *
from httplib.models.model import *
from httplib.router import *
from basic import log
from config import settings
from aioredis import create_pool
from aiohttp_session import redis_storage, setup
from aiohttp_session.redis_storage import RedisStorage
logger = logging.getLogger(__name__)
access_logger = logging.getLogger("http.access")
config = settings.parseconfig()

async def middleware_404(app, handler):
    async def middleware_handler(request):
        try:
            return await handler(request)
        except web.HTTPException as ex:
            if ex.status == 404:
                return web.json_response({"error":"404"}, status=404)
            raise
    return middleware_handler

async def _init_app(loop=None):
    loop = loop or asyncio.get_event_loop()
    app = web.Application(loop=loop,middlewares=[middleware_404])
    aiohttp_jinja2.setup(app,
                         loader=jinja2.FileSystemLoader('httplib/template'))
    setup_router(app)
    redis = await create_pool(('localhost', 6379))
    setup(app, RedisStorage(redis, cookie_name="aiosession", max_age=3600))
    return app

def make_app(loop=None):
    return loop.run_until_complete(_init_app(loop=loop))

def main():
    loop = asyncio.get_event_loop()
    app = make_app(loop)
    def _http_access_log(*args, **kwargs):
        access_logger.debug(f"{args} {kwargs}")
    try:
        web.run_app(app,access_log=access_logger,
                host=config['http_server'],port=config['http_port'],print=_http_access_log
           )
    finally:
        loop.close()