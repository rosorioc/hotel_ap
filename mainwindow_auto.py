# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 320)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btn_reboot = QtWidgets.QPushButton(self.centralWidget)
        self.btn_reboot.setGeometry(QtCore.QRect(380, 240, 81, 22))
        self.btn_reboot.setObjectName("btn_reboot")
        self.btn_shutdown = QtWidgets.QPushButton(self.centralWidget)
        self.btn_shutdown.setGeometry(QtCore.QRect(290, 240, 81, 22))
        self.btn_shutdown.setObjectName("btn_shutdown")
        self.btn_wlan = QtWidgets.QToolButton(self.centralWidget)
        self.btn_wlan.setGeometry(QtCore.QRect(50, 100, 131, 81))
        self.btn_wlan.setObjectName("btn_wlan")
        self.btn_browser = QtWidgets.QToolButton(self.centralWidget)
        self.btn_browser.setGeometry(QtCore.QRect(250, 100, 131, 81))
        self.btn_browser.setObjectName("btn_browser")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 460, 19))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_reboot.setText(_translate("MainWindow", "reboot"))
        self.btn_shutdown.setText(_translate("MainWindow", "shutdown"))
        self.btn_wlan.setText(_translate("MainWindow", "WLAN "))
        self.btn_browser.setText(_translate("MainWindow", "Browser"))

