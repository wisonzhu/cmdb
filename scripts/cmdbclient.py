#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import salt.client
caller = salt.client.Caller()
salt_data=caller.sminion.functions['grains.items']()
cmdb=dict()
salt_cmdb=dict()
salt_cmdb['osversion']=salt_data['lsb_distrib_codename']
salt_cmdb['virtual']=salt_data['virtual']
salt_cmdb['ip_interfaces']=salt_data['ip_interfaces']
salt_cmdb['hostname']=salt_data['host']
salt_cmdb['kernelrelease']=salt_data['kernelrelease']
salt_cmdb['num_cpus']=salt_data['num_cpus']
salt_cmdb['mem_total']=salt_data['mem_total']
salt_cmdb['productname']=salt_data['productname']
salt_cmdb['disks']=salt_data['disks']
salt_cmdb['productname']=salt_data['productname']
salt_cmdb['cpuarch']=salt_data['cpuarch']+ " " + salt_data['cpu_model']
cmdb['servernums'] = salt_data['serialnumber']
cmdb['systeminfo'] = salt_cmdb
headers = {"content-type": "application/json"}
r=requests.post("http://10.10.121.64:9001/asset/", data=json.dumps(cmdb), headers=headers)
print(r.text)
print(cmdb)
