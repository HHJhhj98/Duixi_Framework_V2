# -*- coding：utf-8 -*-
# @Time ：2022/4/6 21:50
# @Authon :hhj
# @Annotation:
# @File : system_properties.py
import os
import re


class SystemProperties:

    def group_call(self):
        # 读取设备id 不支持模拟器
        readDeviceId = list(os.popen('adb devices').readlines())
        deviceIdList = []
        for i in range(1, len(readDeviceId) - 1):
            # 正则表达式匹配出 id 信息
            deviceId = re.findall(r'^\w*\b', readDeviceId[i])[0]
            deviceIdList.append(deviceId)
        return deviceIdList

    def get_android_system_properties(self, devices, propertie):
        # 读取设备系统属性
        '''
        :param devices: 设备ID或127.0.0.1:端口号
        :param propertie: 系统属性名 如：ro.product.model
        :return:系统属性值 如:MI MAX 2
        '''
        if devices == '127':
            devices = '127.0.0.1:62025'
        deviceAndroidVersion = list(
            os.popen('adb -s {} shell getprop {}'.format(devices, propertie)).readlines())
        deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
        return deviceAndroidVersion[0].strip('\n')

    def get_android_launcher_activity(self, devices, android_version):
        # 读取设备系统Launcher的activity
        '''
        :param devices: 设备ID或127.0.0.1:端口号
        :param android_version: android版本
        :return: 系统Launcher的activity
        '''
        # if devices == '127':
        #     devices = '127.0.0.1:62025'
        android_version = float(android_version[0:3])
        if android_version <= 8.0:
            activity = 'mFocusedActivity'
        else:
            activity = 'mResumedActivity'
        deviceAndroidVersion = list(
            os.popen(r'adb -s {} shell dumpsys activity | findstr "{}"'.format(devices, activity)).readlines())
        print(deviceAndroidVersion)
        deviceVersion = re.findall(r'/.*\s', deviceAndroidVersion[0])[0]
        deviceVersion = deviceVersion.split(" ")[0]
        deviceVersion = deviceVersion.split("/")[1]
        print(deviceVersion)
        return deviceVersion


# if __name__ == '__main__':
#     d = SystemProperties().group_call()[0]
#     n = SystemProperties().get_android_system_properties(d, 'ro.build.version.release')
#     print(d)
#     SystemProperties().get_android_launcher_activity(d, n)
