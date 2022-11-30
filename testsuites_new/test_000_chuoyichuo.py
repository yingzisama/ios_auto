# coding:gbk
# 自动化测试用例: 进入直播间，弹出戳一戳
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
import time

logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("直播间-戳一戳")
@allure.feature("直播间-戳一戳弹出")
class Test_Chuo_Yi_Chuo:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('等待戳一戳')
    @allure.title("等待戳一戳")
    def test_wait_chuoyichuo(self, init_audience):
        # 进入直播间
        init_audience.enter_live_room()
        # 等待15s
        time.sleep(15)