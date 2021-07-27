import json
from lib.requests import req
import subprocess
from collector.f5__lb_pool import pool


req = req()

def req_pool(): 
    pool().fillter()

def req_viturl():
    print(req.connect_api("viturl"))

def req_node():
    print(req.connect_api("node"))

def req_rule():
    print(req.connect_api("rule"))


if __name__=='__main__':
    req_pool()











