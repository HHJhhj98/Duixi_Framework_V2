# -*- coding：utf-8 -*-
# @Time ：2022/3/31 21:39
# @Authon :hhj
# @Annotation:
# @File : login_page.py
import allure

from Common.base_page import BasePage
from PageLocators.LoginPageLocators.loginpage_locators import LoginPageLocator as loc

class LoginPage(BasePage):

    # 登录操作
    def login(self, phone, password, rember_user=True):
        doc = '登录页面_登录功能'
        with allure.step("step1：等待登录按钮可见"):
            self.wait_ele_Visible(loc.login_but, doc=doc)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.login_but))
        with allure.step("step2：在{0}中输入用户名：{1}".format(loc.phone_text, phone)):
            self.input_text(loc.phone_text, phone, doc)
        # self.driver.find_element(*loc.name_text).send_keys(phone)
        with allure.step("step3：在{0}中输入密码：{1}".format(loc.pwd_text, password)):
            self.input_text(loc.pwd_text, password, doc)
        # self.driver.find_element(*loc.pwd_text).send_keys(password)
        if rember_user != True:
            # 判断rember_user的值为False，取消勾选记住密码
            # 否则为默认勾选
            with allure.step("step4：不勾选同意《服务条款》《隐私政策》"):
                pass
            # self.driver.find_element(*loc.rember_text).click()
        else:
            with allure.step("step4：勾选同意《服务条款》《隐私政策》"):
                self.click_element(loc.agree_check, doc)
            with allure.step("step5：点击登录按钮"):
                self.click_element(loc.login_but, doc)
        # self.driver.find_element(*loc.login_but).click()