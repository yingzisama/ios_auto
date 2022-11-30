# -*- coding: utf-8 -*-
from tools.loggers import JFMlogging
from module.base import Base
import time
import allure
logger = JFMlogging().getloger()

# 搜索按钮
ele_iv_search = 'icons home search white'
# 搜索输入框
ele_et_search = '//*[@label=""]'
# 确认
ele_search = '搜索'
# 搜索的首个直播间
ele_host_name = '//Table/Cell[1]/StaticText[1]'
# 礼物面板-小象stab
ele_liveroom_ele_tab = '小象'
# 礼物面板-特权stab
ele_liveroom_tequan_tab = '特权'
# 礼物面板-趣味stab
ele_liveroom_quwei_tab = '趣味'
# 礼物面板-浪漫stab
# ele_gift_tab_hot = '浪漫'
# 礼物面板-象豆stab
ele_liveroom_bean_tab = '象豆'
# 礼物面板-热门stab
ele_liveroom_hot_tab = '热门'
# 礼物-啾咪
ele_liveroom_common_coin_gift = '啾咪'
# 礼物-蛋卷寿司
ele_liveroom_common_bean_gift = '蛋卷寿司'
# 礼物-玫瑰
ele_liveroom_grow_gift = '玫瑰'
# 礼物-玫瑰花丛
ele_liveroom_grow_gift_bigmeigui = '玫瑰花丛'
# 礼物-春田花花
ele_liveroom_filter_gift = '春田花花'
# 礼物-王者归来
ele_liveroom_rocket_gift = '王者归来'
# 礼物-幸运钥匙
ele_liveroom_game_gift = '幸运钥匙'
# 礼物-粉丝团
ele_liveroom_fans_gift = '粉丝团'
# 礼物-比心
ele_liveroom_graffiti_gift = '比心'
# 礼物栏-批量按钮
ele_liveroom_gift_sent_batch = "gift num top"
# 礼物栏-背包
ele_liveroom_backpack = 'gift icon bag normal'
# 礼物栏-批量选项-66
ele_liveroom_gift_sent_batch66 = '//Window[1]/Other[2]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Table[1]/Cell[5]'
# 礼物栏-combo赠送
ele_liveroom_gift_sent_combo = 'Combo'
# 礼物栏-象币余额
ele_gift_money = '//Window[1]/Other[2]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Button[1]/StaticText[2]'
# 礼物栏-象豆余额
ele_gift_bean = '//Window[1]/Other[2]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Button[2]/StaticText[2]'

class Audience(Base):
    def __init__(self,driver):
        self.base = Base(driver)

    @allure.step("进入直播间")
    def enter_live_room(self):
        self.base.click(ele_iv_search,'搜索按钮')
        self.base.send_keys(ele_et_search,'Test12284163','输入搜索内容-Test12284163')
        self.base.click(ele_search,'搜索按钮')
        self.base.wait(ele_host_name,'等待直播间出现')
        time.sleep(0.5)
        self.base.click(ele_host_name,'点击直播间')

    @allure.step("打开礼物面板")
    def live_click_gift_button(self):
        self.base.click_xy(0.933, 0.967 ,'点击礼物面板')

    @allure.step('赠送普通象币礼物-啾咪')
    def live_click_gift_qiumi(self):
        self.base.click(ele_liveroom_ele_tab,'点击小象tab')
        time.sleep(1)
        self.base.click(ele_liveroom_common_coin_gift,'点击啾咪')
        time.sleep(1)
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')

    @allure.step('赠送象豆礼物-蛋卷寿司')
    def live_click_20bean_gift(self):
        self.base.swipe_xy(0.512, 0.623,0.168, 0.618)
        self.base.click(ele_liveroom_bean_tab,'点击礼物栏-象豆tab')
        self.base.click(ele_liveroom_common_bean_gift,'点击礼物-蛋卷寿司')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')

    @allure.step('赠送成长礼物-玫瑰')
    def live_click_2coin_grow_gift(self):
        self.base.click(ele_liveroom_quwei_tab,'点击切换到礼物-趣味tab')
        self.base.click(ele_liveroom_grow_gift,'点击成长礼物-玫瑰')
        self.base.wait_time(1)
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')

    @allure.step('赠送成长礼物-玫瑰100次')
    def live_click_100_grow_gift(self):
        self.base.click(ele_liveroom_quwei_tab,'点击切换到礼物-趣味tab')
        self.base.click(ele_liveroom_grow_gift,'点击成长礼物-玫瑰')
        self.base.wait_time(1)
        self.base.click(ele_liveroom_grow_gift,'点击成长礼物-玫瑰')
        self.base.click_more(0.909, 0.96, 100,'赠送按钮')

    # @allure.step('断言-玫瑰花丛(解锁)存在')
    # def assert_big_meigui(self):
    #     self.base.assert_image_findit('./aseert_pic/big_meigui.jpg')

    @allure.step('赠送成长礼物-玫瑰花丛')
    def live_click_grow_gift_bigmeigui(self):
        self.base.click(ele_liveroom_grow_gift_bigmeigui,'点击成长礼物-玫瑰花丛')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')

    @allure.step('赠送滤镜礼物-春田花花')
    def live_click_filter_gift(self):
        self.base.click(ele_liveroom_quwei_tab,'点击切换到礼物-趣味tab')
        self.base.swipe_xy(0.827, 0.806,0.121,  0.806)
        self.base.swipe_xy(0.827, 0.806,0.121,  0.806)
        self.base.click(ele_liveroom_filter_gift,'点击滤镜礼物-春田花花')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')

    @allure.step('赠送横幅-王者归来')
    def live_click_rocket_gift(self):
        self.base.click(ele_liveroom_quwei_tab,'点击切换到礼物-趣味tab')
        self.base.swipe_xy(0.827, 0.806,0.121,  0.806)
        self.base.swipe_xy(0.827, 0.806,0.121,  0.806)
        self.base.swipe_xy(0.827, 0.806,0.121,  0.806)
        self.base.click(ele_liveroom_rocket_gift,'点击横幅礼物-王者归来')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')

    @allure.step('赠送游戏礼物-幸运钥匙')
    def live_click_game_gift(self):
        self.base.swipe_xy(0.512, 0.623,0.168, 0.618)
        self.base.click(ele_liveroom_bean_tab,'点击礼物栏-象豆tab')
        self.base.click(ele_liveroom_game_gift,'点击游戏礼物-幸运钥匙')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')

    @allure.step('赠送粉丝团礼物-粉丝团')
    def live_click_fans_gift(self):
        self.base.click(ele_liveroom_tequan_tab,'点击切换到礼物-特权tab')
        self.base.click(ele_liveroom_fans_gift,'点击游戏礼物-粉丝团')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')

    @allure.step('赠送背包-象币礼物')
    def live_click_backpack_coin_gift(self):
        self.base.click(ele_liveroom_backpack,'点击切换到背包')
        self.base.click(ele_liveroom_backpack_coin_gift,'点击背包-象币礼物')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')

    @allure.step('赠送背包-象豆礼物')
    def live_click_backpack_bean_gift(self):
        self.base.click(ele_liveroom_backpack,'点击切换到背包')
        self.base.click(ele_liveroom_common_bean_gift,'点击背包-象豆礼物')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')

    @allure.step('赠送小象币礼物combo-啾咪')
    def live_click_10coin_gift_combo(self):
        self.base.click(ele_liveroom_ele_tab,'点击礼物栏-小象tab')
        self.base.click(ele_liveroom_common_coin_gift,'点击礼物-啾咪')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')
        self.base.click(ele_liveroom_gift_sent_combo,'点击combo赠送')

    @allure.step('赠送象豆礼物combo-蛋卷寿司')
    def live_click_20bean_gift_combo(self):
        self.base.swipe_xy(0.512, 0.623,0.168, 0.618)
        self.base.click(ele_liveroom_bean_tab,'点击礼物栏-象豆tab')
        self.base.click(ele_liveroom_common_bean_gift,'点击礼物-蛋卷寿司')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')
        self.base.click(ele_liveroom_gift_sent_combo,'点击combo赠送')

    @allure.step('赠送涂鸦礼物-比心')
    def live_click_graffiti_gift(self):
        self.base.click(ele_liveroom_ele_tab,'点击礼物栏-小象tab')
        self.base.click(ele_liveroom_graffiti_gift,'点击礼物-比心')
        self.base.click_more(ele_liveroom_graffiti_center,10,'点击涂鸦区域10次')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')

    @allure.step('批量送礼-啾咪')
    def live_click_10coin_gift_batch66(self):
        self.base.click(ele_liveroom_ele_tab,'点击礼物栏-小象tab')
        self.base.click(ele_liveroom_common_coin_gift,'点击礼物-啾咪')
        self.base.click(ele_liveroom_gift_sent_batch,'点出批量选择')
        self.base.click(ele_liveroom_gift_sent_batch66,'选择批量数66')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')

    @allure.step('批量赠送象豆礼物-蛋卷寿司')
    def live_click_20bean_gift_batch66(self):
        self.base.swipe_xy(0.512, 0.623,0.168, 0.618)
        self.base.click(ele_liveroom_bean_tab,'点击礼物栏-象豆tab')
        self.base.click(ele_liveroom_common_bean_gift,'点击礼物-蛋卷寿司')
        self.base.click(ele_liveroom_gift_sent_batch,'点出批量选择')
        self.base.click(ele_liveroom_gift_sent_batch66,'选择批量数66')
        self.base.click_xy(0.909, 0.96, '点击赠送按钮')


    @allure.step('断言礼物栏-象币余额')
    def assert_gift_balance(self,num):
        self.base.assert_xpath(ele_gift_money,num)

    @allure.step('断言礼物栏-象豆余额')
    def assert_gift_bean_balance(self,num):
        self.base.assert_xpath(ele_gift_bean,num)

    @allure.step('关闭礼物面板')
    def close_gift(self):
        self.base.click_xy(0.528, 0.34,'关闭面板')