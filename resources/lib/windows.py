from PyQt5.QtWidgets import QMessageBox

from resources.lib import event
from resources.ui import LoginWindow, GameWindow, DetailWindow


class WindowController():
    def __init__(self, controller):
        self.controller = controller
        self.loginwindow = LoginWindow.MainWindow()
        self.loginwindow.show()
        self.gamewindow = GameWindow.MainWindow()
        self.detailwindows = []

    def loginOK(self):
        self.loginwindow.loginOK()
        self.addGames()
        self.gamewindow.addAnnouncement(event.getAnnouncement())
        self.loginwindow.hide()
        self.gamewindow.show()

    def loginFailed(self):
        self.loginwindow.loginFailed()

    def addGames(self):
        accounts = self.controller.getGames()
        if accounts:
            num = 0
            for i in accounts:
                i['game_config']['mapId'] = {'code': self.controller.getMapCode(i['game_config']['mapId']),
                                             'name': self.controller.getMapName(i['game_config']['mapId'])}
                self.gamewindow.addFrame()
                self.gamewindow.addCard(i, num)
                num += 1
        else:
            QMessageBox.warning(self, 'Warning!', '请输入正确的邮箱和密码', QMessageBox.Ok)
            self.loginwindow = LoginWindow.MainWindow()
            self.loginwindow.show()

    def refreshGames(self, accounts):
        num = 0
        for i in accounts:
            i['game_config']['mapId'] = {'code': self.controller.getMapCode(i['game_config']['mapId']),
                                         'name': self.controller.getMapName(i['game_config']['mapId'])}
        for i in self.gamewindow.gamecards:
            i.refresh(accounts[num])
            num += 1

    def openDetail(self):
        detail = DetailWindow.MainWindow()
        detail.show()
        self.detailwindows.append(detail)

    def gameCardFlex(self, width):
        col = width // 380
        space = (width - col * 400) / col / 2
        maxheight = 0
        num = 0
        for i in self.gamewindow.gameframes:
            num += 1
            frameheight = (((num + col - 1) // col) - 1) * 275
            i.move(int(((num + col - 1) % col) * (400 + 2 * space) + space) + 15, (((num + col - 1) // col) - 1) * 275)
            if frameheight + 260 > maxheight:
                maxheight = frameheight + 260
        num = 0
        for i in self.gamewindow.gamecards:
            num += 1
            i.parent().move(int(((num + col - 1) % col) * (400 + 2 * space) + space) + 30,
                            (((num + col - 1) // col) - 1) * 275 + 5)
        self.gamewindow.scrollAreaWidgetContents.setGeometry(0, 0, width, maxheight)
