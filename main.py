# -*- coding: utf-8 -*-
# @Time : 2020/5/19 16:56
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : main.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
from src.main_IF import MainInterface
from src.set_IF import SetInterface
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap
from src.dangoTray import MyTray
import sys


class DangoTranslator:
    def __init__(self, app: QApplication):
        self.app = app
        self.main_IF = MainInterface()
        self.set_IF = None

    def run(self):
        self.main_IF.show()
        self.connect()
        self.creat_tray()
        sys.exit(app.exec_())

    def connect(self):
        self.main_IF.set_btn.clicked.connect(self.openSet_IF)
        self.main_IF.minus_btn.clicked.connect(self.close_main_IF)
        self.main_IF.exit_btn.clicked.connect(self.app.quit)

    def openSet_IF(self):
        if not self.set_IF:
            self.set_IF = SetInterface()
        self.set_IF.show()

    def close_main_IF(self):
        self.main_IF.close()
        self.dangoTray.show()

    def open_main_IF(self):
        self.main_IF.show()
        self.dangoTray.hide()

    def creat_tray(self):
        self.dangoTray = QSystemTrayIcon()
        self.dangoTray.setIcon(self.main_IF.icon)
        self.dangoTray.activated.connect(self.main_IF.show)
        dangoTrayMenu = QMenu(QApplication.desktop())
        restoreAct = QAction(u'还原', self.main_IF, triggered=self.open_main_IF)
        exitAct = QAction(u'退出', self.main_IF, triggered=self.app.quit)
        dangoTrayMenu.addAction(restoreAct)
        dangoTrayMenu.addAction(exitAct)
        self.dangoTray.setContextMenu(dangoTrayMenu)
        self.dangoTray.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(False)
    dango = DangoTranslator(app)
    dango.run()
