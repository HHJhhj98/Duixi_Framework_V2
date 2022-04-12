# -*- coding：utf-8 -*-
# @Time ：2022/3/31 21:45
# @Authon :hhj
# @Annotation:
# @File : loginpage_locators.py

from appium.webdriver.common.mobileby import MobileBy


class LoginPageLocator:
    # 元素定位
    # 用户名输入框
    phone_text = (
    MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className(\"android.widget.EditText\").textContains(\"请输入手机号码\")')
    # 密码输入框
    pwd_text = (
    MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className(\"android.widget.EditText\").textContains(\"短信验证码\")')
    # 登录按钮
    login_but = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className(\"android.widget.Button\")')
    # 勾选同意《服务条款》《隐私政策》
    agree_check = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className(\"android.widget.ImageView\")')
