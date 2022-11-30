# -*- coding: utf-8 -*-
import requests
import pymysql
import json
import redis

userId = 'Test12284166'

class ele_function:
    @staticmethod
    def login():
        now_host = 'http://showmetest3.elelive.cn:10009'
        url = now_host+'/login'
        data = {
        'smsCode':'1234',
        'userCode':'Fish'
        }
        res = requests.post(url,data=data)
        cookies = res.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        (key, value), = cookie.items()
        new_cookie = key + '=' + value
        return new_cookie

    @staticmethod
    def add_coin(ele_coin):
        count = pymysql.connect(
        host = 'mysqltest3.elelive.cn',     
        port = 10634,        
        user='showmetest_app',        
        password='M90JB123kdF95',     
        db= '',  
        charset = 'gbk'     
        )
        count.ping(reconnect = True)
        # 完成mysql数据库实例化
        db1 = count.cursor()
        db1.execute("update account.wallet_info set contributions_balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        count.commit()
        # 查找所以内容
        # db1.execute("SELECT user_id, contributions_balance FROM account.wallet_info where user_id = '%s'" % (userId))
        # result = db1.fetchone()
        # print(result)

    @staticmethod
    def add_bean(ele_coin):
        count = pymysql.connect(
        host = 'mysqltest3.elelive.cn',     
        port = 10634,        
        user='showmetest_app',        
        password='M90JB123kdF95',     
        db= '',  
        charset = 'gbk'     
        )
        count.ping(reconnect = True)
        # 完成mysql数据库实例化
        db1 = count.cursor()
        db1.execute("update wallet.wallet_0 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_1 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_2 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_3 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_4 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_5 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_6 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_7 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_8 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        db1.execute("update wallet.wallet_9 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
        count.commit()

    @staticmethod
    def grow_clear():
        '''清除用户的Test12284166的玫瑰成长礼物的数据库和redis缓存'''
        #数据库
        count = pymysql.connect(
        host = 'mysqltest3.elelive.cn',     
        port = 10634,        
        user='showmetest_app',        
        password='M90JB123kdF95',     
        db= '',  
        charset = 'gbk'     
        )
        count.ping(reconnect = True)
        # 完成mysql数据库实例化
        db1 = count.cursor()
        db1.execute("delete FROM account.user_gift_grows_info where user_id = 'Test12284166'")
        count.commit()

        # 连接redis
        r = redis.StrictRedis(host='47.112.74.18',port=30013,password='showmeTEST_3318',db=0,decode_responses=True)
        # 删除key的数据
        r.delete("USER_GIFT_GROWABLE_ENABLE_11839791_202")
        # print(r.smembers('USER_GIFT_GROWABLE_11839791_202'))
        r.delete("USER_GIFT_GROWABLE_11839791_202")
        # print(r.hgetall("USER_GIFT_GROWABLE_11839791_202"))

    @staticmethod
    def fans_clear():
        '''清除用户粉丝身份'''
        #数据库
        count = pymysql.connect(
        host = 'mysqltest3.elelive.cn',     
        port = 10634,        
        user='showmetest_app',        
        password='M90JB123kdF95',     
        db= '',  
        charset = 'gbk'     
        )
        count.ping(reconnect = True)
        # 完成mysql数据库实例化
        db1 = count.cursor()
        db1.execute("delete FROM fansclub.cmedal_info where user_id = 'Test12284166'")
        db1.execute("delete FROM fansclub.exp_record_info WHERE user_id = 'Test12284166'")
        db1.execute("delete FROM  fansclub.fans_joint_history_record_info WHERE user_id = 'Test12284166'")
        count.commit()

        r = redis.StrictRedis(host='47.112.74.18',port=30013,password='showmeTEST_3318',db=0,decode_responses=True)
        r.delete("FANS_EXP_CLUB_Test12284166")


if __name__=='__main__':
    ele_function.grow_clear()
    
