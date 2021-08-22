import unittest,time
from HTMLTestRunnerNew import HTMLTestRunner

#组装测试套件
suite=unittest.defaultTestLoader.discover('./case',pattern='test*.py')
#指定报告存放的路径及位置
filepath='./report/{}.html'.format(time.strftime('%Y_%m_%d %H_%M_%S'))

#运行测试套件并生产测试报告
with open(filepath,"wb") as f:
    HTMLTestRunner(stream=f).run(suite)

