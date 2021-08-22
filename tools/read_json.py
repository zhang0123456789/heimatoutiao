
import json

class ReadJson:

    def __init__(self,filename):
        self.filename='../data/'+filename

    def read_json(self):
        with open(self.filename,'r',encoding='utf-8') as f:
            return json.load(f)

if __name__ == '__main__':
    # 读取登录数据的json
    # data = (ReadJson('login.json').read_json())
    # arrs = []
    # arrs.append(
    #     (data.get("url"), data.get("mobile"), data.get("code"), data.get("status_code"), data.get("expect_result")))
    # print(arrs)


    # 读取channel数据的接送
    # data = (ReadJson('channel.json').read_json())
    # arrs = []
    # arrs.append(
    #     (data.get("url"), data.get("headers"), data.get("expect_code"), data.get("message")))
    # print(arrs)

    # 读取collect_article数据的接送
    # data = (ReadJson('collect_article.json').read_json())
    # arrs = []
    # arrs.append(
    #     (data.get("url"), data.get("headers"), data.get("expect_code"),data.get("data") ,data.get("message")))
    # print(arrs)

    # 读取article_cancle数据的接送
    data = (ReadJson('article_cancel.json').read_json())
    arrs = []
    arrs.append(
        (data.get("url"), data.get("headers"), data.get("expect_code")))
    print(arrs)