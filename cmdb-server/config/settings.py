# -*- coding: utf-8 -*-
import yaml
def parseconfig():
    f = open('config/config.yml',encoding="utf-8")
    x = yaml.load(f)
    return x

