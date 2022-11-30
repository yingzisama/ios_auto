# -*- coding: utf-8 -*-
import wda
import os
from config import *
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


class Driver():
    def init_driver(self):
        try:
            logger.info('ios设备启动初始化')
            d = wda.Client('http://localhost:8100')
            wda.DEBUG = False # default False
            wda.HTTP_TIMEOUT = 180.0 # default 180 seconds
            wda.DEVICE_WAIT_TIMEOUT = 180.0
            d.implicitly_wait(5)
            logger.info("已连接设备")
            return d
        except Exception as e:
            logger.info("初始化ios_driver异常!{}".format(e))

