# -*- coding: utf-8 -*-
# @Time : 2020/5/19 3:34
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : gloVarMan.py
# @Software: PyCharm
# -*- coding: utf-8 -*-


class GloVarMan:
    """
    全局变量管理器
    """

    def __init__(self):
        self.config = {}

    def _read_config(self):
        """
        读取配置文件
        :return: dict: json
        """


glm = GloVarMan()
