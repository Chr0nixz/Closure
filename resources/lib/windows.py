from ..ui import LoginWindow, GameWindow, GameCard
from . import event


class WindowController():
    def __init__(self, controller):
        self.controller = controller
        self.loginwindow = LoginWindow.MainWindow()
        self.loginwindow.show()
        self.gamewindow = GameWindow.MainWindow()
        self.gamecards = []

    def loginOK(self):
        self.loginwindow.hide()
        self.addGames()
        self.gamewindow.addAnnouncement(event.getAnnouncement())
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
            self.gamewindow.addFrame((-360 + (num % 3) * 400, (num // 3) * 270))
            self.gamewindow.addCard(i, (-360 + (num % 3) * 400, (num // 3) * 270))

