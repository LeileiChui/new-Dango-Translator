# -*- coding: utf-8 -*-
# @Time : 2020/5/19 12:45
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : main_IF.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from src.ui.ui import Ui_Widget


class MainInterface(QWidget):
    """
    软件主界面
    """

    def __init__(self):
        super(MainInterface, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


# Test
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainInterface()
    w.show()
    sys.exit(app.exec_())
