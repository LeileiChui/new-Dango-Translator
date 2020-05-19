# -*- coding: utf-8 -*-
# @Time : 2020/5/19 16:56
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : main.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

    def closeEvent(self, QCloseEvent):
        self.hide()
        return QCloseEvent.ignore()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
