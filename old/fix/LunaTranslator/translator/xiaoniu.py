 
 
from traceback import print_exc
import requests
from urllib import parse 
import os
import json
from utils.config import globalconfig,translatorsetting
import re 
from translator.basetranslator import basetrans 
from js2py import EvalJs
import time
class TS(basetrans):  
    def translate(self,query):
        js=translatorsetting[self.typename]
        if js['args']['apikey']=="":
            return 
        else:
            apikey = js['args']['apikey'] 
        headers = { 
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'no-cache',
            'content-type': 'text/plain;charset=UTF-8', 
            'pragma': 'no-cache',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'none',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
        }
         
        params={
            'from':self.srclang ,
            'to':self.tgtlang,
            'src_text':query,
            'apikey':apikey
        }
        
        response = requests.post('https://api.niutrans.com/NiuTransServer/translation',  headers=headers, params=params, timeout=globalconfig['translatortimeout'],proxies=  {'http': None,'https': None})
        # print(response.json())
        js['args']['字数统计']=str(int(js['args']['字数统计'])+len(query))
        js['args']['次数统计']=str(int(js['args']['次数统计'])+1) 
        #print(res['trans_result'][0]['dst'])
        return response.json()['tgt_text'] 