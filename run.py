# -*- coding: utf-8 -*-
import pytest
import os
import subprocess
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()



def init_report():
    cmd = "allure generate ./result/ -o ./reports/ --clean"
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/" + "index.html"
    logger.info("报告地址:{}".format(report_path))


# pytest.main(["-s", "testsuites_new", "--alluredir=./result/","--clean-alluredir"])
# pytest.main(["-s", "D:\workspace_new/ios_auto2/testsuites_new/test_001_gift_send_coin.py","--alluredir=./result/","--clean-alluredir"])
pytest.main(["-s", "D:\workspace_new\ios_auto2\ios_auto/testsuites_new/test_017_banner_click.py","--alluredir=./result/","--clean-alluredir"])
init_report()
