# -*- coding: utf-8 -*-
# 自动化测试用例: 从礼物面板批量赠送象豆类型礼物
import pytest
from tools.loggers import JFMlogging
import allure
from module.audience import Audience
from tools.ele_function import ele_function
logger = JFMlogging().getloger()

@pytest.mark.usefixtures('driver_setup')
@allure.epic("批量送礼-象豆类型礼物")
@allure.feature("批量送礼-象豆类型礼物")
class Test_Gift_Sent_Bean_Batch:
    @pytest.fixture
    def init_audience(self):
        self.audience = Audience(self.driver)
        logger.info("初始化进入直播间")
        self.base = self.audience.base
        yield self.audience
        logger.info("结束进入直播间")

    @allure.story('批量赠送象豆类型礼物')
    @allure.title("批量赠送象豆类型礼物")
    def test_audience_sentgift_coin_batch(self, init_audience):
        # 进入直播间
        init_audience.enter_live_room()
        # 充值1331象豆
        ele_function.add_bean(1331)
        # 打开礼物栏
        init_audience.live_click_gift_button()
        # 批量赠送20象豆礼物66个
        init_audience.live_click_20bean_gift_batch66()
        # 断言余额为77
        init_audience.assert_gift_bean_balance('11')
        # 关闭礼物栏面板
        # self.base.back()
        # 断言评论区出现送礼消息
        # init_audience.assert_gift_message()