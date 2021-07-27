from lib.requests import req
from lib.requests import req
import pandas as pd 
from flatten_json import flatten
req = req()
    
class pool:
    def fillter(self):
        pool_res = req.connect_api("pool")
        #logs = flatten(pool_res)
        print(pool_res)