# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.resize(955, 477)
        Widget.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.widget.setStyleSheet("background-color:#324157;")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.menu_1 = QtWidgets.QLabel(self.widget)
        self.menu_1.setMinimumSize(QtCore.QSize(150, 75))
        self.menu_1.setMaximumSize(QtCore.QSize(150, 75))
        self.menu_1.setStyleSheet("QLabel:hover{\n"
                                  "    background-color:#283446;\n"
                                  "}")
        self.menu_1.setObjectName("menu_1")
        self.verticalLayout.addWidget(self.menu_1)

        self.menu_2 = QtWidgets.QLabel(self.widget)
        self.menu_2.setMinimumSize(QtCore.QSize(150, 75))
        self.menu_2.setMaximumSize(QtCore.QSize(150, 75))
        self.menu_2.setStyleSheet("QLabel:hover{\n"
                                  "    background-color:#283446;\n"
                                  "}")
        self.menu_2.setObjectName("menu_2")
        self.verticalLayout.addWidget(self.menu_2)
        self.menu_3 = QtWidgets.QLabel(self.widget)
        self.menu_3.setMinimumSize(QtCore.QSize(150, 75))
        self.menu_3.setMaximumSize(QtCore.QSize(150, 75))
        self.menu_3.setStyleSheet("QLabel:hover{\n"
                                  "    background-color:#283446;\n"
                                  "}")
        self.menu_3.setObjectName("menu_3")
        self.verticalLayout.addWidget(self.menu_3)
        self.menu_4 = QtWidgets.QLabel(self.widget)
        self.menu_4.setMinimumSize(QtCore.QSize(150, 75))
        self.menu_4.setMaximumSize(QtCore.QSize(150, 75))
        self.menu_4.setStyleSheet("QLabel:hover{\n"
                                  "    background-color:#283446;\n"
                                  "}")
        self.menu_4.setObjectName("menu_4")
        self.verticalLayout.addWidget(self.menu_4)
        self.menu_5 = QtWidgets.QLabel(self.widget)
        self.menu_5.setMinimumSize(QtCore.QSize(150, 75))
        self.menu_5.setMaximumSize(QtCore.QSize(150, 75))
        self.menu_5.setStyleSheet("QLabel:hover{\n"
                                  "    background-color:#283446;\n"
                                  "}")
        self.menu_5.setObjectName("menu_5")
        self.verticalLayout.addWidget(self.menu_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(30, 20, 50, 40)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setStyleSheet("background-color:rgb(0, 170, 255)\n"
                                    "")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
