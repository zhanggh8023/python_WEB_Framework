# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @Software: PyCharm
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas.login_testdata import *
from TestDatas.CommonData import *
from selenium import webdriver
import time
from Common import myLogger2
import logging
import pytest
class Test_Login:
    @pytest.fixture
    def init_driver(self):
        self.driver = webdriver.Chrome()
        self.lp = LoginPage(self.driver)
        yield
        self.driver.quit()

    #用例一 ：登陆成功
    @pytest.mark.smoke
    def test_1_login_success(self,init_driver):
        logging.info("========开始执行测试用例：登陆成功用例=========")
        #步骤
        self.lp.login(web_url,login_success_datas["username"],login_success_datas["passwd"])
        # 结果比对
        time.sleep(3)
        ip = IndexPage(self.driver)
        assert ip.get_url() == login_success_datas["check_url"]
        assert ip.get_nickname() == login_success_datas["check_nickname"]
    #用例二 ：没有用户名
    def test_2_login_noUsername(self,init_driver):
        logging.info("========开始执行测试用例：登陆成功用例=========")
        # 步骤
        self.lp.login(web_url,login_noUser_datas["username"], login_noUser_datas["passwd"])
        # 结果比对
        time.sleep(3)
        url = self.lp.get_url()
        wrong_msg = self.lp.get_wrongMsg_from_noUserPaswd()
        assert url == login_noUser_datas["check_url"]
        assert wrong_msg == login_noUser_datas["check_msg"]
