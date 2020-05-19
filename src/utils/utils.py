# -*- coding: utf-8 -*-
# @Time : 2020/5/19 12:38
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : utils.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import sys
import os
import json
from win32 import win32gui, win32print
from win32.lib import win32con
from win32.win32api import GetSystemMetrics


def resource_path(relative_path):
    """
    获取资源文件路径，确保打包后仍能读取到资源文件
    :param relative_path: 资源文件的相对路径
    :return: str 资源的绝对路径
    """
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath("D:\\new-Dango-Translator")
    return os.path.join(base_path, relative_path)


def read_config(config_path: str):
    """
    读取配置文件
    :param config_path: str
    :return: dict
    """
    with open(resource_path(config_path), 'r+', encoding='utf8')as config_file:
        return json.load(config_file)


def save_config(config_path: str, config_data: dict):
    """
    保存配置
    :param config_path: str 配置文件路径
    :param config_data: dict 配置数据
    :return: None
    """
    with open(resource_path(config_path), 'w', encoding='utf8') as config_file:
        config_file.write(json.dumps(config_data, indent=4, ensure_ascii=False))


def get_real_resolution():
    """
    获取屏幕真实分辨率
    :return: 横向 纵向真实分辨率
    """
    hDC = win32gui.GetDC(0)
    # 横向分辨率
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    # 纵向分辨率
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h


def get_screen_size():
    """
    获取缩放后的分辨率
    :return: 横向 纵向缩放后的分辨率
    """
    w = GetSystemMetrics(0)
    h = GetSystemMetrics(1)
    return w, h


def get_screen_rate():
    """
    计算屏幕缩放比
    :return: 屏幕缩放比，两位小数
    """
    real_resolution = get_real_resolution()
    screen_size = get_screen_size()
    screen_scale_rate = round(real_resolution[0] / screen_size[0], 2)

    return screen_scale_rate


# test
if __name__ == '__main__':
    print(get_screen_rate())
