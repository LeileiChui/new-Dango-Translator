# -*- coding: utf-8 -*-
# @Time : 2020/5/20 21:22
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : dangoTray.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QSystemTrayIcon
import src.utils.utils as utils


class MyTray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        # self.parent_window = window
        try:
            self.setIcon(QIcon(utils.resource_path('asserts/光标.png')))
            self.activated.connect(self.iconClicked)
        except Exception as e:
            print(e)


    def iconClicked(self, reason):
        # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        print('reason=%d' % reason)
        return
        if reason == 3:
            return
