# -*- coding: utf-8 -*-
# @Time : 2021/12/17 21:12
# @Author : shelly
# @File : config.py
# @Desc :

import sys
import os
# print(os.getcwd())
# print(os.path.dirname(os.path.dirname(__file__)))
driver_path=f"{os.path.dirname(os.path.dirname(__file__))}\driver\chromedriver.exe"
url="http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html"
file=r"E:\online_learning\module1\B_web_selenium\selenium_day6\script\data\testdata.xlsx"
sheet="login"
log_path=r"E:\online_learning\module1\B_web_selenium\selenium_day6\script\log\log.txt"