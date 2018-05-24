#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 下午6:31
# @Author  : Aries
# @Site    : 
# @File    : service.py
# @Software: PyCharm
from httplib.models.model import *


class exec_workflow(object):
    def __init__(self,bid,task,status,type):
        self.task = task
        self.status = status
        self.type = type
        self.bid = bid

    def execflow(self):
        workflow  = Workflow.objects.filter(name=self.type)
        if workflow:
            stage = workflow[0].stage[0]
            current_status = workflow[0].tasks[0][self.task]['stage']
            if self.type == "Asset":
                obj = Order.objects(bid=self.bid)
                stage_status = obj[0].stage_status
                if  stage_status == "finish" or stage_status == "cancel":
                        return "workerorder is close"
                if obj:
                    next_stage = stage[stage.index(stage_status) +1]
                    if current_status == next_stage and self.status == "ok":
                        obj.update(stage_status=next_stage)
                        task_status = [{self.task : self.status } ]
                        obj.update(push__status = task_status)
                        data = "update sucessful"
                    elif current_status == next_stage and self.status == "cancel":
                        data = "workerorder cannel"
                        obj.update(stage_status=f"{self.task}:cancel")
                    else:
                        data = "workerorder error"
                if next_stage == "finish" or self.status == "cancel":
                     Ticket.objects.filter(bid=self.bid).update(status="close")
        else:
            data = f"{self.type} workflow is not exist"
        return data



class IdcManager(object):
    def idc(self,data):
        rackobj = data["rackinfo"]
        idcid = data['idcid']
        if IdcBandWidth.objects.filter(uid=data['bandwidth']['uid']):
             data['bandwidth'] = IdcBandWidth.objects.filter(uid=data['bandwidth']['uid'])[0]
        else:
            objband = data['bandwidth']
            IdcBandWidth(**objband).save()
            data['bandwith'] = IdcBandWidth.objects.filter(uid=data['bandwidth']['uid'])[0]

        logging.info(data)
        if Idc.objects.filter(idcid = idcid):
            return "idc exist"

        else:
            if rackobj:
                rackinfo = MachineRack.objects.filter(rackid = rackobj['rackid'])
                if rackinfo:
                    data['rackinfo'] = rackinfo
                    logging.info(data)
                    Idc(**data).save()
                    return "add"
                else:
                    MachineRack(**rackobj).save()
                    data['rackinfo'] = MachineRack.objects.filter(rackid = rackinfo['rackid'])
                    Idc(**data).save()
                    return "new add"

    def rack(self,data):
        obj = data["palletinfo"]
        if MachineRack.objects.filter(rackid=data['rackid']):
            return "rack exist"
        else:
            if obj:
                palletinfo = Pallets.objects.filter(palletid=obj['palletid'])
                if palletinfo:
                    data['palletinfo'] = palletinfo
                    MachineRack(**data).save()
                    return "add"
                else:
                    Pallets(**obj).save()
                    data['palletinfo'] = Pallets.objects.filter(palletid=obj['palletid'])
                    logging.info(data)
                    MachineRack(**data).save()
                    return "new add"

    def pallet(self,data):
        Pallets(**data).save()
        return "add successful"

    def bandwidth(self,data):
        bandobj = IdcBandWidth.objects.filter(uid = data['uid'])
        if bandobj is None:
            IdcBandWidth(**data).save()
            return IdcBandWidth.objects.filter(uid = data['uid'])
        else:
           return bandobj

    def excutor(self,name=None,data=None):
        if  name == "pallet":
            result = self.pallet(data)
        elif name == "rack":
            result = self.rack(data)
        elif name == "idc":
            result = self.idc(data)
        else:
            result = "create error"
        return result









