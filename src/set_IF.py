# -*- coding: utf-8 -*-
# @Time : 2020/5/20 19:14
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : set_IF.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from src.ui.ui import Ui_Widget


class SetInterface(QtWidgets.QWidget):
    def __init__(self):
        super(SetInterface, self).__init__()
        # self.ui = Ui_Widget()
        # self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.resize(1000, 500)
        self.root_layout = QtWidgets.QHBoxLayout(self)
        self.root_layout.setContentsMargins(0, 0, 0, 0)
        self.root_layout.setSpacing(0)
        # 侧边菜单栏
        self.menubar = QtWidgets.QWidget(self)
        self.menubar.setMaximumWidth(150)
        self.menubar.setStyleSheet("background-color:rgba(50,65,87,0.5);")
        self.root_layout.addWidget(self.menubar)

        # 右侧主界面
        self.main_area = QtWidgets.QWidget(self)
        self.root_layout.addWidget(self.main_area)

        self.menubar_layout = QtWidgets.QVBoxLayout(self.menubar)
        self.menubar_layout.setContentsMargins(0, 0, 0, 0)
        self.menubar_layout.setSpacing(0)

        for i in range(5):
            self.menu_item = QtWidgets.QLabel(self.menubar)
            self.menu_item.setMinimumSize(QtCore.QSize(150, 75))
            self.menu_item.setMaximumSize(QtCore.QSize(150, 75))
            self.menu_item.setStyleSheet("QLabel:hover{\n"
                                         "    background-color:#283446;\n"
                                         "}")
            self.menu_item.setObjectName("menu_item_%d" % i)
            self.menubar_layout.addWidget(self.menu_item)

        menubar_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menubar_layout.addItem(menubar_spacer)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = SetInterface()
    w.show()
    sys.exit(app.exec_())
