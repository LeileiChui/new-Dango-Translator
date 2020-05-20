# -*- coding: utf-8 -*-
# @Time : 2020/5/20 19:14
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : set_IF.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets


class SetInterface(QtWidgets.QWidget):
    def __init__(self):
        super(SetInterface, self).__init__()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = SetInterface()
    w.show()
    sys.exit(app.exec_())
