#!/bin/bash
cd /data/gitv-cmdb/cmdb-gitv/cmdb-server
ps -ef |grep startweb|grep -v grep |awk '{print $2}'|xargs kill -9
nohup  /data/python36/bin/python3 startweb.py &

