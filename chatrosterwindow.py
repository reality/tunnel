#!/usr/bin/env python
"""
TODO: Document me
"""

__date__ = "$28-Apr-2010 20:54:49$"

import sys
from PyQt4 import QtCore, QtGui

from chatwindow import ChatWindow

sys.path.insert(0, 'ui')
from dlgchat import Ui_dlgChatRoster
del sys.path[0]

class ChatRosterWindow(QtGui.QDialog):
    """Dialog for chat window also handling clientside chat stuff"""

    def __init__(self, parent, win_parent=None):
        """Initialise dialog"""
        QtGui.QDialog.__init__(self, win_parent)
        self.parent = parent
        self.ui = Ui_dlgChatRoster()
        self.ui.setupUi(self)

        self.roster_timer = QtCore.QTimer(self)

        self.new_window_signal = QtCore.SIGNAL("new_window_signal(QString, QString)")
        self.connect(self, self.new_window_signal, self.open_chat_window)

        self.authenticated = False
        self.chats = {}

        self.roster_names = {}

        QtCore.QObject.connect(self.ui.lstRoster, \
            QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), self.__activate_roster_item)
        QtCore.QObject.connect(self.roster_timer, QtCore.SIGNAL("timeout()"),
            self.trigger_roster_update)


    def __activate_roster_item(self, item):
        """This will open the chat window"""
        # Check against roster ID to prevent name clashes
        if not str(item.text()) in self.parent.xmpp.roster:
            self.open_chat_window(self.roster_names[str(item.text())])
        else:
            self.open_chat_window(str(item.text()))

    def session_start(self, event):
        self.parent.xmpp.add_event_handler("roster_update", self.roster_update)
        self.trigger_roster_update()
        self.ui.lblStatus.setText("Status: Online")
        
    def incoming_message(self, message):
        msg_from = str(message["from"]).split("/")[0]
        if msg_from in self.chats:
            self.chats[msg_from].incoming_message(message)
        else:
            self.emit(self.new_window_signal, msg_from, message["body"])
            self.incoming_message(message)

    def open_chat_window(self, id, first_message=False):
        id = str(id)
        self.chats[id] = ChatWindow(self.parent, id, self, first_message)
        self.chats[id].show()

    def trigger_roster_update(self):
        self.parent.xmpp.get_roster()

    def roster_update(self, roster):
        self.ui.lstRoster.clear()
        self.roster_names = {}

        roster = self.parent.xmpp.client_roster

        for id in roster:
            if roster[id]['presence']:
                print('online')
            #   if roster[id]['name']:
            #        self.roster_names[roster[id]['name']] = id
             #       self.ui.lstRoster.addItem(str(roster[id]['name']))
              #  else:
               #     self.ui.lstRoster.addItem(str(id))
        self.roster_timer.start(6800)

    def close_chat(self, chat):
        del self.chats[str(chat)]
