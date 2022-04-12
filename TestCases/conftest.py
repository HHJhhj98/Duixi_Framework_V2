# # -*- coding：utf-8 -*-
# # @Time ：2022/4/3 21:50
# # @Authon :hhj
# # @Annotation:
# # @File : conftest.py
# import pytest
# import yaml
# import random
#
# from Common.base_page import BasePage
# from Common.my_log import MyLog
# from Common.system_properties import SystemProperties
# from PageLocators.WelcomePageLocators.welcomepage_locators import WelcomePageLocator as loc
# from Common.project_path import *
# from appium import webdriver
#
# from PageObjects.WelcomePage.welcome_page import WelcomePage
# from Common.base_driver import BaseDriver
# from Common.app_info import get_android_launcher_activity
#
#
# # @pytest.fixture
# # def startApp():
# #     # 准备服务器参数，与appium server进行连接
# #     # 1、要不要判断欢迎界面是否存在?
# #     # 2、要不要判断当前用户是否已登录？
# #     pass
#
#
# # def baseDriver(automationName=None, noReset=None):
# #     '''
# #     :param automationName:
# #     :param noReset:
# #     :return:
# #     '''
# #     fs = open(yaml_path)
# #     caps = yaml.load(fs)
# #     if automationName is not None:
# #         caps['automationName'] = automationName
# #     if noReset == False:
# #         caps['noReset'] = False
# #
# #     driver = webdriver.Remote('http://127.0.0.1:4724/wd/hub', caps)
# #     return driver
#
# # def do_welcome(driver):
# #     # 处理欢迎页面
# #     # 如果没有找到首页的元素/不包含MainActivity，那么就在欢迎界面
# #     doc = '欢迎页面_引导页'
# #     curAct = driver.current_activity
# #     if curAct.find("Mainactivity")==-1:
# #         # 滑动欢迎页面至首页
# #         if BasePage(driver).is_element_exsist(locator=loc.privacy_text,doc=doc)==True:
# #             BasePage(driver).wait_ele_Presence(locator=loc.privacy_agree_btn,doc=doc)
# #
# #         else:
# my_log = MyLog()
# driver = None
#
#
import pytest


def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="device_info", help=None)


@pytest.fixture(scope='session')
def cmdopt(pytestconfig):
    # 两种写法
    return pytestconfig.getoption("--cmdopt")
    # return pytestconfig.option.cmdopt

@pytest.fixture
def device(cmdopt):
    # cmdopt = {'platform_version': '7.1.2', 'server_port': 4724, 'system_port': 8200, 'device': '127.0.0.1:62025'}
    yield eval(cmdopt)
#
#
# def pytest_itemcollected(item):
#     item._nodeid = str(random.randint(1, 1000)) + '_' + item . _nodeid
#
# @pytest.fixture(scope='function')
# def start_function_App_and_launcher_name():
#     # 准备服务器参数，与appium server进行连接。noReset=False
#     # 1、要不要判断欢迎界面是否存在?
#     # 2、要不要判断当前用户是否已登录？
#     # pass
#     # 前置操作
#     my_log.info("****开始获取系统Launcher名称****")
#     cmdopt = {'platform_version': '7.1.2', 'server_port': 4724, 'system_port': 8200, 'device': '127.0.0.1:62025'}
#     my_log.info(cmdopt)
#     cmd = cmdopt
#     device_id = cmd['device']
#     android_version = cmd['platform_version']
#     launcher_name = get_android_launcher_activity(device_id, android_version)
#     my_log.info("****系统Launcher名称为{}****".format(launcher_name))
#     my_log.info("====每条用例的前置操作：启动对戏APP(setUpClass)====")
#     global driver
#     base_driver = BaseDriver(cmdopt)
#     driver = base_driver.base_driver()
#     wel = WelcomePage(driver)
#     yield (driver, launcher_name, wel)  # 分割线，返回值
#     # 后置操作
#     my_log.info("====每条用例的后置操作：关闭对戏APP，清理环境(teardownClass)====")
#     driver.quit()