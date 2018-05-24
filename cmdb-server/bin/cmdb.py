#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 上午10:01
# @Author  : Aries
# @Site    : 
# @File    : cmdb.py
# @Software: PyCharm
import os
import time
import sys
from startweb import main
import signal

if __name__ == '__main__':
    if sys.argv[1] == "start":
        pid = os.fork()
        if pid == 0:
            print(os.getpid(),os.getppid())
            main()
        else:
            with open("logs/cmdb.pid","w+") as f:
                    f.write(str(pid))
            sys.exit(0)

    if sys.argv[1] == "stop":
        try:
            with open("logs/cmdb.pid","r+") as f:
                pid= str.strip(f.readline())
                os.kill(int(pid), signal.SIGKILL)
        except:
               print("pid not exist")

