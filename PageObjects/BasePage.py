# -*- coding: utf-8 -*-
# @Author  : zgh
# @Email   : 849080458@qq.com
# @Software: PyCharm
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Common.dir_config import *
from Common import myLogger2
import logging
import time



class BasePage:

    # 初始化
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    #等待元素可见
    def wait_eleVisible(self,locator,by=By.XPATH,wait_times=40):
        if by not in By.__dict__.values():
            logging.error("定位类型不在支持类型内。请修改定位类型。")
        #开始时间
        t1 = time.time()
        try:
            WebDriverWait(self.driver,wait_times,1).until(EC.visibility_of_element_located((by,locator)))
            t2 = time.time()
            # 结束时间 - 两者之差就是真正的等待时间
            logging.info("wait element visible start time：{0}，end time：{1},total wait times is: {2}".format(t1, t2, t2 - t1))
        except Exception as e:
            #截屏
            file_path = os.path.join(screenshot_dir,"{0}.png".format(time.ctime()))
            self.driver.save_screenshot(file_path)
            #打印日志
            logging.exception("等待元素超时，没有找到相应的元素。截屏文件为：{0}".format(file_path))
            #抛出异常
            raise e


    #查找元素 - 一个元素
    def find_element(self,locator,by=By.XPATH,wait_times=40):
        logging.info("当前元素定位类型：{0}，当前查找的元素为：{1}".format(by,locator))
        self.wait_eleVisible(locator,by,wait_times)
        ele = self.driver.find_element(by,locator)
        return ele

    #查找多个元素
    def find_elements(self,locator,by=By.XPATH,wait_times=40):
        self.wait_eleVisible(locator, by, wait_times)
        eles = self.driver.find_elements(by, locator)
        return eles

    # 获取当前页面的url
    def get_url(self):
        return self.driver.current_url

    #滚动到可见区域
    def scroll_intoView(self,ele):
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
