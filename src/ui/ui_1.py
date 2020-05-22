# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from src.utils.gloVarMan import glm
import qtawesome
from functools import partial
import webbrowser


class Ui_Widget(object):
    def setupUi(self, Widget: QtWidgets.QWidget):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout_7.setContentsMargins(50, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.formWidget = QtWidgets.QWidget(Widget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.formWidget)
        self.verticalLayout.setSpacing(10)
        self.widget = QtWidgets.QWidget(self.formWidget)
        self.widget.setMinimumSize(QtCore.QSize(100, 26))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.bd_ocr_label = QtWidgets.QLabel(self.widget)
        self.bd_ocr_label.setText(
            '<p><font color="red">(必填)</font>OCR API: 用于识别要翻译的文字&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>')
        self.horizontalLayout.addWidget(self.bd_ocr_label)
        self.bd_OCR_guide_btn = self.get_guide_btn(self.widget, '注册指南')

        self.horizontalLayout.addWidget(self.bd_OCR_guide_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget)
        self.widget_13 = QtWidgets.QWidget(self.formWidget)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(20)

        self.bd_ocr_id = self.get_lineEdit(self.widget_13, 'OCR API Key')
        self.horizontalLayout_13.addWidget(self.bd_ocr_id)

        self.label_12 = QtWidgets.QLabel(self.widget_13)
        self.label_12.setMinimumSize(QtCore.QSize(0, 26))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 26))
        self.label_12.setText('<p style="color:red">*</p>')
        self.horizontalLayout_13.addWidget(self.label_12)
        self.verticalLayout.addWidget(self.widget_13)
        self.widget_2 = QtWidgets.QWidget(self.formWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(20)
        self.bd_ocr_key = self.get_lineEdit(self.widget_2, 'OCR API Secret')
        self.horizontalLayout_2.addWidget(self.bd_ocr_key)

        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMinimumSize(QtCore.QSize(0, 26))
        self.label.setMaximumSize(QtCore.QSize(16777215, 26))
        self.label.setText('<p style="color:red">*</p>')
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_7.addWidget(self.formWidget)
        self.formWidget_2 = QtWidgets.QWidget(Widget)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.formWidget_2)
        self.verticalLayout_6.setSpacing(10)
        self.widget_7 = QtWidgets.QWidget(self.formWidget_2)
        self.widget_7.setMinimumSize(QtCore.QSize(100, 26))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.bd_trans_label = QtWidgets.QLabel(self.widget_7)
        self.bd_trans_label.setText('百度翻译API    ')
        self.horizontalLayout_7.addWidget(self.bd_trans_label)
        self.bd_trans_guide_btn = self.get_guide_btn(self.widget_7, '注册指南')
        self.bd_query_guide_btn = self.get_guide_btn(self.widget_7, '额度查询')

        self.horizontalLayout_7.addWidget(self.bd_trans_guide_btn)
        self.horizontalLayout_7.addWidget(self.bd_query_guide_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_6.addWidget(self.widget_7)
        self.widget_14 = QtWidgets.QWidget(self.formWidget_2)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.bd_trans_id = self.get_lineEdit(self.widget_14, '百度翻译 APP ID')
        self.horizontalLayout_14.addWidget(self.bd_trans_id)
        self.label_14 = QtWidgets.QLabel(self.widget_14)
        self.label_14.setMinimumSize(QtCore.QSize(0, 26))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 26))
        self.horizontalLayout_14.addWidget(self.label_14)
        self.verticalLayout_6.addWidget(self.widget_14)
        self.widget_8 = QtWidgets.QWidget(self.formWidget_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.bd_trans_key = self.get_lineEdit(self.widget_8, '百度翻译 APP 密钥')
        self.horizontalLayout_8.addWidget(self.bd_trans_key)
        self.label_8 = QtWidgets.QLabel(self.widget_8)
        self.label_8.setMinimumSize(QtCore.QSize(0, 26))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 26))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.verticalLayout_6.addWidget(self.widget_8)
        self.verticalLayout_7.addWidget(self.formWidget_2)
        self.formWidget_3 = QtWidgets.QWidget(Widget)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.formWidget_3)
        self.verticalLayout_5.setSpacing(10)
        self.widget_9 = QtWidgets.QWidget(self.formWidget_3)
        self.widget_9.setMinimumSize(QtCore.QSize(100, 26))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.tencent_trans_label = QtWidgets.QLabel(self.widget_9)
        self.tencent_trans_label.setText('腾讯翻译API    ')
        self.horizontalLayout_9.addWidget(self.tencent_trans_label)
        self.tencent_trans_guide_btn = self.get_guide_btn(self.widget_9, '注册指南')
        self.tencent_query_guide_btn = self.get_guide_btn(self.widget_9, '额度查询')

        self.horizontalLayout_9.addWidget(self.tencent_trans_guide_btn)
        self.horizontalLayout_9.addWidget(self.tencent_query_guide_btn)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_5.addWidget(self.widget_9)
        self.widget_15 = QtWidgets.QWidget(self.formWidget_3)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.tencent_trans_id = self.get_lineEdit(self.widget_15, '腾讯翻译API SecretId')
        self.horizontalLayout_15.addWidget(self.tencent_trans_id)
        self.label_15 = QtWidgets.QLabel(self.widget_15)
        self.label_15.setMinimumSize(QtCore.QSize(0, 26))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 26))
        self.horizontalLayout_15.addWidget(self.label_15)
        self.verticalLayout_5.addWidget(self.widget_15)
        self.widget_10 = QtWidgets.QWidget(self.formWidget_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.tencent_trans_key = self.get_lineEdit(self.widget_10, '腾讯翻译API SecretKey')
        self.horizontalLayout_10.addWidget(self.tencent_trans_key)
        self.label_10 = QtWidgets.QLabel(self.widget_10)
        self.label_10.setMinimumSize(QtCore.QSize(0, 26))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 26))
        self.horizontalLayout_10.addWidget(self.label_10)
        self.verticalLayout_5.addWidget(self.widget_10)
        self.verticalLayout_7.addWidget(self.formWidget_3)
        self.formWidget_4 = QtWidgets.QWidget(Widget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.formWidget_4)
        self.verticalLayout_4.setSpacing(10)
        self.widget_11 = QtWidgets.QWidget(self.formWidget_4)
        self.widget_11.setMinimumSize(QtCore.QSize(100, 26))
        self.widget_11.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.cy_trans_label = QtWidgets.QLabel(self.widget_11)
        self.cy_trans_label.setText('彩云翻译API    ')
        self.horizontalLayout_11.addWidget(self.cy_trans_label)
        self.cy_trans_guide_btn = self.get_guide_btn(self.widget_11, '注册指南')
        self.cy_trans_query_btn = self.get_guide_btn(self.widget_11, '额度查询')

        self.horizontalLayout_11.addWidget(self.cy_trans_guide_btn)
        self.horizontalLayout_11.addWidget(self.cy_trans_query_btn)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.verticalLayout_4.addWidget(self.widget_11)
        self.widget_16 = QtWidgets.QWidget(self.formWidget_4)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.cy_trans_token = self.get_lineEdit(self.widget_16, '彩云小泽API Token')
        self.horizontalLayout_16.addWidget(self.cy_trans_token)
        self.label_16 = QtWidgets.QLabel(self.widget_16)
        self.label_16.setMinimumSize(QtCore.QSize(0, 26))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 26))
        self.horizontalLayout_16.addWidget(self.label_16)
        self.verticalLayout_4.addWidget(self.widget_16)
        self.widget_12 = QtWidgets.QWidget(self.formWidget_4)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.verticalLayout_4.addWidget(self.widget_12)
        self.verticalLayout_7.addWidget(self.formWidget_4)

        self.setLabelFont()

    @staticmethod
    def get_guide_btn(widget: QtWidgets.QWidget, text: str):
        button = QtWidgets.QPushButton(qtawesome.icon('fa.arrow-circle-right', color='grey'), text, widget)
        button.setIconSize(QtCore.QSize(25, 25))

        button.setMinimumWidth(100)
        button.setStyleSheet("background: transparent;"
                             "font-size:20px;"
                             "font-family:华康方圆体W7;")
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.clicked.connect(partial(webbrowser.open, 'https://www.baidu.com/s?ie=UTF-8&wd=' + text))
        return button

    @staticmethod
    def get_lineEdit(widget: QtWidgets.QWidget, placeholder: str):
        lineEdit = QtWidgets.QLineEdit(widget)
        lineEdit.setMaximumWidth(600)
        lineEdit.setStyleSheet("QLineEdit {"
                               "background: transparent;"
                               "border-width:0;"
                               "border-style:outset;"
                               "border-bottom: 2px solid #92a8d1;"
                               "font-size:20px;"
                               "font-family:微软雅黑;}"
                               "QLineEdit:focus {""border-bottom: 2px dashed #9265d1;""}")
        lineEdit.setPlaceholderText(placeholder)
        return lineEdit

    def setLabelFont(self):
        for name, obj in vars(self).items():
            if isinstance(obj, QtWidgets.QLabel):
                obj.setStyleSheet("font-size:20px;"
                                  "font-family:华康方圆体W7;")
