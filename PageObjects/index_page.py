# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @Software: PyCharm
from PageObjects.BasePage import BasePage

class IndexPage(BasePage):
    # 首页 - 我的帐户链接
    home_userInfo_xpath = '//a[@href="/Member/index.html"]'
    #第一个标 - 标名
    firstLoan_loanName_xpath = '//span[@class="fs-22"]'


    #获取当前用户的昵称
    def get_nickname(self):
        #加个等待
        ele = self.find_element(self.home_userInfo_xpath)
        nickname = ele.text
        return nickname

    #选择页面的第一个标
    def click_firstLoan(self):
        #加个等待
        ele = self.find_element(self.firstLoan_loanName_xpath)
        ele.click()

    #获取第一个标的标名
    def get_firstLoanName(self):
        ele = self.find_element(self.firstLoan_loanName_xpath)
        return ele.text


