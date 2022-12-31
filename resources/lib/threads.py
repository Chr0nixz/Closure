# TODO: 多线程分离
from PyQt5.QtCore import QThread, pyqtSignal

from resources.lib import event


class LoginThread(QThread):
    loginsignal = pyqtSignal(bool)

    def __init__(self, email, password):
        super().__init__()
        self.email = email
        self.password = password
        self.loginsignal.connect(event.loginResult)

    def run(self) -> None:
        self.loginsignal.emit(event.eventhandler.login(self.email, self.password))
        self.quit()


class getGamesThread(QThread):
    getgamessignal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.getgamessignal.connect(event.loginOK)

    def run(self) -> None:
        self.getgamessignal.emit(event.eventhandler.getGames())


class refreshGamesThread(QThread):
    def __init__(self):
        super().__init__()


class gameLoginThread(QThread):
    gameloginsignal = pyqtSignal(bool)

    def __init__(self, account, platform):
        super().__init__()
        self.account = account
        self.platform = platform
        self.gameloginsignal.connect(event.gameLoginResult)

    def run(self) -> None:
        self.gameloginsignal.emit(event.eventhandler.gameLogin(self.account, self.platform))

