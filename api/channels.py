import requests

class ApiChannel:
    def api_get_channel(self,url,headers):
        return  requests.get(url,headers)