# -*- coding: utf-8 -*-
import subprocess, pytest, time, allure
import base64
from ios_driver import Driver
from config import *
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


@pytest.fixture()
def driver_setup(request):
    logger.info("自动化测试开始!")
    request.instance.driver = Driver().init_driver()
    logger.info("driver初始化")
    request.instance.driver.app_activate(pck_name)
    time.sleep(launch_time)

    def driver_teardown():
        logger.info("自动化测试结束!")
        # request.instance.driver.watcher.remove()
        request.instance.driver.session().app_terminate(pck_name)
    request.addfinalizer(driver_teardown)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    hook pytest失败
    :param item:
    :param call:
    :return:
    """
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")

def screen_shot(driver):
    """
    截图操作
    pic_name:截图名称
    :return:
    """
    try:
        fail_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        fail_pic = str(fail_time) + "截图"
        pic_name = os.path.join(screenshots_folder, fail_pic)
        driver.screenshot("{}.png".format(pic_name))
        logger.info('截图:{}'.format(pic_name))
        f = open(pic_name, 'rb')  # 二进制方式打开图文件
        base64_str = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()
        return base64_str
    except Exception as e:
        logger.info("{}截图失败!{}".format(pic_name, e))

