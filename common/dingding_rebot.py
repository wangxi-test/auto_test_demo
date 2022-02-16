import json
import requests
from common.dingding_check import dingding_check

def sendmessage():
    timestamp,sign=dingding_check('SECea7f88d91f8b6a7a3ed0cb34a88fc6669c8094ad636d8df38dfa76a750f00901')
    print(timestamp,sign)
    url = 'https://oapi.dingtalk.com/robot/send?access_token=27587e7997015c41731d49962cb34913d615a587d490054c2e9f66b3b9938722&timestamp={}&sign={}'.format(timestamp,sign)  # 钉钉机器人的webhook地址
    print(url)
    HEADERS = {
    "Content-Type":"application/json ;charset=utf-8 "
    }
    print(url)
    String_textMsg = {}
    print(url,String_textMsg,HEADERS)
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    print(res.status_code)
    print(res.text)
    print(res.status_code)
    print(res.status_code)
    print(res.status_code)
    # return res


if '__name__' == '__main__':
    sendmessage()