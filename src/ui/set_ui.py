# -*- coding: utf-8 -*-
# @Time : 2020/5/21 10:29
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : set_ui.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from src.ui.ui_1 import Ui_Widget as ui_1
from src.utils.gloVarMan import glm
import sip


def get_apiSet_widget():
    set_widget = QtWidgets.QWidget()
    ui = ui_1()
    # set_widget.setStyleSheet('background-color:rgba(62,62,62,0.3);')
    ui.setupUi(set_widget)

    return set_widget


def get_trans_resources_widget():
    set_widget = QtWidgets.QWidget()
    set_widget.setStyleSheet('background-color:yellow;')
    return set_widget


def get_trans_ui_widget():
    set_widget = QtWidgets.QWidget()
    set_widget.setStyleSheet('background-color:blue;')
    return set_widget


def get_other_widget():
    set_widget = QtWidgets.QWidget()
    set_widget.setStyleSheet('background-color:green;')
    return set_widget


def get_supportMe_widget():
    set_widget = QtWidgets.QWidget()
    set_widget.setStyleSheet('background-color:pink;')
    return set_widget


ui_set_func = [get_apiSet_widget,
               get_trans_resources_widget,
               get_trans_ui_widget,
               get_other_widget,
               get_supportMe_widget
               ]
