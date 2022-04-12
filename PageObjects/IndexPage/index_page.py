# -*- coding：utf-8 -*-
# @Time ：2022/4/5 17:34
# @Authon :hhj
# @Annotation:
# @File : index_page.py

import allure

from Common.base_page import BasePage
from PageLocators.IndexPageLocators.indexpage_locators import IndexPageLocator as index_loc


class IndexPage(BasePage):

    # 判断是否在首页
    def is_index_page_exsist(self):
        doc = '首页_判断是否在首页'
        return self.is_element_exsist(locator=index_loc.top_search_input, doc=doc)
