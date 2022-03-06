# -*- coding: utf-8 -*-
# @Time : 2021/12/15 22:01
# @Author : shelly
# @File : bug.py
# @Desc :
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import win32con
import win32gui

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("打开浏览器")
        s = Service(r"E:\online_learning\module1\B_web_selenium\selenium_day6\script\driver\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()
        cls.driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")

    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")
        cls.driver.quit()

    def setUp(self):
        print("登录")
        self.driver.find_element(By.ID, "account").send_keys("shelly")
        self.driver.find_element(By.NAME, "password").send_keys("p@ssw0rd")
        self.driver.find_element(By.ID, "submit").click()
        sleep(2)

    def tearDown(self):
        print("退出系统")
        self.driver.find_element(By.XPATH, "//a[@class='dropdown-toggle']/span[1]").click()
        self.driver.find_element(By.LINK_TEXT, "退出").click()
#测试用例1
    def addbug_success(self):
        '''成功添加bug'''
        sleep(3)
        self.driver.find_element(By.LINK_TEXT, "测试").click()
        self.driver.find_element(By.XPATH, "//nav[@id='subNavbar']/ul/li[1]/a").click()
        self.driver.find_element(By.LINK_TEXT, "提Bug").click()
        self.driver.find_element(By.CLASS_NAME, "search-field").click()
        self.driver.find_element(By.CLASS_NAME, "active-result").click()
        self.driver.find_element(By.ID, 'title').send_keys("test")
        sleep(2)
        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)
        sleep(1)
        self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[1]/div[1]/div[1]/div[1]/button[1]").click()
        sleep(2)
        dialog = win32gui.FindWindow("#32770", "打开")
        #
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
        # 往编辑当中，输入文件路径 。
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, r"C:\Users\Asus\Desktop\test.jpg")  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        self.driver.find_element(By.ID,"submit").click()
        # sleep(2)
        # print(self.driver.find_element(By.LINK_TEXT, "提Bug").text)
        sleep(3)
        try:
            self.assertEqual(self.driver.find_element(By.LINK_TEXT,"提Bug").text,"提Bug")
            print("创建bug成功")
        except:
            print("添加bug失败")

