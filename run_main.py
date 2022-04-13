# -*- coding：utf-8 -*-
# @Time ：2022/4/5 21:01
# @Authon :hhj
# @Annotation:
# @File : run_main.py
from time import sleep

import pytest

from multiprocessing import Pool
from Common.get_data import GetData
import os
import pytest
from Common.app_info import get_device_infos, uninstall_app
from Common.appium_auto_server import close_appium


def run_parallel(device_info):
    # print(device_info)
    # setattr(GetData, 'device_dict', device_info)
    pytest.main([f"--cmdopt={device_info}", "--alluredir", "Outputs/Reports/my_allure_re"])
    os.system("allure generate Outputs/Reports/my_allure_re -o Outputs/Reports/html --clean")
#hhj
#jjll
if __name__ == "__main__":
    device_lists = get_device_infos()
    uninstall_app(device_lists)
    with Pool(len(device_lists)) as pool:
        pool.map(run_parallel, device_lists)
        sleep(0.5)
        pool.close()
        pool.join()
    close_appium()
