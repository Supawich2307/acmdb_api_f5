from requests.api import request
from lib.config import authen,api
import json


class req:
    def __init__(self) :
        for data in authen["user"]:
            self.token = data["token"]
        print(self.token)
    
    def get(self,url):
        payload={}
        headers = {
        'X-F5-Auth-Token': self.token
        }
        response = request("GET", url, headers=headers, data=payload)
        return response
    
    def connect_api(self,attribute):
        url = self.find_url(attribute)
        response = self.get(url)
        #print(type(response.text))
        if response.status_code == 200 :
            text_res = json.loads(response.text)
            text_dump = json.dumps(text_res,ensure_ascii=False,indent=2)
        else :
            print("can not connect ",url)
        #return json.dumps(response,ensure_ascii=False,indent=2)
        return text_dump
    
    def find_url(self,attribute):
        for loop_address in api["f5_lb"]:
            address = loop_address["address"]
            for loop_uri in loop_address[attribute]:
                uri = loop_uri["uri"] 
        print(address+uri)
        return address+uri

