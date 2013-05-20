# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/dlgchat.ui'
#
# Created: Mon May  3 02:02:11 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgChatRoster(object):
    def setupUi(self, dlgChatRoster):
        dlgChatRoster.setObjectName("dlgChatRoster")
        dlgChatRoster.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(dlgChatRoster)
        self.gridLayout.setObjectName("gridLayout")
        self.lblStatus = QtGui.QLabel(dlgChatRoster)
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout.addWidget(self.lblStatus, 0, 0, 1, 1)
        self.lstRoster = QtGui.QListWidget(dlgChatRoster)
        self.lstRoster.setObjectName("lstRoster")
        self.gridLayout.addWidget(self.lstRoster, 1, 0, 1, 1)

        self.retranslateUi(dlgChatRoster)
        QtCore.QMetaObject.connectSlotsByName(dlgChatRoster)

    def retranslateUi(self, dlgChatRoster):
        dlgChatRoster.setWindowTitle(QtGui.QApplication.translate("dlgChatRoster", "Tunnel Chat", None, QtGui.QApplication.UnicodeUTF8))
        self.lblStatus.setText(QtGui.QApplication.translate("dlgChatRoster", "Status: Offline", None, QtGui.QApplication.UnicodeUTF8))

