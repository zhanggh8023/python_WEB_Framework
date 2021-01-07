# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @Software: PyCharm

import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]


testcase_dir = os.path.join(base_dir,"TestCases")

htmlreport_dir = os.path.join(base_dir,"HtmlReport")

logs_dir = os.path.join(base_dir,"Logs")

screenshot_dir = os.path.join(base_dir,"ScreenShot")