# -*- coding：utf-8 -*-
# @Time ：2022/4/5 17:10
# @Authon :hhj
# @Annotation:
# @File : test_welcome.py
from time import sleep

import allure
import pytest

from Common.my_log import MyLog
from PageObjects.WelcomePage.welcome_page import WelcomePage
from PageObjects.IndexPage.index_page import IndexPage
from TestDatas import welcome_datas as WD
from Common.system_properties import SystemProperties

my_log = MyLog()


@allure.feature("引导页")
class Test0Welcome:

    # 有隐私保护政策，点击用户协议or隐私政策
    @pytest.mark.parametrize("user_or_policy_data", WD.user_or_policy_data)
    @pytest.mark.usefixtures("start_function_App")  # 在运行的时候，会去运行start_function_App函数
    @pytest.mark.smoke
    @allure.story("点击用户协议or隐私政策")
    @allure.description("点击用户协议or隐私政策")  # 用例的描述
    @allure.severity(allure.severity_level.BLOCKER)
    def test_welcome_0_user_policy(self, common_driver, device, user_or_policy_data):
        allure.dynamic.title("{}:{}".format(user_or_policy_data['title'], device["device"]))
        my_log.info("****{}****".format(user_or_policy_data['title']))
        driver = common_driver[0]
        wel = WelcomePage(driver)
        sleep(3)
        res = wel.show_privacy_user_agreement_or_policy(user_or_policy_data['click'])
        with allure.step("step：断言文案是否为{}？".format(user_or_policy_data['check'])):
            assert res == user_or_policy_data['check']

    # 有隐私保护政策，点击用户协议or隐私政策后返回
    @pytest.mark.parametrize("user_or_policy_data", WD.user_or_policy_data)
    @pytest.mark.usefixtures("start_function_App")  # 在运行的时候，会去运行start_function_App函数
    @pytest.mark.smoke
    @allure.story("点击用户协议or隐私政策后返回")
    @allure.description("点击用户协议or隐私政策后返回")  # 用例的描述
    @allure.severity(allure.severity_level.BLOCKER)
    def test_welcome_1_user_policy(self, common_driver, device, user_or_policy_data):
        allure.dynamic.title("{}_返回:{}".format(user_or_policy_data['title'], device["device"]))
        my_log.info("****{}****".format(user_or_policy_data['title']))
        driver = common_driver[0]
        wel = WelcomePage(driver)
        sleep(1)
        wel.show_privacy_user_agreement_or_policy(user_or_policy_data['click'])
        with allure.step("step：断言隐私保护政策是否存在？"):
            assert wel.is_privacy_protection_exsist()
    #
    # @pytest.mark.smoke
    # # @pytest.mark.usefixtures("common_driver")  # 在运行的时候，会去运行start_function_App函数
    # @allure.story("引导页_同意_点击")
    # @allure.description("引导页_同意_点击")  # 用例的描述
    # @allure.severity(allure.severity_level.BLOCKER)
    # def test_welcome_2_click_privacy_agree_btn(self, common_driver, device):
    #     allure.dynamic.title("引导页_同意_点击:{}".format(device["device"]))
    #     my_log.info("****引导页_同意_点击****")
    #     driver = common_driver[0]
    #     wel = WelcomePage(driver)
    #     sleep(1)
    #     wel.click_privacy_agree_btn()
    #     wel.click_privacy_agree_btn()
    #     with allure.step("step：断言马上开始按钮是否存在？"):
    #         assert wel.is_began_btn_exsist()
    #
    # @pytest.mark.smoke
    # # @pytest.mark.usefixtures("common_driver")  # 在运行的时候，会去运行start_function_App函数
    # @allure.story("引导页_应用是如何工作的_点击")
    # @allure.description("引导页_应用是如何工作的_点击")  # 用例的描述
    # @allure.severity(allure.severity_level.BLOCKER)
    # def test_welcome_3_show_app_work(self, common_driver, device):
    #     allure.dynamic.title("引导页_应用是如何工作的_点击:{}".format(device["device"]))
    #     my_log.info("****引导页_应用是如何工作的_点击****")
    #     driver = common_driver[0]
    #     wel = WelcomePage(driver)
    #     sleep(1)
    #     with allure.step("step：断言返回按钮是否存在？"):
    #         assert wel.show_App_work()
    #
    # @pytest.mark.smoke
    # # @pytest.mark.usefixtures("common_driver")  # 在运行的时候，会去运行start_function_App函数
    # @allure.story("引导页_应用是如何工作的_点击_返回_点击")
    # @allure.description("引导页_应用是如何工作的_点击_返回_点击")  # 用例的描述
    # @allure.severity(allure.severity_level.BLOCKER)
    # def test_welcome_4_show_app_work_back(self, common_driver, device):
    #     allure.dynamic.title("引导页_应用是如何工作的_点击_返回_点击：{}".format(device["device"]))
    #     my_log.info("****引导页_应用是如何工作的_点击_返回_点击****")
    #     driver = common_driver[0]
    #     wel = WelcomePage(driver)
    #     sleep(1)
    #     # wel.click_privacy_agree_btn()
    #     wel.show_App_work()
    #     with allure.step("step：断言马上开始按钮是否存在？"):
    #         assert wel.is_began_btn_exsist()
    #
    # @pytest.mark.demo2
    # # @pytest.mark.usefixtures("common_driver")  # 在运行的时候，会去运行start_function_App函数
    # @allure.story("引导页_同意_点击_马上开始_点击")
    # @allure.description("引导页_同意_点击_马上开始_点击")  # 用例的描述
    # @allure.severity(allure.severity_level.BLOCKER)
    # def test_welcome_5_click_began_btn(self, common_driver, device):
    #     allure.dynamic.title("引导页_同意_点击_马上开始_点击：{}".format(device["device"]))
    #     my_log.info("****引导页_同意_点击_马上开始_点击****")
    #     driver = common_driver[0]
    #     wel = WelcomePage(driver)
    #     index = IndexPage(driver)
    #     sleep(1)
    #     # wel.click_privacy_agree_btn()
    #     wel.click_began_btn()
    #     with allure.step("step：断言首页搜索是否存在？"):
    #         assert index.is_index_page_exsist()
