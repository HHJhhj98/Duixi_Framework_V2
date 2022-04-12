# -*- coding：utf-8 -*-
# @Time ：2022/4/6 22:02
# @Authon :hhj
# @Annotation:
# @File : base_driver.py
from appium import webdriver
import time
import yaml
import os

from Common.my_log import MyLog
from Common.project_path import *
from Common.appium_auto_server import *
from Common.app_info import *

my_log = MyLog()


class BaseDriver:

    def __init__(self, device_info):
        self.device_info = device_info
        cmd = "start /b appium -a 127.0.0.1 -p {0} -bp {1}".format(self.device_info["server_port"],
                                                                   self.device_info["server_port"] + 1)
        open_appium(cmd, self.device_info["server_port"])

    def base_driver(self, automationName="appium"):
        fp = open(yamls_path, encoding='utf-8')
        # 平台名称、包名、Activity名称、超时时间、是否重置、server_ip、
        desired_caps = yaml.load(fp, Loader=yaml.FullLoader)

        # 设备名称
        desired_caps["deviceName"] = self.device_info['device']

        # 版本信息
        desired_caps["platform_version"] = get_devices_version(desired_caps["deviceName"])

        app_Path = os.path.join(app_path, get_app_name(app_path))
        desired_caps['app'] = app_Path

        desired_caps['appPackage'] = get_app_package_name()

        desired_caps['appActivity'] = get_app_launchable_activity()

        # udid
        desired_caps["udid"] = self.device_info['device']
        # 系统端口号
        desired_caps["systemPort"] = self.device_info["system_port"]

        if automationName != "appium":
            desired_caps["automationName"] = 'uiautomator2'
        # desired_caps["automationName"] = 'uiautomator2'
        my_log.info(desired_caps)
        driver = webdriver.Remote(f"http://127.0.0.1:{self.device_info['server_port']}/wd/hub",
                                  desired_capabilities=desired_caps)
        return driver
