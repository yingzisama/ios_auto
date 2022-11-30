# -*- coding: utf-8 -*-
# 自动化测试用例: 从礼物面板赠送小象币类型礼物combo
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("送礼-小象币类型礼物combo")
@allure.feature("送礼-小象币类型礼物combo")
class Test_Gift_Sent_Coin_Combo:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('赠送小象币类型礼物combo')
    @allure.title("赠送小象币类型礼物combo")
    def test_audience_sentgift_coin_combo(self, init_audience):
        # 进入直播间
        init_audience.enter_live_room()
        # 充值99小象币
        ele_function.add_coin(79)
        # 打开礼物栏
        init_audience.live_click_gift_button()
        # 赠送小象币（10小象币）类型的礼物
        init_audience.live_click_10coin_gift_combo()
        # 断言余额为90
        init_audience.assert_gift_balance('59')
        # 关闭礼物栏面板
        # self.base.back()
        # 断言评论区出现送礼消息
        # init_audience.assert_gift_message()