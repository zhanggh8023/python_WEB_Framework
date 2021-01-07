# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @Software: PyCharm
from PageObjects.BasePage import BasePage

class LoanInfo_Page(BasePage):

    #元素定位
    # 标详情页面 - 投资金额输入处
    invest_moneyInput_xpath = '//input[@data-url="/Invest/invest"]'
    # 标详情页面 - 投标按钮
    invest_moneySubmit_xpath = "//button[text()='投标']"
    #投资成功 - 弹出框
    invest_success_popup_xpath = '//div[contains(@class,"layui-layer-page")]'
    #投资成功弹出框 - 获取 成功的提示消息
    invest_success_msg_xpath = '//div[contains(@class,"layui-layer-page")]//*[contains(@class,"capital_font1")]'
    #投资成功弹出框  查看并激动 - 按钮
    invest_success_activeButton_xpath = '//div[contains(@class,"layui-layer-page")]//button'
    #投资失败 - 弹出框 - 提示信息
    invest_failed_popup_xpath = '//div[contains(@class,"layui-layer-dialog")]//div[@class="text-center"]'

    #投资行为
    def invest(self,money):
        #等待金额输入框出现
        ele = self.find_element(self.invest_moneyInput_xpath)
        self.scroll_intoView(ele)
        #输入金额
        ele.send_keys(money)
        #提交投资
        ele = self.find_element(self.invest_moneySubmit_xpath)
        self.scroll_intoView(ele)
        ele.click()

    #投资成功弹出框 - 获取投标成功的提示
    def get_investSuccess_msg(self):
        ele = self.find_element(self.invest_success_popup_xpath)
        #返回弹出框中的消息。
        return ele.text

    #点击查看并激动 - 跳转到个人页面
    def click_popup_activeButton(self):
        #点击
        self.find_element(self.invest_success_activeButton_xpath).click()

    #获取个人余额
    def get_userLeftMoney(self):
        ele = self.find_element(self.invest_moneyInput_xpath)
        # 获取金额输入框的data-amount属性值;
        return ele.get_attribute("data-amount")

    #获取投资失败时的，提示信息
    def get_investFailed_msg(self):
        ele = self.find_element(self.invest_failed_popup_xpath)
        return ele.text
