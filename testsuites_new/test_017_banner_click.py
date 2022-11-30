# -*- coding: utf-8 -*-
# 自动化测试用例: 首页点击banner成功跳转
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("点击-banner")
@allure.feature("点击-banner")
class Test_Banner_Click:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('点击首页banner')
    @allure.title("点击首页banner")
    def test_click_banner(self, init_audience):
        # 进入印尼地区推荐页(点击发现-越南)
        init_audience.live_click_VNpage()
        # 点击banner，跳转到指定直播间
        init_audience.live_click_banner()
        # 断言直播间元素存在
        init_audience.assert_live_room()
        