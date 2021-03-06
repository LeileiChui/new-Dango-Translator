# -*- coding: utf-8 -*-
# @Time : 2020/5/19 3:34
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : gloVarMan.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import src.utils.utils as utils
from src.utils.logger import logger
from PyQt5.QtGui import QFont

config_path = 'config/config.json'


class GloVarMan:
    """
    全局变量管理器
    """

    def __init__(self):
        self.logger = logger
        self.config = self.read_config()
        self.screen_scale_rate = utils.get_screen_rate()
        self.logger.info("读取配置文件")
        self.mainUI_font = QFont('华康方圆体W7')
        self.mainUI_font.setPointSize(15)
        self.setUI_font = QFont('华康方圆体W7')
        self.setUI_font.setPointSize(12)

    @staticmethod
    def read_config():
        """
        读取配置文件
        :return: dict
        """
        return utils.read_config(utils.resource_path(config_path))

    def save_config(self):
        """
        保存配置文件
        :return: None
        """
        utils.save_config(utils.resource_path(config_path), self.config)
        self.logger.info("保存配置文件")


glm = GloVarMan()
