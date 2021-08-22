import unittest,requests
from api.channels import ApiChannel
from tools.read_json import ReadJson
from parameterized import parameterized

def get_channel_data():
    # 读取channel数据的接收
    data = (ReadJson('channel.json').read_json())
    arrs = []
    arrs.append(
        (data.get("url"), data.get("headers"), data.get("expect_code"), data.get("message")))
    print(arrs)

class TestChannel(unittest.TestCase):
    @parameterized.expand(get_channel_data())
    def test_channel(self,url,headers,expect_code,message):
        # url="http://ttapi.research.itcast.cn/app/v1_0/users/channel"
        # headers={
        #     "Content-type": "application/json",
        #     "Authorization":"Bear Token信息"
        # }

        resp=ApiChannel().api_get_channel(url,headers=headers)
        print(resp.json())
        # self.assertEquals(200, resp.status_code)
        # self.assertEquals("OK", resp.json()['message'])

        # 断言
        self.assertEquals(expect_code,resp.status_code)
        self.assertEquals(message,resp.json()['message'])

if __name__ == '__main__':
    unittest.main()