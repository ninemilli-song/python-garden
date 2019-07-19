#!python3

import time


def convert_timestamp(timestamp):
    """
    将时间戳转换为可读日期
    :return:
    """
    if timestamp is not None:
        # 将时间戳转换为时间元组
        tiemtuple = time.localtime(timestamp)
        # 将时间元组格式化为日期字符串
        time_str = time.strftime('%Y/%m/%d', tiemtuple)
        return time_str
    else:
        return ''
