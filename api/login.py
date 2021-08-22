'''目的：实现登录接口封装'''

'''导包  requests'''
import requests

'''建立class  登录接口对象'''
class ApiLogin():
    '''建立def  登录方法'''
    def post_api_login(self,url,mobile,code):
        '''定义url'''
        headers={"Content-type": "application/json"}
        '''定义data'''
        data = {"mobile":mobile,"code":code}
        '''调用post请求方法，参数接受'''
        rep = requests.post(url=url, headers=headers, data=data)
        '''返回结果'''
        return rep

""""
    注意：url,mobile,code,最后都是从execl读取，所以采用动态传参
"""