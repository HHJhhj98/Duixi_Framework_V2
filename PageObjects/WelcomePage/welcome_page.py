# -*- coding：utf-8 -*-
# @Time ：2022/4/5 12:57
# @Authon :hhj
# @Annotation:
# @File : welcome_page.py
from time import sleep

import allure

from Common.base_page import BasePage
from PageLocators.WelcomePageLocators.welcomepage_locators import WelcomePageLocator as loc
from PageObjects.IndexPage.index_page import IndexPage


class WelcomePage(BasePage):

    # 判断隐保护政策是否存在
    def is_privacy_protection_exsist(self):
        doc = '引导页_判断隐私保护政策是否存在'
        with allure.step("step：返回隐私保护政策是否存在"):
            return self.is_element_exsist(locator=loc.privacy_text, doc=doc)

    # 点击同意按钮
    def click_privacy_agree_btn(self):
        doc = '引导页_点击同意按钮'
        with allure.step("step：等待同意按钮可见"):
            self.wait_ele_Visible(locator=loc.privacy_agree_btn, doc=doc)
        with allure.step("step：点击同意按钮"):
            self.click_element(locator=loc.privacy_agree_btn, doc=doc)

    # 点击不同意按钮
    def click_privacy_disagree_btn(self):
        doc = '引导页_点击不同意按钮'
        with allure.step("step：等待不同意按钮可见"):
            self.wait_ele_Visible(locator=loc.privacy_disagree_btn, doc=doc)
        with allure.step("step：点击不同意按钮"):
            self.click_element(locator=loc.privacy_disagree_btn, doc=doc)

    # 查看用户协议/隐私政策
    def show_privacy_user_agreement_or_policy(self, attr=''):
        '''
        :param attr: 用户协议or隐私政策
        :return: content_des文本
        '''
        doc = ''
        if attr == '用户协议':
            doc = '引导页_查看用户协议'
            with allure.step("step：等待《用户协议》按钮可见"):
                self.wait_ele_Visible(locator=loc.privacy_user_agreement_btn, doc=doc)
            with allure.step("step：点击《用户协议》按钮"):
                self.click_element(locator=loc.privacy_user_agreement_btn, doc=doc)
            ele_loc = loc.terms_of_service_text
        elif attr == '隐私政策':
            doc = '引导页_查看隐私政策'
            with allure.step("step：等待《隐私政策》按钮可见"):
                self.wait_ele_Visible(locator=loc.privacy_policy_btn, doc=doc)
            with allure.step("step：点击《隐私政策》按钮"):
                self.click_element(locator=loc.privacy_policy_btn, doc=doc)
            ele_loc = loc.privacy_policy_text
        with allure.step("step：等待《" + attr + "》元素可见"):
            self.wait_ele_Visible(locator=ele_loc, doc=doc)
        with allure.step("step：获取《" + attr + "》content-desc文本"):
            sleep(3)
            content_desc = self.get_ele_attribute(locator=ele_loc, attr='content-desc', doc=doc)
            # self.click_element(locator=loc.terms_of_service_text, doc=doc)
        with allure.step("step：等待返回按钮可见"):
            self.wait_ele_Visible(locator=loc.terms_of_service_btn, doc=doc)
        with allure.step("step：点击返回按钮"):
            self.click_element(locator=loc.terms_of_service_btn, doc=doc)
        return content_desc

    # # 查看隐私政策
    # def show_privacy_policy(self):
    #     doc = '引导页_查看隐私政策'
    #     with allure.step("step：等待《隐私政策》按钮可见"):
    #         self.wait_ele_Visible(locator=loc.privacy_policy_btn, doc=doc)
    #     with allure.step("step：点击《隐私政策》按钮"):
    #         self.click_element(locator=loc.privacy_policy_btn, doc=doc)
    #     with allure.step("step：等待《隐私政策》元素可见"):
    #         self.wait_ele_Visible(locator=loc.terms_of_service_text, doc=doc)
    #     with allure.step("step：获取《隐私政策》content-desc文本"):
    #         content_desc = self.get_ele_attribute(locator=loc.terms_of_service_text, attr='content-desc', doc=doc)
    #         # self.click_element(locator=loc.terms_of_service_text, doc=doc)
    #     with allure.step("step：点击返回按钮"):
    #         self.click_element(locator=loc.terms_of_service_btn, doc=doc)
    #     return content_desc

    # 隐私政策内容上滑
    def slide_up_text(self):
        doc = '引导页_隐私政策内容上滑'
        pass

    # 隐私政策内容上滑
    def slide_down_text(self):
        doc = '引导页_隐私政策内容下滑'
        pass

    def do_welcome(self):
        # 处理欢迎页面
        # 如果没有找到首页的元素/不包含MainActivity，那么就在欢迎界面
        doc = '欢迎页面_引导页'
        flag = IndexPage(self.driver).is_index_page_exsist()
        if flag == False:
            # 滑动欢迎页面至首页
            if self.is_element_exsist(locator=loc.privacy_text, doc=doc) == True:
                self.wait_ele_Presence(locator=loc.privacy_agree_btn, doc=doc)
                self.click_element(locator=loc.privacy_agree_btn, doc=doc)
            self.wait_ele_Visible(locator=loc.began_btn, doc=doc)

    def get_warm_tips_text(self):
        doc = '引导页_温馨提示文案'
        with allure.step("step：等待'温馨提示'文案元素可见"):
            self.wait_ele_Visible(locator=loc.warm_tips_text, doc=doc)
        with allure.step("step：获取'温馨提示'文案"):
            warm_tips_text = self.get_ele_attribute(locator=loc.warm_tips_text, doc=doc)
        return warm_tips_text

    def click_warm_tips_quit_btn(self):
        doc = '引导页_温馨提示_退出应用_点击'
        with allure.step("step：等待'温馨提示_退出应用'元素可见"):
            self.wait_ele_Visible(locator=loc.warm_tips_quit_btn, doc=doc)
        with allure.step("step：点击'温馨提示_退出应用'"):
            self.click_element(locator=loc.warm_tips_quit_btn, doc=doc)
        with allure.step("step：获取当前Activity"):
            act = self.driver.current_activity
        return act

    def click_warm_tips_agree_btn(self):
        doc = '引导页_温馨提示_同意并继续_点击'
        with allure.step("step：等待'温馨提示_同意并继续'元素可见"):
            self.wait_ele_Visible(locator=loc.warm_tips_agree_btn, doc=doc)
        with allure.step("step：点击'温馨提示_同意并继续'"):
            self.click_element(locator=loc.warm_tips_agree_btn, doc=doc)
        with allure.step("step：获取马上开始按钮是否存在"):
            flag = self.is_began_btn_exsist()
        return flag

    def is_began_btn_exsist(self):
        doc = '引导页_马上开始按钮'
        with allure.step("step：等待马上开始按钮可见"):
            self.wait_ele_Visible(locator=loc.began_btn, doc=doc)
        with allure.step("step：返回马上开始是否可见"):
            return self.is_element_exsist(locator=loc.began_btn, doc=doc)

    def click_began_btn(self):
        doc = '引导页_马上开始按钮_点击'
        with allure.step("step：等待马上开始按钮可见"):
            self.wait_ele_Visible(locator=loc.began_btn, doc=doc)
        with allure.step("step：点击马上开始按钮"):
            self.click_element(locator=loc.began_btn, doc=doc)

    # 查看用户协议/隐私政策
    def show_App_work(self):
        doc = '引导页_查看用户协议'
        with allure.step("step：等待应用是如何工作的按钮可见"):
            self.wait_ele_Visible(locator=loc.app_work_btn, doc=doc)
        with allure.step("step：点击应用是如何工作的按钮"):
            sleep(2)
            self.click_element(locator=loc.app_work_btn, doc=doc)
        # ele_loc = loc.terms_of_service_text
        # with allure.step("step：等待应用是如何工作的元素可见"):
        #     self.wait_ele_Visible(locator=ele_loc, doc=doc)
        # with allure.step("step：获取《"+attr+"》content-desc文本"):
        #     sleep(3)
        #     content_desc = self.get_ele_attribute(locator=ele_loc, attr='content-desc', doc=doc)
        # self.click_element(locator=loc.terms_of_service_text, doc=doc)
        with allure.step("step：等待返回按钮可见"):
            self.wait_ele_Visible(locator=loc.terms_of_service_btn, doc=doc)
            flag = self.is_element_exsist(locator=loc.terms_of_service_btn, doc=doc)
        with allure.step("step：点击返回按钮"):
            sleep(2)
            self.click_element(locator=loc.terms_of_service_btn, doc=doc)
        return flag
