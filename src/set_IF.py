# -*- coding: utf-8 -*-
# @Time : 2020/5/20 19:14
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : set_IF.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import src.utils.utils as utils
from src.ui.set_ui import ui_set_func
from src.utils.gloVarMan import glm


class SetInterface(QtWidgets.QWidget):
    def __init__(self):
        super(SetInterface, self).__init__()
        self.menu_name = ['API 设置', '翻译源设置', '翻译样式', '其他设置', '支持作者']
        self.set_widget = [i() for i in ui_set_func]
        self.font = glm.setUI_font
        self.init_ui()
        # 当前菜单index，默认为充电界面
        self.curIndex = 0
        self.menu_switch(self.curIndex)

    def init_ui(self):
        self.resize(1120, 700)
        self.root_layout = QtWidgets.QHBoxLayout(self)
        self.root_layout.setContentsMargins(0, 0, 0, 0)
        self.root_layout.setSpacing(0)
        # 侧边菜单栏
        self.menubar = QtWidgets.QWidget(self)
        self.menubar.setMaximumWidth(150)
        self.menubar.setStyleSheet("background-color:white;")
        self.root_layout.addWidget(self.menubar)

        # 右侧主界面
        self.main_area = QtWidgets.QWidget(self)
        self.root_layout.addWidget(self.main_area)
        self.main_area.setStyleSheet('''background-color:white
        ''')
        self.main_area_layout = QtWidgets.QVBoxLayout(self.main_area)
        self.main_area_layout.setContentsMargins(30, 20, 30, 10)
        self.main_area_layout.setSpacing(0)
        # 添加各个设置界面
        for i in self.set_widget:
            self.main_area_layout.addWidget(i)
            i.hide()
        # 注，声明控件必须在设置界面后导入，否则出现相对位置错误
        statementLabel = QtWidgets.QLabel()
        statementLabel.setMaximumHeight(100)
        statementLabel.setStyleSheet('''background-color:white;
                                     color:red;''')
        statementLabel.setFont(self.font)
        statementLabel.setText(
            "<p>说明：①<a style='text-decoration: none; font-family:微软雅黑;' "
            "href='https://github.com/LeileiChui/new-Dango-Translator'>new Dango翻译器</a>基于<a style='text-decoration: "
            "none;font-family:微软雅黑;' href='https://github.com/PantsuDango/Dango-Translator'>团子翻译器</a"
            ">，感谢胖次团子的前期工作与无私奉献</p> "
            "<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;②new Dango翻译器是免费软件，如你是通过第三方购买获得，请<a style='text-decoration: none;' "
            "href='tencent://message/?uin=2501440197'>联系我</a></p> "
            "<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;③加群可获取最新版本以及交流解惑，结交同好</p>")
        statementLabel.setOpenExternalLinks(True)
        self.main_area_layout.addWidget(statementLabel)

        self.menubar_layout = QtWidgets.QVBoxLayout(self.menubar)
        self.menubar_layout.setContentsMargins(0, 0, 0, 0)
        self.menubar_layout.setSpacing(0)
        # logo图片，
        # TODO 个性化设置
        self.logo_label = QtWidgets.QLabel()
        logo = QtGui.QPixmap(utils.resource_path('asserts/logo.png'))
        logo = logo.scaled(150, 150, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        self.logo_label.setMinimumSize(150, 150)
        self.logo_label.setPixmap(logo)
        self.menubar_layout.addWidget(self.logo_label)
        # 添加菜单项
        from functools import partial
        for index in range(5):
            menu_item = QtWidgets.QPushButton(self.menubar)
            menu_item.setText(self.menu_name[index])
            menu_item.setMinimumSize(QtCore.QSize(150, 75))
            menu_item.setMaximumSize(QtCore.QSize(150, 75))
            menu_item.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            menu_item.setFont(self.font)
            menu_item.setStyleSheet('''QPushButton{
                                        border: 0 none;
                                        outline: none;
                                        text-align:left;
                                        padding-left:10px;
                                        background-color:white;
                                    }
                                    QPushButton:hover{
                                        border: 0 none;
                                        outline: none;
                                        background-color:pink;
                                    }
                                    QPushButton:focus{
                                        border: 0 none;
                                        outline: none;
                                    }
                                    QPushButton:pressed{
                                        border: 0 none;
                                        outline: none;
                                    }
                                    ''')
            # 此处不可使用lambda函数
            menu_item.clicked.connect(partial(self.menu_switch, index))
            self.menubar_layout.addWidget(menu_item)
        del partial
        menubar_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menubar_layout.addItem(menubar_spacer)

    def menu_switch(self, index):
        if self.set_widget[index] not in self.main_area.children():
            self.main_area_layout.addWidget(self.set_widget[index])

        if self.curIndex == index and self.set_widget[index].isHidden():
            self.set_widget[index].show()
            return
        self.set_widget[self.curIndex].hide()
        self.curIndex = index
        self.set_widget[self.curIndex].show()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = SetInterface()
    w.show()
    sys.exit(app.exec_())
