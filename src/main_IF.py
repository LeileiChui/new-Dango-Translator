# -*- coding: utf-8 -*-
# @Time : 2020/5/19 12:45
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : main_IF.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui, QtCore
from src.utils.gloVarMan import glm
import src.utils.utils as utils
import qtawesome


class MainInterface(QtWidgets.QWidget):
    """
    软件主界面
    """
    width = 800 * glm.screen_scale_rate
    height = 150 * glm.screen_scale_rate
    tool_icon_size = 16 * glm.screen_scale_rate

    def __init__(self):
        super(MainInterface, self).__init__()
        self.resize(self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 设置程序图标和光标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(utils.resource_path('asserts/图标.ico')), QtGui.QIcon.Normal, QtGui.QIcon.On)
        cursor = QtGui.QCursor(QtGui.QPixmap(utils.resource_path('asserts/光标.png')), 0, 0)
        self.setWindowIcon(icon)
        self.setCursor(cursor)
        self.init_ui()

    def init_ui(self):
        self.dragLabel = QtWidgets.QLabel(self)
        self.dragLabel.setGeometry(0, 0, 4000, 4000)
        self.dragLabel.setStyleSheet('QLabel{background-color:green}')
        self.toolbar_layout = QtWidgets.QVBoxLayout(self)
        self.toolbar_layout.setContentsMargins(0, 0, 0, 0)
        self.toolbar_layout.addWidget(QtWidgets.QPushButton('测试'))
        self.toolbar_layout.addWidget(QtWidgets.QPushButton('测试'))
        self.toolbar_layout.addWidget(QtWidgets.QPushButton('测试'))
        self.toolbar_layout.addWidget(QtWidgets.QPushButton('测试'))
        self.toolbar_layout.addWidget(QtWidgets.QSizeGrip(self), 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        try:
            self._endPos = event.pos() - self._startPos
            self.move(self.pos() + self._endPos)
        except Exception as e:
            print(e)

    def mousePressEvent(self, event: QtGui.QMouseEvent):

        try:
            if event.button() == QtCore.Qt.LeftButton:
                self._isTracking = True
                self._startPos = QtCore.QPoint(event.x(), event.y())
        except Exception as e:
            print(e)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):

        try:
            if event.button() == QtCore.Qt.LeftButton:
                self._isTracking = False
                self._startPos = None
                self._endPos = None
        except Exception as e:
            glm.logger.info(str(e))

    # def enterEvent(self, QEvent):
    #     self.dragLabel.setStyleSheet('{background-color:rgba(62, 62, 62, 0.3)}')


# Test
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainInterface()
    w.show()
    sys.exit(app.exec_())
