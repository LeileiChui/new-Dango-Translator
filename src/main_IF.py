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
from src.ui.switch_btn import SwitchBtn
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
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(utils.resource_path('asserts/图标.ico')), QtGui.QIcon.Normal, QtGui.QIcon.On)
        cursor = QtGui.QCursor(QtGui.QPixmap(utils.resource_path('asserts/光标.png')), 0, 0)
        self.setWindowIcon(self.icon)
        self.setCursor(cursor)
        # 加载字体
        self.font = QtGui.QFont('华康方圆体W7')
        self.font.setPointSize(15)
        # 设置文本样式
        self.format = QtGui.QTextCharFormat()
        self.format.setTextOutline(
            QtGui.QPen(QtGui.QColor('#FF69B4'), 0.7, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        # 存储toolbar内的按钮对象
        self.buttons = []
        self.translate_text_trans = 0.3
        self.init_ui()
        # 预先隐藏所有按钮
        for btn in self.buttons:
            btn.hide()

    def init_ui(self):
        # 垂直布局
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        # 拖动辅助控件
        self.dragLabel = QtWidgets.QLabel(self)
        self.dragLabel.setGeometry(0, 0, 4000, 4000)
        self.dragLabel.setObjectName('dragLabel')

        # 顶部按钮
        toolbar_placeholder = QtWidgets.QWidget()
        toolbar_placeholder.setMinimumHeight(30 * glm.screen_scale_rate)
        # toolbar_placeholder.setStyleSheet("background-color:green")
        self.main_layout.addWidget(toolbar_placeholder)

        self.toolbar_layout = QtWidgets.QHBoxLayout(toolbar_placeholder)
        self.main_layout.addLayout(self.toolbar_layout)
        self.toolbar_layout.setContentsMargins(0, 0, 0, 0)
        self.toolbar_layout.addSpacerItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.start_btn = self.new_button('fa.play', '<b>开始翻译</b>')
        # fa.square
        self.toolbar_layout.addWidget(self.start_btn)

        self.play_voice_btn = self.new_button('fa.music', '<b>朗读原文</b><br>朗读识别到的原文')
        self.toolbar_layout.addWidget(self.play_voice_btn)

        self.history_btn = self.new_button('fa.history', '<b>翻译历史</b><br>查看翻译历史记录')
        self.toolbar_layout.addWidget(self.history_btn)

        self.copy_btn = self.new_button('fa5s.copy', '<b>复制</b><br>复制翻译结果')
        self.toolbar_layout.addWidget(self.copy_btn)

        self.switch_btn = SwitchBtn()
        self.switch_btn.setToolTip('<b>模式 Mode</b><br>手动翻译/自动翻译')
        self.switch_btn.setMinimumSize(50 * glm.screen_scale_rate, 20 * glm.screen_scale_rate)
        self.switch_btn.setMaximumSize(50 * glm.screen_scale_rate, 20 * glm.screen_scale_rate)
        self.switch_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolbar_layout.addWidget(self.switch_btn)
        self.buttons.append(self.switch_btn)

        self.set_btn = self.new_button('fa5s.cog', '<b>设置</b>')
        self.toolbar_layout.addWidget(self.set_btn)
        self.donate_btn = self.new_button('fa5s.donate', 'yellow', '<b>充电</b><br>我要给团子充电支持！')
        self.toolbar_layout.addWidget(self.donate_btn)

        self.minus_btn = self.new_button('fa.minus', 'green', '<b>最小化</b>最小化到托盘')
        self.toolbar_layout.addWidget(self.minus_btn)

        self.exit_btn = self.new_button('fa5s.times', 'red', '<b>关闭</b><br>关闭团子翻译器')
        self.toolbar_layout.addWidget(self.exit_btn)

        self.toolbar_layout.addSpacerItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        # 翻译文本
        self.translate_text = QtWidgets.QTextBrowser()
        self.main_layout.addWidget(self.translate_text)
        self.translate_text.stackUnder(self.dragLabel)
        self.translate_text.setObjectName('translate_text')
        self.translate_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.translate_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.translate_text.setFont(self.font)
        self.translate_text.mergeCurrentCharFormat(self.format)
        self.translate_text.append("团子翻译器 ver4.0 --- By：Leil, Forked form 胖次团子")
        self.translate_text.append("交流群：1050705995   加群可获取最新版本并解惑翻译器一切问题")
        self.translate_text.append("喜欢这个软件可以点击上方的电池按钮给团子个充电支持吗 ❤")
        self.translate_text.append("团子会努力保持更新让大家用上更好的团子翻译器哒！")

        # 右下角缩放按钮
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setMaximumHeight(10 * glm.screen_scale_rate)
        self.main_layout.addWidget(self.statusbar)

        self.leaveEvent(QEvent=None)

    def new_button(self, icon_type: str, color: str = 'black', tool_tip: str = ""):
        button = QtWidgets.QPushButton(qtawesome.icon(icon_type, color=color), "", self)
        button.setIconSize(QtCore.QSize(self.tool_icon_size, self.tool_icon_size))
        button.setToolTip(tool_tip)
        button.setStyleSheet("background: transparent")
        button.setMinimumWidth(40 * glm.screen_scale_rate)
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttons.append(button)
        return button

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

    def enterEvent(self, QEvent):
        for btn in self.buttons:
            btn.show()
        self.changeToHoverUI(True)

    def leaveEvent(self, QEvent):
        for btn in self.buttons:
            btn.hide()
        self.changeToHoverUI(False)

    def changeToHoverUI(self, status: bool):
        if not status:
            trans = self.translate_text_trans
        else:
            trans = 0
        self.translate_text.setStyleSheet("border-width:0;\
                                                  border-style:outset;\
                                                  border-top:0px solid #e8f3f9;\
                                                  color:white;\
                                                  font-weight: bold;\
                                                  background-color:rgba(62, 62, 62, %f)" % trans)

        self.statusbar.setStyleSheet(
            'QStatusBar{background-color:rgba(62, 62, 62,%f)}' % trans)

        self.dragLabel.setStyleSheet(
            'QLabel#dragLabel{background-color:rgba(62, 62, 62,%f)}' % (self.translate_text_trans - trans + 0.01))


# Test
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainInterface()
    w.show()
    sys.exit(app.exec_())
