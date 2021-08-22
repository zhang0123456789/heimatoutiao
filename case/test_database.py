#导包
import pymysql

#创建连接数据库信息
conn=pymysql.connect("127.0.0.1","root","123456","hmtt",charset='utf8')
#创建游标，后续所有操作都基于游标进行
cursor=conn.cursor()
# sql语句
sql="select is_deleted from new_collection where user_id=1 and article_id=2"
#执行sql语句
cursor.execute('sql')
#获取一条结果
result=cursor.fetchone()
assert 0 ==result[0]
#关闭游标
cursor.close()
#关闭数据库连接
conn.close()