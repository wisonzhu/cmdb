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

async def init(loop):
    app = web.Application(loop=loop)
    aiohttp_jinja2.setup(app,
                         loader=jinja2.FileSystemLoader('httplib/template'))
    setup_router(app)
    config = settings.parseconfig()
    redis = await create_pool(('localhost', 6379))
    setup(app, RedisStorage(redis, cookie_name="aiosession", max_age=3600))
    srv = await loop.create_server(app.make_handler(), config['http_server'], config['http_port'])
    logger.debug('server started at http://localhost:9001')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
