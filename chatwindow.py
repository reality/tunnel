#!/usr/bin/env python
"""
TODO: Document me
"""

__date__ = "$02-Apr-2010 01:32:49$"

import sys
import time
from PyQt4 import QtCore, QtGui

sys.path.insert(0, 'ui')
from dlgchatwindow import Ui_dlgChatWindow
del sys.path[0]

class ChatWindow(QtGui.QDialog):
    """Dialog for a chat window also handling clientside chat stuff"""

    def __init__(self, parent, id, roster_window, first_message=False, win_parent=None):
        """Initialise dialog"""
        QtGui.QDialog.__init__(self, win_parent)
        self.parent = parent
        self.ui = Ui_dlgChatWindow()
        self.ui.setupUi(self)

        self.new_message_signal = QtCore.SIGNAL("new_message()")
        self.connect(self, self.new_message_signal, self.update_chat_text)

        self.close_chat_signal = QtCore.SIGNAL("closed(QString)")
        self.connect(self, self.close_chat_signal, roster_window.close_chat)

        QtCore.QObject.connect(self.ui.btnSend, \
        QtCore.SIGNAL("clicked()"), self.__click_btn_send)

        self.roster_object = self.parent.xmpp.roster[id]
        self.chat_with = id
        self.chat = []

        if first_message != False:
            self.ui.txtChat.appendPlainText(self.chat_with + ": " +
            str(first_message))

        self.setWindowTitle("Chat with " + id)
        if "tunnel" in self.roster_object["presence"]:
            self.ui.lblStatus.setText(str(self.chat_with) + " - " +
            str(self.roster_object["presence"]["tunnel"]["status"]))
        else:
            self.ui.lblStatus.setText(str(self.chat_with) + " - " + "Not connected via tunnel")

    def __click_btn_send(self):
        self.parent.xmpp.sendMessage(self.chat_with,
        str(self.ui.edtMessage.text()))
        self.ui.txtChat.appendPlainText("me: " + self.ui.edtMessage.text())
        self.ui.edtMessage.clear()

    def incoming_message(self, message):
        self.chat.append(message)
        self.emit(self.new_message_signal)

    def update_chat_text(self):
        self.ui.txtChat.appendPlainText(self.chat_with + ": " + self.chat[-1]["body"])

    def closeEvent(self, e):
        self.emit(self.close_chat_signal, self.chat_with)
