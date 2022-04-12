# -*- coding：utf-8 -*-
# @Time ：2022/4/5 17:36
# @Authon :hhj
# @Annotation:
# @File : indexpage_locators.py


from appium.webdriver.common.mobileby import MobileBy


class IndexPageLocator:
    # 首页元素定位
    top_search_input = (MobileBy.ACCESSIBILITY_ID, '热门搜索')
