#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import requests
import json
import salt.client
cmdb=dict()
salt_cmdb=dict()
salt_cmdb['disks']=None
salt_cmdb['IdcName'] = None
salt_cmdb['idrac_addr'] = None
caller = salt.client.Caller()
salt_data = caller.sminion.functions['grains.items']()
keys = ["IdcName","disks","idrac_addr",'lsb_distrib_codename']
for i in keys:
    if salt_data.has_key(i):
        pass
    else:
        salt_data[i] = None
try:
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
    salt_cmdb['saltversion'] = salt_data['saltversion']
    salt_cmdb['idrac_addr'] = salt_data['idrac_addr']
    cmdb['servernums'] = salt_data['serialnumber']
    cmdb['systeminfo'] = salt_cmdb
except:
     pass

if  __name__  == "__main__":

    headers = {"content-type": "application/json"}
    r=requests.post("http://10.10.121.64:9001/asset/", data=json.dumps(cmdb), headers=headers)
    print(r.text)
    print(cmdb)
