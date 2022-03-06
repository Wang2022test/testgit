# -*- coding: utf-8 -*-
# @Time : 2021/12/15 22:37
# @Author : shelly
# @File : demo.py
# @Desc :
from selenium import webdriver
import time
time.sleep(3)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s= Service(r"E:\online_learning\module1\B_web_selenium\selenium_day6\script\driver\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
print(driver)
driver.get("https://www.baidu.com")
time.sleep(3)
driver.find_element(By.ID,"kw").send_keys("软件测试")
driver.find_element(By.ID,"su").click()
# driver.find_element_by_id("kw").send_keys("软件测试")
# driver.find_element_by_id("su").click()