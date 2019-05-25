import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
import time


# 测试用例路径和测试报告路径
test_dir = "./test_case"
report_dir = "./reports"

# 自动加载测试用例
suite = unittest.defaultTestLoader.discover(test_dir)

# 定义报告文件的格式
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir+'/'+now+' test_report.html'

# 运行用例生成测试报告
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="weather api test report", description="china city weather report")
    runner.run(suite)

