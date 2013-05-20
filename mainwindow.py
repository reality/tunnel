#!/usr/bin/env python
"""
TODO: Document me
"""

__date__ = "$07-Apr-2010 18:36:49$"

import sys
import os
import os.path
import fnmatch
from PyQt4 import QtCore, QtGui

import game
from game import Game
from addgamewindow import AddGameWindow

sys.path.insert(0, 'ui')
from dlgmain import Ui_dlgMain
del sys.path[0]

class MainWindow(QtGui.QDialog):
    """Game launcher dialog and associated methods"""

    def __init__(self, parent, win_parent=None):
        """Initialise the launcher"""
        QtGui.QDialog.__init__(self, win_parent)

        self.parent = parent
        self.ui = Ui_dlgMain()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.btnNext, \
        QtCore.SIGNAL("clicked()"), self.__click_btn_next)
        QtCore.QObject.connect(self.ui.btnPrev, \
        QtCore.SIGNAL("clicked()"), self.__click_btn_prev)
        QtCore.QObject.connect(self.ui.btnLaunch, \
        QtCore.SIGNAL("clicked()"), self.__click_btn_launch)
        QtCore.QObject.connect(self.ui.btnAddGame, \
        QtCore.SIGNAL("clicked()"), self.__click_btn_add_game)
 
        self.game_pointer = 0
        self.games = ["Home"]
        self.__refresh_games()

    def __refresh_games(self):
        """Refresh the list of games from the object files"""
        self.games = ["Home"]

        path = "../../../object_files"
        for f in os.listdir(path):
            if fnmatch.fnmatch(f, '*.gme'):
                game_path = path + os.sep + f
                self.games.append(game.load(game_path))

    def __update_game_info(self):
        """Update the UI according to current game_pointer"""
        if self.game_pointer == 0:
            self.ui.lblTitle.setText("Home")
            self.ui.lblInfo.setText("Welcome to Tunnel, scroll through " + \
            "your games with the arrow buttons")
            self.ui.lblPlayTime.setText("")
            self.ui.btnLaunch.setEnabled(False)
        else:
            self.ui.lblTitle.setText(self.games[self.game_pointer].name)
            self.ui.lblInfo.setText(self.games[self.game_pointer].description)
            self.ui.lblPlayTime.setText("Play time: " + \
            str(self.games[self.game_pointer].total_play_time))
            self.ui.btnLaunch.setEnabled(True)

    def __change_game(self, game_number):
        self.game_pointer = game_number
        self.__update_game_info()

    def __click_btn_next(self):
        """Show info for the next game"""
        if self.game_pointer == (len(self.games) - 1):
            pass
        else:
            self.game_pointer += 1

        self.__update_game_info()

    def __click_btn_prev(self):
        """Show info for the previous game"""
        if self.game_pointer == 0:
            pass
        else:
            self.game_pointer -= 1
 
        self.__update_game_info()

    def __click_btn_launch(self):
        """Launch current game"""
        self.games[self.game_pointer].launch()
        self.ui.lblPlayTime.setText("Play time: " + \
        str(self.games[self.game_pointer].total_play_time))
        game.save(self.games[self.game_pointer])

    def __click_btn_add_game(self):
        """Open add game dialog"""
        addgame = AddGameWindow(self.parent)
        addgame.exec_()
        self.__refresh_games()
        self.__change_game((len(self.games) - 1))

    def closeEvent(self, e):
        sys.exit()


