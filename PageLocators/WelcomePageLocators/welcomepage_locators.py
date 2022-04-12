# -*- coding：utf-8 -*-
# @Time ：2022/4/3 23:36
# @Authon :hhj
# @Annotation:
# @File : welcomepage_locators.py

from appium.webdriver.common.mobileby import MobileBy


class WelcomePageLocator:
    # 元素定位
    # 隐私保护文本
    privacy_text = (MobileBy.ACCESSIBILITY_ID, '隐私保护政策')
    # 隐私保护_同意按钮
    privacy_agree_btn = (MobileBy.ACCESSIBILITY_ID, '同意')
    # 隐私保护_不同意按钮
    privacy_disagree_btn = (MobileBy.ACCESSIBILITY_ID, '不同意')
    # 隐私保护_《用户协议》按钮
    privacy_user_agreement_btn = (MobileBy.ACCESSIBILITY_ID, '《用户协议》')
    # 隐私保护_《隐私政策》按钮
    privacy_policy_btn = (MobileBy.ACCESSIBILITY_ID, '《隐私政策》')

    # 服务条款页面
    terms_of_service_text = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains(\"服务\")')

    # 隐私政策页面
    privacy_policy_text = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains(\"隐私\")')
    # 返回按钮
    terms_of_service_btn = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className(\"android.widget.ImageView\")')

    # 马上开始按钮
    began_btn = (MobileBy.ACCESSIBILITY_ID, '马上开始 ')

    # 温馨提示
    warm_tips = (MobileBy.ACCESSIBILITY_ID, '温馨提示')
    # 温馨提示文案
    warm_tips_text = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains(\"《对戏隐私保护政策》\")')
    # 温馨提示退出应用按钮
    warm_tips_quit_btn = (MobileBy.ACCESSIBILITY_ID, '退出应用')
    # 温馨提示同意并继续按钮
    warm_tips_agree_btn = (MobileBy.ACCESSIBILITY_ID, '同意并继续')

    # 应用是如何工作的
    app_work_btn = (MobileBy.ACCESSIBILITY_ID, '应用是如何工作的')
