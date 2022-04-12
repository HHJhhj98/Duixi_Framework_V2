# -*- coding：utf-8 -*-
# @Time ：2022/2/26 17:47
# @Authon :hhj
# @Annotation:
# @File : base_page.py
from datetime import datetime

import allure

from Common.my_log import MyLog
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from Common.project_path import *

my_logger = MyLog()


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_Visible(self, locator, times=10, poll_frequency=0.5, doc=''):
        """
        :param locator: (元素定位方式,元素定位表达式)
        :param times: 元素等待时间
        :param poll_frequency: 元素等待循环周期
        :param doc: 模块名_页面名称_操作名称（截图名称）
        :return: None
        """
        my_logger.info("{0}等待元素{1}可见".format(doc, locator))
        try:
            # 开始等待时间
            start = datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            end = datetime.now()
            my_logger.info('{0}元素等待结束，等待时长为：{1}毫秒'.format(locator, end - start))
        except:
            my_logger.exception('{0}等待元素{1}可见失败！！！'.format(doc, locator))
            # 截图
            self.save_screenshot(doc)
            self.save_allure_screen(doc)
            raise

    # 等待元素存在
    def wait_ele_Presence(self, locator, times=10, poll_frequency=0.5, doc=''):
        """
        :param locator: (元素定位方式,元素定位表达式)
        :param times: 元素等待时间
        :param poll_frequency: 元素等待循环周期
        :param doc: 模块名_页面名称_操作名称（截图名称）
        :return: None
        """
        my_logger.info("{0}_等待元素{1}存在".format(doc, locator))
        try:
            # 开始等待时间
            start = datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.presence_of_element_located(locator))
            # 结束等待时间
            end = datetime.now()
            my_logger.info('等待结束，等待时长为：{0}毫秒'.format(end - start))
        except:
            my_logger.exception('{0}_等待元素{1}存在失败！！！'.format(doc, locator))
            # 截图
            self.save_screenshot(doc)
            self.save_allure_screen(doc)
            raise

    # 判断元素存在
    def is_element_exsist(self, locator, times=10, poll_frequency=0.5, doc=''):
        """
        :param locator: (元素定位方式,元素定位表达式)
        :param times: 元素等待时间
        :param poll_frequency: 元素等待循环周期
        :param doc: 模块名_页面名称_操作名称（截图名称）
        :return: None
        """
        try:
            # 开始等待时间
            start = datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.presence_of_element_located(locator))
            # 结束等待时间
            end = datetime.now()
            my_logger.info("{0}_等待元素{1}存在".format(doc, locator))
            my_logger.info('等待结束，等待时长为：{0}毫秒'.format(end - start))
            return True
        except:
            my_logger.exception('{0}_等待元素{1}不存在！！！'.format(doc, locator))
            # 截图
            # self.save_screenshot(doc)
            # self.save_allure_screen(doc)
            return False

    # 查找元素
    def get_element(self, locator, doc=''):
        """
        :param locator: (元素定位方式,元素定位表达式)
        :param doc: 模块名_页面名称_操作名称（截图名称）
        :return: Webelement(元素对象)
        """
        my_logger.info('{0}查找元素：{1}'.format(doc, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            my_logger.exception('{0}查找元素{1}存在失败！！！'.format(doc, locator))
            # 截图
            self.save_screenshot(doc)
            self.save_allure_screen(doc)
            raise

    # 查找多个元素
    def get_elements(self, locator, doc=''):
        """
        :param locator: (元素定位方式,元素定位表达式)
        :param doc: 模块名_页面名称_操作名称（截图名称）
        :return: Webelements(元素对象)
        """
        my_logger.info('{0}查找多个元素：{1}'.format(doc, locator))
        try:
            return self.driver.find_elements(*locator)
        except:
            my_logger.exception('{0}查找多个元素{1}存在失败！！！'.format(doc, locator))
            # 截图
            self.save_screenshot(doc)
            self.save_allure_screen(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc='', index=None):
        """
        :param locator: (元素定位方式,元素定位表达式)
        :param doc: 模块名_页面名称_操作名称（截图名称）
        :param index: 默认为None，只能查找出一个元素，如果指定值，为多个元素的下标
        :return: None
        """
        # 找元素
        if index != None:
            ele = self.get_elements(locator, doc)[index]
        else:
            ele = self.get_element(locator, doc)
        # 元素操作
        try:
            my_logger.info('{0}_点击元素：{1}'.format(doc, locator))
            ele.click()
        except:
            my_logger.info('{0}_点击{1}元素出错！！！'.format(doc, locator))
            # 截图
            self.save_screenshot(doc)
            self.save_allure_screen(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc='', index=None):
        """
        :param locator: (元素定位方式,元素定位表达式)
        :param text: 输入文本
        :param doc: 模块名_页面名称_操作名称（截图名称）
        :param index: 默认为None，只能查找出一个元素，如果指定值，为多个元素的下标
        :return: None
        """
        # 找元素
        if index != None:
            ele = self.get_elements(locator, doc)[index]
        else:
            ele = self.get_element(locator, doc)
        # 元素操作
        try:
            my_logger.info('在{0}_{1}元素中输入文本：{2}'.format(doc, locator, text))
            ele.send_keys(text)
        except:
            my_logger.info('在{0}_{1}元素中输入文本：{2}时出错！！！'.format(doc, locator, text))
            # 截图
            self.save_screenshot(doc)
            self.save_allure_screen(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc='', index=None):
        """
        :param locator: (元素定位方式,元素定位表达式)
        :param doc: 模块名_页面名称_操作名称（截图名称）
        :param index: 默认为None，只能查找出一个元素，如果指定值，为多个元素的下标
        :return: 元素文本内容
        """
        # 找元素
        if index != None:
            ele = self.get_elements(locator, doc)[index]
        else:
            ele = self.get_element(locator, doc)
        # 元素操作
        try:
            my_logger.info('在{0}中获取{1}元素的文本'.format(doc, locator))
            return ele.text
        except:
            my_logger.info('在{0}中获取{1}元素的文本时出错！！！'.format(doc, locator))
            # 截图
            self.save_screenshot(doc)
            self.save_allure_screen(doc)
            raise

    # 获取元素的属性
    def get_ele_attribute(self, locator, attr, doc='', index=None):
        """
        :param locator: (元素定位方式,元素定位表达式)
        :param attr: 属性名
        :param doc: 模块名_页面名称_操作名称（截图名称）
        :param index: 默认为None，只能查找出一个元素，如果指定值，为多个元素的下标
        :return: 元素属性值
        """
        # 找元素
        if index != None:
            ele = self.get_elements(locator, doc)[index]
        else:
            ele = self.get_element(locator, doc)
        # 元素操作
        try:
            my_logger.info('在{0}中获取{1}元素_{2}的属性值'.format(doc, locator, attr))
            return ele.get_attribute(name=attr)
        except:
            my_logger.info('在{0}中获取{1}元素_{2}的属性值时出错！！！'.format(doc, locator, attr))
            # 截图
            self.save_screenshot(doc)
            self.save_allure_screen(doc)
            raise

    # 判断按钮的点击状态
    def ele_is_enabled(self, locator, doc='', index=None):
        """
        :param locator: (元素定位方式,元素定位表达式)
        :param doc: 模块名_页面名称_操作名称（截图名称）
        :param index: 默认为None，只能查找出一个元素，如果指定值，为多个元素的下标
        :return: 可用为True
        """
        # 找元素
        if index != None:
            ele = self.get_elements(locator, doc)[index]
        else:
            ele = self.get_element(locator, doc)
        # 元素操作
        try:
            my_logger.info('在{0}中查看{1}元素的点击状态'.format(doc, locator))
            return ele.is_enabled()
        except:
            my_logger.info('在{0}中查看{1}元素的点击状态时出错！！！'.format(doc, locator))
            # 截图
            self.save_screenshot(doc)
            self.save_allure_screen(doc)
            raise

    # alert处理
    def alert_action(self, action='accept'):
        pass

    # iframe切换
    def switch_iframe(self, iframe_reference):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理
    # 窗口切换

    # 截图保存为allure附件
    def save_allure_screen(self, name):
        if name is not None:
            allure.attach(self.driver.get_screenshot_as_png(), name, allure.attachment_type.PNG)  # 保存截图为allure的附件
            my_logger.info('allure截取网页成功，文件路径为：{0}'.format(name))

    # 截图
    def save_screenshot(self, name):
        # 图片名称 ： 模块名_页面名称_操作名称_时间.png
        file_name = '{0}\{1}_{2}.png'.format(sceen_shots_path, name, datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
        self.driver.save_screenshot(file_name)
        my_logger.info('截取网页成功，文件路径为：{0}'.format(file_name))

    # 上下左右滑动
    def swipe_up(self, size):
        # 向上滑动
        self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.1)

    def swipe_down(self, size):
        # 向下滑动
        self.driver.swipe(size["width"] * 0.5, size["height"] * 0.2, size["width"] * 0.5, size["height"] * 0.9)

    def swipe_left(self, size):
        # 从左往右
        self.driver.swipe(size["width"] * 0.1, size["height"] * 0.5, size["width"] * 0.9, size["height"] * 0.5, 200)

    def swipe_right(self, size):
        # 从右往左
        self.driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5, 200)

    # 获取整个屏幕大小
    def get_window_size(self):
        return self.driver.get_window_size()

    # toast获取
    def get_toast_msg(self, str):
        # 1、xpath表达式  文本匹配
        loc = (MobileBy.XPATH, '//*[contains(@text,"{}")]'.format(str))
        try:
            WebDriverWait(self.driver, 20, 0.02).until(
                EC.presence_of_element_located(loc))  # 不能使用visibility_of_element_located，toast不支持
            return self.driver.find_element(*loc).text
        except:
            my_logger.exception("没有找到匹配的toast")
            raise

    # H5切换
