# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(568, 189)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_USUARIO = QtGui.QLabel(self.centralwidget)
        self.label_USUARIO.setObjectName(_fromUtf8("label_USUARIO"))
        self.gridLayout.addWidget(self.label_USUARIO, 0, 0, 1, 1)
        self.lineEdit_USUARIO = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_USUARIO.setObjectName(_fromUtf8("lineEdit_USUARIO"))
        self.gridLayout.addWidget(self.lineEdit_USUARIO, 0, 1, 1, 1)
        self.pushButton_ACEPUSER = QtGui.QPushButton(self.centralwidget)
        self.pushButton_ACEPUSER.setObjectName(_fromUtf8("pushButton_ACEPUSER"))
        self.gridLayout.addWidget(self.pushButton_ACEPUSER, 0, 2, 1, 1)
        self.label_MSJUSER = QtGui.QLabel(self.centralwidget)
        self.label_MSJUSER.setText(_fromUtf8(""))
        self.label_MSJUSER.setObjectName(_fromUtf8("label_MSJUSER"))
        self.gridLayout.addWidget(self.label_MSJUSER, 1, 0, 1, 3)
        self.label_PASSWORD = QtGui.QLabel(self.centralwidget)
        self.label_PASSWORD.setObjectName(_fromUtf8("label_PASSWORD"))
        self.gridLayout.addWidget(self.label_PASSWORD, 2, 0, 1, 1)
        self.lineEdit_PASSWORD = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_PASSWORD.setObjectName(_fromUtf8("lineEdit_PASSWORD"))
        self.gridLayout.addWidget(self.lineEdit_PASSWORD, 2, 1, 1, 1)
        self.pushButton_ACEPPASS = QtGui.QPushButton(self.centralwidget)
        self.pushButton_ACEPPASS.setObjectName(_fromUtf8("pushButton_ACEPPASS"))
        self.gridLayout.addWidget(self.pushButton_ACEPPASS, 2, 2, 1, 1)
        self.label_MSJPASS = QtGui.QLabel(self.centralwidget)
        self.label_MSJPASS.setText(_fromUtf8(""))
        self.label_MSJPASS.setObjectName(_fromUtf8("label_MSJPASS"))
        self.gridLayout.addWidget(self.label_MSJPASS, 3, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_USUARIO.setText(_translate("MainWindow", "USUARIO:", None))
        self.pushButton_ACEPUSER.setText(_translate("MainWindow", "ACEPTAR", None))
        self.label_PASSWORD.setText(_translate("MainWindow", "PASSWORD:", None))
        self.pushButton_ACEPPASS.setText(_translate("MainWindow", "ACEPTAR", None))