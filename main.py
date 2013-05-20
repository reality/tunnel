#!/usr/bin/env python
"""
TODO: Document me
"""

__date__ = "$16-Mar-2010 16:35:49$"

import sys
from PyQt4 import QtCore, QtGui

from tunnelchat import TunnelChat
from chatrosterwindow import ChatRosterWindow

from loginwindow import LoginWindow

class TunnelClient(object):
    """Holder object for the application"""

    def __init__(self):
        """Initialise objects"""
        self.connected = False
 
        self.app = QtGui.QApplication(sys.argv)

        self.chat = ChatRosterWindow(self)

        self.login()
    
        self.chat.show()
        sys.exit(self.app.exec_())
 
    def login(self):
        """Run login dialog and get the api_conn set up"""
        login = LoginWindow(self)
        login.exec_()
        self.connected = True

    def set_login_details(self, username, password, server):
        self.username = username
        self.password = password
        self.server = server

        return self.start_connection()

    def start_connection(self):
        # Initialise the XMPP connection
        try:
            self.xmpp = TunnelChat(str(self.username) + "/tunnel",
                    str(self.password), self.chat)
            self.xmpp.connect((str(self.server), 5222))
            self.xmpp.process(threaded=True)
        except:
            return False
        else:
            return True



TunnelClient()
