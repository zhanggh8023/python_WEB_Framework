# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @Software: PyCharm
import pytest

if __name__ == "__main__":

    pytest.main(["-m","smoke","--html","HtmlReport/report.html","--junitxml","HtmlReport/report.xml"])
