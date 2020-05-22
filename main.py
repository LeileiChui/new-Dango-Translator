# -*- coding: utf-8 -*-
# @Time : 2020/5/19 16:56
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : main.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
from src.main_IF import MainInterface
from src.set_IF import SetInterface
import src.utils.utils as utils
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap, QFontDatabase, QFont
from src.dangoTray import MyTray
import sys


class DangoTranslator:
    def __init__(self, app: QApplication):
        self.app = app
        # 加载字体，需要在UI创建之前
        res = QFontDatabase.addApplicationFont(utils.resource_path('asserts/华康方圆体W7.ttf'))
        # 获取字体名字 print(QFontDatabase.applicationFontFamilies(0))
        self.main_IF = MainInterface()
        # self.main_IF.hide()
        self.set_IF = SetInterface()
        # self.set_IF.show()

    def run(self):
        self.main_IF.show()
        self.connect()
        self.creat_tray()
        sys.exit(app.exec_())

    def connect(self):
        self.main_IF.set_btn.clicked.connect(self.openSet_IF)
        self.main_IF.minus_btn.clicked.connect(self.main_IF.hide)
        self.main_IF.exit_btn.clicked.connect(self.app.quit)

    def openSet_IF(self):
        if not self.set_IF:
            self.set_IF = SetInterface()
        self.set_IF.show()

    def creat_tray(self):
        self.dangoTray = MyTray()
        self.dangoTray.setIcon(self.main_IF.icon)
        self.dangoTray.activated.connect(self.main_IF.show)
        dangoTrayMenu = QMenu(QApplication.desktop())
        restoreAct = QAction(u'还原', self.main_IF, triggered=self.main_IF.show)
        exitAct = QAction(u'退出', self.main_IF, triggered=self.app.quit)
        dangoTrayMenu.addAction(restoreAct)
        dangoTrayMenu.addAction(exitAct)
        # self.dangoTray.setContextMenu(dangoTrayMenu)
        self.dangoTray.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(False)
    dango = DangoTranslator(app)
    dango.run()
