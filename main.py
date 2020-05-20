# -*- coding: utf-8 -*-
# @Time : 2020/5/19 16:56
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : main.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
from src.main_IF import MainInterface
from PyQt5.QtWidgets import QApplication
import sys


class DangoTranslator:
    def __init__(self, app: QApplication):
        self.app = app
        self.main_IF = MainInterface()

    def run(self):
        self.main_IF.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dango = DangoTranslator(app)
    dango.run()
