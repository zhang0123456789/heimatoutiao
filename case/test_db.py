import unittest
from tools.read_db import ReadDB

#新建测试类，继承
class TestDB(unittest.TestCase):
    #新建测试方法
    def test_db(self):
        sql="select is_deleted from new_collection where user_id=1 and article_id=2"
        # 调用get_sql_one方法
        data=ReadDB().get_sql_one(sql)
        #查看返回结果
        print(data)
        #断言
        self.assertEquals(0,data[0])
if __name__ == '__main__':
    unittest.main()