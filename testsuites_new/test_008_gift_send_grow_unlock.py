# -*- coding: utf-8 -*-
# 自动化测试用例: 从礼物面板赠送成长类型礼物，解锁成长礼物
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("送礼-解锁成长礼物")
@allure.feature("送礼-解锁成长礼物")
class Test_Gift_Sent_Grow_Unlock:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('解锁成长礼物')
    @allure.title("解锁成长礼物")
    def test_audience_sentgift_grow_unlock(self, init_audience):
        # 还原环境
        ele_function.grow_clear()
        # 进入直播间
        init_audience.enter_live_room()
        # 充值212小象币
        ele_function.add_coin(313)
        # 打开礼物栏
        init_audience.live_click_gift_button()
        # 赠送成长礼物-玫瑰100次
        init_audience.live_click_100_grow_gift()
        # 断言成长礼物-玫瑰花丛icon(解锁后)存在
        # init_audience.assert_big_meigui()
        # 赠送玫瑰花丛
        init_audience.live_click_grow_gift_bigmeigui()
        # 关闭成长礼物栏
        init_audience.close_gift()
        # 断言余额为14
        init_audience.assert_gift_balance('14')
        # 关闭礼物栏面板
        # self.base.back()
        # self.base.back()
        # # 断言评论区出现送礼消息
        # init_audience.assert_gift_message()
