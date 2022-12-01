# -*- coding: utf-8 -*-
# 自动化测试用例: 从礼物面板赠送游戏礼物
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
import time
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("送礼-游戏礼物")
@allure.feature("送礼-游戏礼物")
class Test_Gift_Sent_Game:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('赠送游戏礼物')
    @allure.title("赠送游戏礼物")
    def test_audience_sentgift_game(self, init_audience):
        # 进入直播间
        init_audience.enter_live_room()
        # 充值12小象币
        ele_function.add_bean(67)
        # 打开礼物栏
        init_audience.live_click_gift_button()
        # 赠送热门-幸运钥匙
        init_audience.live_click_game_gift()
        # # 关闭礼物栏
        # init_audience.close_gift()
        # # 查看象豆
        # init_audience.live_click_gift_button()
        # time.sleep(1)
        # 断言余额为57
        init_audience.assert_gift_bean_balance(57)
        # 关闭礼物栏面板
        # self.base.back()
        # # 断言评论区出现送礼消息
        # init_audience.assert_gift_message()