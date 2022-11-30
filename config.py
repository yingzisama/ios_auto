# -*- coding: utf-8 -*-
import os

# 全局配置
pck_name = "com.yiwuzhibo.yiwu"   # 包名
wait_timeout = 5
launch_time = 1
current_path = os.path.abspath(os.path.dirname(__file__))
screenshots_folder = os.path.join(current_path, "screenshots")
if not os.path.exists(screenshots_folder):
    os.mkdir(screenshots_folder)
    print("创建截图目录:{}".format(screenshots_folder))
