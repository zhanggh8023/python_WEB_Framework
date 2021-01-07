# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @Software: PyCharm
import time
from python_WEB_Framework.PageObjects.BasePage import BasePage


class UserInfo_Page(BasePage):

    # 元素定位
    # 个人可用余额
    user_leftMoney = '//*[@class="personal_info"]//li[@class="color_sub"]'
    # 个人详情页面 - 我的投资项目tab
    investRecords_tab_xpath = "//div[text()='投资项目']"
    # 个人详情页面 -  第一条投资记录
    first_investRecord_xpath = '//table[@class="deal_mange_tab"]//tr'
    #投资记录中，标名对应的属性值
    investRecord_loanName = '//*[@ms-html="item.title"]/a'

    #获取用户的余额
    def get_userLeftMoney(self):
        ele = self.find_element(self.user_leftMoney)
        self.scroll_intoView(ele)
        money = ele.text
        #截取数字部分
        money = money.split("元")
        return money[0]

    #点击投资Tab - 展开投资记录
    def click_investRecord_tab(self):
        ele = self.find_element(self.investRecords_tab_xpath)
        self.scroll_intoView(ele)
        ele.click()
        time.sleep(0.5)

    #获取第一条投资记录 的 标名
    def get_firstLoanName_byInvestRecord(self):
        ele = self.find_element(self.first_investRecord_xpath)
        self.scroll_intoView(ele)
        #获取对应的标名
        return self.find_element(self.first_investRecord_xpath+self.investRecord_loanName).text





