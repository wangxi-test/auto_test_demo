import jsonpath
import requests


class ApiKey:
    # get请求
    def get(self,url,params=None,**kwargs):
        return requests.get(url,params=params,**kwargs)

    # post请求
    def post(self,url,data=None,**kwargs):
        return requests.post(url,data=data,**kwargs)