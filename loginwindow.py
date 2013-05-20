#!/usr/bin/env python
"""
TODO: Document me
"""

__date__ = "$07-Apr-2010 18:36:49$"

import sys
from PyQt4 import QtCore, QtGui

sys.path.insert(0, 'ui')
from dlglogin import Ui_dlgLogin
del sys.path[0]

class LoginWindow(QtGui.QDialog):
    """Dialog for login window"""

    def __init__(self, parent, win_parent=None):
        """Initialise dialog"""
        QtGui.QDialog.__init__(self, win_parent)
        self.parent = parent
        self.ui = Ui_dlgLogin()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.btnLogin, QtCore.SIGNAL("clicked()"), \
        self.__click_btn_login)

        self.authenticated = False

    def __click_btn_login(self):
        """Put authentication code here
               TODO: Make a check login
        """
        login_test = self.parent.set_login_details(self.ui.edtUser.text(), \
        self.ui.edtPass.text(), self.ui.edtServ.text())

        if login_test == True:
            self.authenticated = True
            self.close()
        else:
            self.QMessageBox.error("Information", "A plain, informational message")

    def closeEvent(self, e):
        """Close application instead of window if not authenticated"""
        if self.authenticated == False:
            sys.exit()

