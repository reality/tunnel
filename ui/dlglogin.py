# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/dlglogin.ui'
#
# Created: Tue Aug  3 12:05:32 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgLogin(object):
    def setupUi(self, dlgLogin):
        dlgLogin.setObjectName("dlgLogin")
        dlgLogin.resize(251, 204)
        self.edtUser = QtGui.QLineEdit(dlgLogin)
        self.edtUser.setGeometry(QtCore.QRect(30, 30, 191, 23))
        self.edtUser.setObjectName("edtUser")
        self.edtPass = QtGui.QLineEdit(dlgLogin)
        self.edtPass.setGeometry(QtCore.QRect(30, 80, 191, 23))
        self.edtPass.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.edtPass.setInputMask("")
        self.edtPass.setEchoMode(QtGui.QLineEdit.Password)
        self.edtPass.setObjectName("edtPass")
        self.lblUser = QtGui.QLabel(dlgLogin)
        self.lblUser.setGeometry(QtCore.QRect(30, 10, 191, 20))
        self.lblUser.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUser.setObjectName("lblUser")
        self.lblPass = QtGui.QLabel(dlgLogin)
        self.lblPass.setGeometry(QtCore.QRect(30, 60, 191, 20))
        self.lblPass.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPass.setObjectName("lblPass")
        self.btnLogin = QtGui.QPushButton(dlgLogin)
        self.btnLogin.setGeometry(QtCore.QRect(70, 160, 111, 22))
        self.btnLogin.setObjectName("btnLogin")
        self.edtServ = QtGui.QLineEdit(dlgLogin)
        self.edtServ.setGeometry(QtCore.QRect(30, 130, 191, 23))
        self.edtServ.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edtServ.setInputMask("")
        self.edtServ.setEchoMode(QtGui.QLineEdit.Normal)
        self.edtServ.setObjectName("edtServ")
        self.lblServ = QtGui.QLabel(dlgLogin)
        self.lblServ.setGeometry(QtCore.QRect(30, 110, 191, 20))
        self.lblServ.setAlignment(QtCore.Qt.AlignCenter)
        self.lblServ.setObjectName("lblServ")

        self.retranslateUi(dlgLogin)
        QtCore.QMetaObject.connectSlotsByName(dlgLogin)
        dlgLogin.setTabOrder(self.edtUser, self.edtPass)
        dlgLogin.setTabOrder(self.edtPass, self.edtServ)
        dlgLogin.setTabOrder(self.edtServ, self.btnLogin)

    def retranslateUi(self, dlgLogin):
        dlgLogin.setWindowTitle(QtGui.QApplication.translate("dlgLogin", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUser.setText(QtGui.QApplication.translate("dlgLogin", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPass.setText(QtGui.QApplication.translate("dlgLogin", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLogin.setText(QtGui.QApplication.translate("dlgLogin", "Enter tunnel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblServ.setText(QtGui.QApplication.translate("dlgLogin", "Server", None, QtGui.QApplication.UnicodeUTF8))

