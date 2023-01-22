import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from resources.lib import event, gamedata
from resources.ui import LoginWindow, GameWindow, DetailWindow, CheckUpdateWindow


class WindowController():
    def __init__(self, controller, path):
        self.controller = controller
        self.path = path
        self.detailwindows = {}
        self.accountconfigs = {}
        self.icon = QIcon(os.path.join(self.path, 'resources', 'img', 'icon.png'))

    def start(self):
        self.loginwindow = LoginWindow.MainWindow()
        self.loginwindow.setWindowIcon(self.icon)
        self.loginwindow.show()

    def loginOK(self, accounts):
        self.gamewindow = GameWindow.MainWindow()
        self.gamewindow.setWindowIcon(self.icon)
        self.gamewindow.addGames(accounts)
        self.gamewindow.addAnnouncement(event.getAnnouncement())
        self.loginwindow.hide()
        self.gamewindow.show()

    def openDetail(self, data):
        if data['account'] in self.detailwindows:
            self.detailwindows[data['account']].deleteLater()
        detail = DetailWindow.MainWindow(data)
        detail.setWindowIcon(self.icon)
        detail.show()
        self.detailwindows[data['account']] = detail
