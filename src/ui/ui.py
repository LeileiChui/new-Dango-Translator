# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 463)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setSizeGripEnabled(True)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-style:italic; color:#032f62;\">self</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">.QuitButton </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#d73a49;\">= </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#6f42c1;\">QPushButton</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">(qtawesome.</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#6f42c1;\">icon</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">(</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-weight:600; color:#008080;\">\'fa.times\'</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">, </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#e36209;\">color</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#d73a49;\">=</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-weight:600; color:#008080;\">\'white\'</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">), </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-weight:600; color:#008080;\">&quot;&quot;</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">, </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-style:italic; color:#032f62;\">self</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">)<br /></span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-style:italic; color:#032f62;\">self</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">.QuitButton.</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#6f42c1;\">setIconSize</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">(</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#6f42c1;\">QSize</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">(</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#005cc5;\">20</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">, </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#005cc5;\">20</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">))<br /></span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-style:italic; color:#032f62;\">self</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">.QuitButton.</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#6f42c1;\">setGeometry</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">(</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#6f42c1;\">QRect</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">(</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#005cc5;\">567 </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#d73a49;\">* </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-style:italic; color:#032f62;\">self</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">.rate, </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#005cc5;\">5 </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#d73a49;\">* </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-style:italic; color:#032f62;\">self</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">.rate, </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#005cc5;\">20 </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#d73a49;\">* </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-style:italic; color:#032f62;\">self</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">.rate, </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#005cc5;\">20 </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#d73a49;\">* </span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-style:italic; color:#032f62;\">self</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">.rate))<br /></span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-style:italic; color:#032f62;\">self</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">.QuitButton.</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#6f42c1;\">setToolTip</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">(</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-weight:600; color:#008080;\">\'&lt;b&gt;</span><span style=\" font-family:\'.萍方-简\'; font-size:12pt; font-weight:600; color:#008080;\">退出程序</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-weight:600; color:#008080;\"> Quit&lt;/b&gt;\'</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">)<br /></span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-style:italic; color:#032f62;\">self</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">.QuitButton.</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#6f42c1;\">setStyleSheet</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">(</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-weight:600; color:#008080;\">&quot;background-color:rgba(62, 62, 62, 0);&quot;</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">)<br /></span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-style:italic; color:#032f62;\">self</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">.QuitButton.</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#6f42c1;\">setCursor</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">(</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#6f42c1;\">QCursor</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">(Qt.PointingHandCursor))<br /></span><span style=\" font-family:\'Fira Code\'; font-size:12pt; font-style:italic; color:#032f62;\">self</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">.QuitButton.</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#6f42c1;\">hide</span><span style=\" font-family:\'Fira Code\'; font-size:12pt; color:#24292e;\">()</span></p></body></html>"))
