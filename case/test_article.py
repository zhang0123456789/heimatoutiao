import unittest
from api.article import ApiArticle
from tools.read_json import ReadJson
from parameterized import parameterized

def collect_article_data():
    data = (ReadJson('collect_article.json').read_json())
    arrs = []
    arrs.append(
        (data.get("url"), data.get("headers"), data.get("expect_code"), data.get("data"), data.get("message")))
    return arrs

# 读取article_cancle数据的接送
def article_cancel_data():
    data = (ReadJson('article_cancel.json').read_json())
    arrs = []
    arrs.append(
        (data.get("url"), data.get("headers"), data.get("expect_code")))
    return arrs

class TestArticle(unittest.TestCase):
    @parameterized.expand(collect_article_data)
    def test01_collect_article(self,url,headers,data,expect_code,message):
        # url="http://ttapi.research.itcast.cn/app/v1_0/users/collect"
        # headers ={"Content-type": "application/json",
        #     "Authorization":"Bear Token信息"}
        # data={"target":1}
        resp=ApiArticle().api_post_collect_article(url,headers,data)
        print("收藏文章响应信息：{}".format(resp.json()))
        # self.assertEquals(201,resp.status_code)
        # self.assertEquals("OK",resp.json()["message"])

        self.assertEquals(expect_code, resp.status_code)
        self.assertEquals(message, resp.json()["message"])



    @parameterized.expand(article_cancel_data())
    def test02_delete_articel(self,url,headers,expect_code):
        # url = "http://ttapi.research.itcast.cn/app/v1_0/users/collect/1"
        # headers = {"Content-type": "application/x-www-form-urlencoded",
        #            "Authorization": "Bear Token信息"}
        resp = ApiArticle().api_delete_collect_article(url,headers)
        print("收藏文章响应信息：{}".format(resp.json()))
        # self.assertEquals(204, resp.status_code)

        self.assertEquals(expect_code, resp.status_code)

if __name__ == '__main__':
    unittest.main()