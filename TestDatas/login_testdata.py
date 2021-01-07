# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @Software: PyCharm
#测试数据 - 成功登陆
login_success_datas = {
    "username":"18684720553",
    "passwd":"python",
    "check_url":"http://120.79.176.157:8012/Index/index",
    "check_nickname":"我的帐户[小蜜蜂96027921]"
}

#测试数据 - 没有用户名
login_noUser_datas = {
    "username":"",
    "passwd":"python_test",
    "check_url":"http://120.79.176.157:8012/Index/login.html",
    "check_msg":"请输入手机号"
}
