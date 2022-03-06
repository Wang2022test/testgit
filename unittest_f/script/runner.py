# -*- coding: utf-8 -*-
# @Time : 2021/12/15 20:43
# @Author : shelly
# @File : runner.py.py
# @Desc :
import unittest
from BeautifulReport import BeautifulReport


#加载准备好的测试用例
cases=unittest.defaultTestLoader.discover(start_dir=r"E:\online_learning\module1\B_web_selenium\selenium_day6\script\testcases",pattern='test*.py')
#执行测试用例
result=BeautifulReport(cases)
#生成测试报告
result.report(description="系统用户的测试报告",filename="SIT测试报告",report_dir=r"E:\online_learning\module1\B_web_selenium\selenium_day6\script\report")