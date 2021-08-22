import requests

class ApiArticle:
    def api_post_collect_article(self,url,headers,data):
        return  requests.post(url,headers,data)

    def api_delete_collect_article(self,url,headers):
        return  requests.delete(url,headers)