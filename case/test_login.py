'''
导包 unittest ApiLogin
新建测试类  必须继承unittest.TestCase
新建测试方法，test_login()
    参数化数据准备 url、mobile、code
    实例化ApiLogin()类，并调用登录方法
    断言 响应信息，响应状态码
'''

'''解决数据存储问题
步骤：
1、编写数据存储文件 login.json
    位置：data目录下
    内容：{
  "url": "http://ttapi.research.itcast.cn/app/v1_0/authorizations",
  "mobile": "18576437695",
  "code": "",
  "expect_result": "OK",
  "status_code": 201
}
编写读取json工具
使用参数化动态获取参数数据
'''





'''导入包'''
import unittest
from api.login import ApiLogin

from parameterized import parameterized
from tools.read_json import ReadJson


'''读取json里面的数据'''
def get_data():
    data=(ReadJson('login.json').read_json())
    arrs=[]
    arrs.append((data.get("url"),data.get("mobile"),data.get("code"),data.get("status_code"),data.get("expect_result")))
    return arrs

'''新建测试类'''
class TestLogin(unittest.TestCase):
    '''新建测试方法'''
    @parameterized.expand(get_data())
    def test_login(self,url,mobile,code,status_code,expect_result):
        # '''暂存数据'''
        # url="http://ttapi.research.itcast.cn/app/v1_0/authorizations"
        # mobile="18576437595"
        # '''短信验证码，get请求，直接通过浏览器请求，手机收到验证码'''
        # code="882477"

        s = ApiLogin().post_api_login(url,mobile,code)
        print(s.json()) #json中包含有token信息
        # self.assertEquals("OK", s.json()['mseeage'])
        # self.assertEquals("201", s.status_code)
        self.assertEquals(expect_result,s.json()['mseeage'])
        self.assertEquals(status_code,s.status_code)

if __name__ == '__main__':
    unittest.main()


