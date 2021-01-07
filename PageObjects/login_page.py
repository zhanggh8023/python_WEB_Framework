# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @Software: PyCharm
from PageObjects.BasePage import BasePage

class LoginPage(BasePage):
    #
    login_username_xpath= "//*[@name='phone']"
    #
    login_passwd_xpath = "//*[@name='password']"
    #
    login_button_xpath = "//button"
    #用户名为空时 - 提示元素
    login_noUserPaswd_xpath = '//div[@class="form-error-info"]'
    #提示 - 页面中间提示信息
    login_wrongUserPaswd_xpath= "//div[@class='layui-layer-content']"

    #只写操作步骤
    def login(self,url,username,passwd):
        self.driver.get(url)
        #找到登陆用户名
        self.find_element(self.login_username_xpath).send_keys(username)
        self.find_element(self.login_passwd_xpath).send_keys(passwd)
        self.find_element(self.login_button_xpath).click()

    def register(self):
        #driver.find
        pass

    def get_wrongMsg_from_noUserPaswd(self):
        return self.find_element(self.login_noUserPaswd_xpath).text

    #获取到错误的提示 - 用户名或者密码错误的时候。
    def get_wrongMsg_from_pageCenter(self):
        return self.find_element(self.login_wrongUserPaswd_xpath).text


