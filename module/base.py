# -*- coding: utf-8 -*-
import re, time
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


class Base(object):

    def __init__(self, driver):
        self.d = driver

    def click(self, label_name, log_text):
        """
        元素点击
        label_name:元素名称
        log_text:打印log的文案
        """
        if re.findall("//", str(label_name)):
            self.d.xpath(label_name).click()
        else:
            self.d(label=label_name).click()
        logger.info("「{}」".format(log_text))

    def click_xy(self, x, y, log_text):
        """
        坐标点击
        x: X坐标
        y: Y坐标
        log_text:打印log的文案
        """
        self.d.click(x,y)
        logger.info("「{}」".format(log_text))

    def send_keys(self, label_name, sendtext, log_text):
        """
        文本输入
        label_name:元素名称
        sendtext:输入的文案
        log_text:打印log的文案
        :return:
        """
        if re.findall("//", str(label_name)):
            self.d.xpath(label_name).set_text(sendtext)
        else:
            self.d(label=label_name).set_text(sendtext)
        logger.info("「{}」".format(log_text))

    def wait(self, label_name, log_text):
        """
        文本输入
        label_name:元素名称
        log_text:打印log的文案
        :return:
        """
        if re.findall("//", str(label_name)):
            self.d(xpath=label_name).wait(timeout=10.0) # 等待元素出现
        else:
            self.d(label=label_name).wait(timeout=10.0) # 等待元素出现 
        logger.info("「{}」".format(log_text))

    def assert_xpath(self, label_name,num):
        """
        断言xpath元素的值为num
        label_name:元素名称
        num: 预期值
        log_text:打印log的文案
        :return:
        """
        real_num = self.d(xpath=label_name).get().value
        assert real_num == num, "断言「{}」元素值为「{}」,失败了!".format(real_num,num)
        logger.info("断言「{}」元素值为「{}」,成功了!".format(real_num,num))

    def assert_exists(self, label_name):
        """
        断言label元素存在
        label_name:元素名称
        :return:
        """
        time.sleep(0.5)
        assert self.d(label=label_name).exists == True, "断言「{}」元素存在,失败了!".format(label_name)
        logger.info("断言「{}」元素存在,成功了!".format(label_name))

    def swipe_xy(self,x1,y1,x2,y2):
        """
        x1y1滑动到x2y2
        :return:
        """
        self.d.swipe(x1, y1, x2, y2, 0.5)

    def click_more(self,x,y,num,log_text):
        """
        坐标点击多次
        x:横坐标
        y:纵坐标
        num:点击次数
        """
        for i in range(num):
            self.d.click(x,y)
        logger.info("点击元素:「{}」「{}」次 ".format(log_text,num))

    def wait_time(self,timeout=2):
        """
        等待
        num:等待时间
        """
        time.sleep(timeout)