# -*- coding：utf-8 -*-
# @Time ：2022/4/10 9:57
# @Authon :hhj
# @Annotation:
# @File : utils.py
from Common.my_log import MyLog
import re
my_log = MyLog()


def re_extract(data, rePath):
    try:
        return re.findall(rePath, data)
    except Exception as e:
        my_log.exception("提取执行失败！{}".format(e))
    return None