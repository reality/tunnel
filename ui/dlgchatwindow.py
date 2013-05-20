# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/dlgchatwindow.ui'
#
# Created: Mon May  3 12:35:16 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgChatWindow(object):
    def setupUi(self, dlgChatWindow):
        dlgChatWindow.setObjectName("dlgChatWindow")
        dlgChatWindow.resize(408, 300)
        self.gridLayout = QtGui.QGridLayout(dlgChatWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.edtMessage = QtGui.QLineEdit(dlgChatWindow)
        self.edtMessage.setObjectName("edtMessage")
        self.gridLayout.addWidget(self.edtMessage, 2, 1, 1, 1)
        self.btnSend = QtGui.QPushButton(dlgChatWindow)
        self.btnSend.setObjectName("btnSend")
        self.gridLayout.addWidget(self.btnSend, 2, 2, 1, 1)
        self.txtChat = QtGui.QPlainTextEdit(dlgChatWindow)
        self.txtChat.setReadOnly(True)
        self.txtChat.setPlainText("")
        self.txtChat.setObjectName("txtChat")
        self.gridLayout.addWidget(self.txtChat, 1, 0, 1, 3)
        self.lblStatus = QtGui.QLabel(dlgChatWindow)
        self.lblStatus.setMinimumSize(QtCore.QSize(50, 0))
        self.lblStatus.setBaseSize(QtCore.QSize(50, 0))
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout.addWidget(self.lblStatus, 0, 0, 1, 3)

        self.retranslateUi(dlgChatWindow)
        QtCore.QMetaObject.connectSlotsByName(dlgChatWindow)

    def retranslateUi(self, dlgChatWindow):
        dlgChatWindow.setWindowTitle(QtGui.QApplication.translate("dlgChatWindow", "Chat with", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSend.setText(QtGui.QApplication.translate("dlgChatWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))

