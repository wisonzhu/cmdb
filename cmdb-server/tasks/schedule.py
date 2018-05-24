#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 下午9:14
# @Author  : Aries
# @Site    : 
# @File    : schedule.py
# @Software: PyCharm
from apscheduler.schedulers.blocking import BlockingScheduler

def my_job():
    with open("abc.txt","a+") as f:
        f.write("abc\n")
    print("test123")
sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=5)
sched.start()