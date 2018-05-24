#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 上午10:05
# @Author  : Aries
# @Site    : 
# @File    : logger.py
# @Software: PyCharm
import logging.config
from config.settings import *
path = parseconfig()['log_path']
DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s %(levelname)-8s %(name)s %(message)s",
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ["default", "console"]
        },
        'http.access': {
            'level': 'DEBUG',
            'handlers': ["views", "console"]
        },
    },
    "handlers": {
        "workflow": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "logs/access.log",
            "maxBytes": 10240000000,
            "backupCount": 7,
        },
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "views": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": f"{path}/test.log",
            "maxBytes": 10240000000,
            "backupCount": 7,
        },
        "default": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": f"{path}/access.log",
            "maxBytes": 10240000000,
            "backupCount": 7,
        },
    },
}

logging.config.dictConfig(DEFAULT_LOGGING)
