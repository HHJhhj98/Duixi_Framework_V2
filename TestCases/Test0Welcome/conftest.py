# -*- coding：utf-8 -*-
# @Time ：2022/4/3 21:50
# @Authon :hhj
# @Annotation:
# @File : conftest.py
import os
import re
from time import sleep

import allure
import pytest
import yaml
import random
from Common.base_page import BasePage
from Common.my_log import MyLog
from Common.system_properties import SystemProperties
from PageLocators.WelcomePageLocators.welcomepage_locators import WelcomePageLocator as loc
from Common.project_path import *
from appium import webdriver

from PageObjects.WelcomePage.welcome_page import WelcomePage
from Common.base_driver import BaseDriver
from Common.app_info import get_android_launcher_activity
from Common.get_data import GetData

my_log = MyLog()
driver = None



@pytest.fixture(scope='function')
def start_function_App(cmdopt):
    # 准备服务器参数，与appium server进行连接。noReset=False
    # 1、要不要判断欢迎界面是否存在?
    # 2、要不要判断当前用户是否已登录？
    # pass
    # 前置操作
    my_log.info("====每条用例的前置操作：启动对戏APP(setUpClass)====")
    # cmdopt = device_dict
    # cmdopt = getattr(GetData, 'device_dict')
    my_log.info(eval(cmdopt))
    global driver
    driver = base_driver = BaseDriver(eval(cmdopt))
    driver = base_driver.base_driver()
    wel = WelcomePage(driver)
    yield (driver, wel)  # 分割线，返回值
    # 后置操作
    my_log.info("====每条用例的后置操作：关闭对戏APP，清理环境(teardownClass)====")
    driver.close_app()
    driver.quit()


@pytest.fixture(scope='function')
def start_function_App_and_launcher_name(cmdopt):
    # 准备服务器参数，与appium server进行连接。noReset=False
    # 1、要不要判断欢迎界面是否存在?
    # 2、要不要判断当前用户是否已登录？
    # pass
    # 前置操作
    my_log.info("****开始获取系统Launcher名称****")
    # cmdopt = {'platform_version': '7.1.2', 'server_port': 4724, 'system_port': 8200, 'device': '127.0.0.1:62025'}
    # cmdopt = getattr(GetData, 'device_dict')
    my_log.info(eval(cmdopt))
    cmd = eval(cmdopt)
    device_id = cmd['device']
    android_version = cmd['platform_version']
    launcher_name = get_android_launcher_activity(device_id, android_version)
    my_log.info("****系统Launcher名称为{}****".format(launcher_name))
    my_log.info("====每条用例的前置操作：启动对戏APP(setUpClass)====")
    global driver
    base_driver = BaseDriver(cmdopt)
    driver = base_driver.base_driver()
    wel = WelcomePage(driver)
    yield (driver, launcher_name, wel)  # 分割线，返回值
    # 后置操作
    my_log.info("====每条用例的后置操作：关闭对戏APP，清理环境(teardownClass)====")
    driver.close_app()
    driver.quit()


# 定义公共的fixture
@pytest.fixture(scope='session')
def common_driver(cmdopt):
    # 准备服务器参数，与appium server进行连接。noReset=False
    # 1、要不要判断欢迎界面是否存在?
    # 2、要不要判断当前用户是否已登录？
    # pass
    # 前置操作
    my_log.info("====所有用例的前置操作：启动对戏APP(setUp)====")
    # cmdopt = {'platform_version': '7.1.2', 'server_port': 4724, 'system_port': 8200, 'device': '127.0.0.1:62025'}
    # cmdopt = getattr(GetData, 'device_dict')
    global driver
    base_driver = BaseDriver(eval(cmdopt))
    sleep(1)
    my_log.info(eval(cmdopt))
    driver = base_driver.base_driver()
    sleep(5)
    wel = WelcomePage(driver)
    yield (driver, wel)  # 分割线，返回值
    # 后置操作
    my_log.info("====所有用例的后置操作：关闭对戏APP，清理环境(teardown)====")
    driver.close_app()
    driver.quit()


# def do_welcome(driver):
#     # 处理欢迎页面
#     # 如果没有找到首页的元素/不包含MainActivity，那么就在欢迎界面
#     doc = '欢迎页面_引导页'
#     curAct = driver.current_activity
#     if curAct.find("Mainactivity")==-1:
#         # 滑动欢迎页面至首页
#         if BasePage(driver).is_element_exsist(locator=loc.privacy_text,doc=doc)==True:
#             BasePage(driver).wait_ele_Presence(locator=loc.privacy_agree_btn,doc=doc)
#
#         else:

# def get_loginStatus():
#     '''
#     获取登录状态
#     :return: 已登录 True 未登录False
#     '''
#     try:
#         # 等待5秒
#         pass
#     except:
#         pass

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


# if __name__ == '__main__':
#     # fs = open(yaml_path)
#     # caps = yaml.load(fs, Loader=yaml.FullLoader)
#     # my_log.info(caps)

@pytest.fixture
def device(cmdopt):
    yield eval(cmdopt)

def pytest_itemcollected(item):
    item._nodeid = str(random.randint(1, 1000)) + '_' + item._nodeid
