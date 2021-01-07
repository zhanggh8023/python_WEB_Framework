# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @Software: PyCharm
from PageObjects.index_page import IndexPage
from PageObjects.loanInfo_page import LoanInfo_Page
from PageObjects.userInfo_page import UserInfo_Page
from TestDatas.invest_testdata import *
import pytest

@pytest.mark.usefixtures("init_env")
class Test_Invest:

    def test_invest_sucess(self,init_env):
        #步骤
        #实例化首页对象，首页点击第一个标名
        index_p = IndexPage(init_env)
        invest_loanName = index_p.get_firstLoanName()
        index_p.click_firstLoan()
        #进入标的详情页面后，获取当前用户余额，实例化标详情页面对象
        loan_p = LoanInfo_Page(init_env)
        userMoney_beforeInvest = loan_p.get_userLeftMoney()
        #输入金额，并提交投标操作
        loan_p.invest(invest_success_datas["money"])
        #投标成功弹出框出现，获取其提示信息
        success_msg = loan_p.get_investSuccess_msg()
        #点击激活并查看按钮 ，进入个人页面
        loan_p.click_popup_activeButton()
        #校验 - 实例化个人页面对象
        user_p = UserInfo_Page(init_env)
        #获取用户当前余额
        userMoney_afterInvest = user_p.get_userLeftMoney()
        #查看用户投资记录的第一条，获取标名。
        user_p.click_investRecord_tab()
        investRecord_loanName = user_p.get_firstLoanName_byInvestRecord()
        #比对余额差，投资记录的标名是否正确。
        assert success_msg.find(invest_success_datas["check_success_msg"]) != -1
        assert invest_success_datas["check_less_money"] == int(float(userMoney_beforeInvest))-int(float(userMoney_afterInvest))
        assert invest_loanName == investRecord_loanName

    def test_invest_no100(self,init_env):
        pass