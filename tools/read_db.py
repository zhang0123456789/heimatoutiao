#导包
import pymysql
#创建类
class ReadDB:
    conn=None
    #创建连接数据库的方法
    def get_databse(self,):
        if self.conn is None:
            self.conn=pymysql.connect("127.0.0.1","root","123456","hmtt",charset='utf8')
        return self.conn

    #创建游标对象方法
    def get_cursor(self):
        return self.get_databse().cursor()

    #创建关闭游标对象方法
    def close_cursor(self,cursor):
        if cursor:
            cursor.close()

    #创建关闭连接对象方法
    def close_conn(self):
        if self.conn:
            self.conn.close()
            #关闭连接对象后，对象地址还存在，手工设置为None
            self.conn=None

    #创建获取一条结果方法
    def get_sql_one(self,sql):
        #属性
        cursor=None
        data=None
        try:
            #获取游标对象
            cursor=self.get_cursor()
            #调用执行方法
            cursor.execute(sql)
            # 获取结果
            data=cursor.fetchone(sql)
        except Exception as e:
            print("get_sql_one error:{}".format(e))
        finally:
            #关闭游标对象
            self.close_cursor(cursor)
            #关闭连接
            self.close_conn()
            return data

    # 创建获取所有结果方法
    def get_sql_all(self, sql):
        # 属性
        cursor = None
        data = None
        try:
            # 获取游标对象
            cursor = self.get_cursor()
            # 调用执行方法
            cursor.execute(sql)
            # 获取结果
            data = cursor.fetchall(sql)
        except Exception as e:
            print("get_sql_all error:{}".format(e))
        finally:
            # 关闭游标对象
            self.close_cursor(cursor)
            # 关闭连接
            self.close_conn()
            return data

    # 修改、删除、新增
    def update_sql(self, sql):
        # 属性
        cursor = None
        data = None
        try:
            # 获取游标对象
            cursor = self.get_cursor()
            # 调用执行方法
            cursor.execute(sql)
            # 提交事务，无获取结果
            self.conn.commit()
        except Exception as e:
            # 事务回滚
            self.conn.rollback()
            print("get_sql_one error:{}".format(e))
        finally:
            # 关闭游标对象
            self.close_cursor(cursor)
            # 关闭连接
            self.close_conn()
