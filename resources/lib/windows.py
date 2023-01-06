import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from resources.lib import event, gamedata
from resources.ui import LoginWindow, GameWindow, DetailWindow


class WindowController():
    def __init__(self, controller, path):
        self.controller = controller
        self.path = path
        self.loginwindow = LoginWindow.MainWindow()
        self.icon = QIcon(os.path.join(self.path, 'resources', 'img', 'icon.png'))
        self.loginwindow.setWindowIcon(self.icon)
        self.loginwindow.show()
        self.detailwindows = {}
        self.accountconfigs = {}

    def loginOK(self, accounts):
        self.gamewindow = GameWindow.MainWindow()
        self.gamewindow.setWindowIcon(self.icon)
        self.addGames(accounts)
        self.gamewindow.addAnnouncement(event.getAnnouncement())
        self.loginwindow.hide()
        self.gamewindow.show()

    def loginFailed(self):
        self.loginwindow.loginFailed()

    def serverMaintain(self):
        QMessageBox.warning(self.loginwindow, '维护中!', '服务器正在维护中，请等待维护结束！', QMessageBox.Ok)
        self.loginwindow.loginFailed()

    def addGames(self, accounts):
        if accounts:
            num = 0
            for i in accounts:
                i['game_config']['mapId'] = {'code': gamedata.getMapCode(i['game_config']['mapId']),
                                             'name': gamedata.getMapName(i['game_config']['mapId'])}
                self.gamewindow.addFrame()
                self.gamewindow.addCard(i, num)
                num += 1

    def refreshGames(self, accounts):
        num = 0
        for i in accounts:
            i['game_config']['mapId'] = {'code': gamedata.getMapCode(i['game_config']['mapId']),
                                         'name': gamedata.getMapName(i['game_config']['mapId'])}
        for i in self.gamewindow.gamecards:
            i.refresh(accounts[num])
            num += 1

    def openDetail(self, data):
        if data['account'] in self.detailwindows:
            self.detailwindows[data['account']].deleteLater()
        detail = DetailWindow.MainWindow(data)
        detail.setWindowIcon(self.icon)
        detail.show()
        self.detailwindows[data['account']] = detail

    def detailMessage(self, account, title, text):
        message = QMessageBox.information(self.detailwindows[account], title, text, QMessageBox.Ok)
