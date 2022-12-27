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
        num = 0
        for i in accounts:
            i['game_config']['mapId'] = {'code': self.controller.getMapCode(i['game_config']['mapId']),
                                         'name': self.controller.getMapName(i['game_config']['mapId'])}
            num += 1
            self.gamewindow.addFrame((35 + ((num + 2) % 3) * 400, (((num + 2) // 3) - 1) * 270))
            self.gamewindow.addCard(i, (35 + ((num + 2) % 3) * 400, (((num + 2) // 3) - 1) * 270))

    def refreshGames(self):
        self.gamewindow.scrollArea.setWidget(self.gamewindow.scrollAreaWidgetContents)

    def openDetail(self):
        detail = DetailWindow.MainWindow()
        detail.show()
        self.detailwindows.append(detail)
