# -*- coding：utf-8 -*-
# @Time ：2022/4/3 21:50
# @Authon :hhj
# @Annotation:
# @File : test_login.py
# import pytest
# from time import sleep
#
# from Common.my_log import MyLog
# from PageObjects.WelcomePage.welcome_page import WelcomePage
# from PageObjects.IndexPage.index_page import IndexPage
# from TestDatas import welcome_datas as WD
# my_log = MyLog()
# class TestLogin:
#
#     # 有隐私保护政策，点击用户协议or隐私政策
#     @pytest.mark.parametrize("user_or_policy_data", WD.user_or_policy_data)
#     @pytest.mark.usefixtures("start_function_App")  # 在运行的时候，会去运行start_function_App函数
#     @pytest.mark.demo3
#     def test_welcome_0_user_policy(self, start_function_App, user_or_policy_data):
#         my_log.info("****{}****".format(user_or_policy_data['title']))
#         driver = start_function_App[0]
#         wel = WelcomePage(driver)
#         sleep(3)
#         res = wel.show_privacy_user_agreement_or_policy(user_or_policy_data['click'])
#         assert res == user_or_policy_data['check']

