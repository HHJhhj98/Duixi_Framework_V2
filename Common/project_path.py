# -*- coding：utf-8 -*-
# @Time ：2022/2/22 23:08
# @Authon :hhj
# @Annotation:
# @File : project_path.py

import os
from datetime import datetime

'''专门来读取路径的值'''
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# os.mkdir(project_path + '\\Outputs\\{}'.format(now))
# test_now_result_path = os.path.join(project_path, 'Outputs', now)

# test_result_list = ['Outputs', 'Logs', 'ScreenShots']
# for i in test_result_list:
#     os.mkdir(test_now_result_path+'\\{}'.format(i))

# 配置文件存放路径
# conf_path = os.path.join(project_path, 'common', 'conf', 'case.config')

# 测试用例文件存放路径
test_case_path = os.path.join(project_path, 'TestCases')

# 测试报告存放路径
# test_report_path = os.path.join(test_now_result_path, 'Reports')

# 日志存放路径
test_log_path = os.path.join(project_path, 'Outputs', 'Logs', 'FrameworkLogs', now + '_log.txt')

# Appium日志存放路径
appium_log_path = os.path.join(project_path, 'Outputs', 'Logs', 'AppiumLogs')

# 截图存放路径
sceen_shots_path = os.path.join(project_path, 'Outputs', 'ScreenShots')

# yaml文件路径
yaml_path = os.path.join(project_path, 'Common', 'desired_caps.yaml')

# 多机yaml文件路径
yamls_path = os.path.join(project_path, 'Desired_Caps', 'desired_caps.yaml')

# app路径
app_path = os.path.join(project_path, 'app')

# print(project_path)
# print(test_path)
# print(conf_path)
# print(test_log_path, sceen_shots_path)
