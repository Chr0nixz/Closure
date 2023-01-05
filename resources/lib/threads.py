# TODO: 多线程分离
from PyQt5.QtCore import QThread, pyqtSignal

from resources.lib import event


class LoginThread(QThread):
    loginsignal = pyqtSignal(int)

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
    refreshsignal = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.refreshsignal.connect(event.refreshResult)

    def run(self) -> None:
        self.refreshsignal.emit(event.eventhandler.getGames())


class gameLoginThread(QThread):
    gameloginsignal = pyqtSignal(bool)

    def __init__(self, account, platform):
        super().__init__()
        self.account = account
        self.platform = platform
        self.gameloginsignal.connect(event.gameLoginResult)

    def run(self) -> None:
        self.gameloginsignal.emit(event.eventhandler.gameLogin(self.account, self.platform))


class gamePauseThread(QThread):
    gamepausesignal = pyqtSignal(bool)

    def __init__(self, account, platform):
        super().__init__()
        self.account = account
        self.platform = platform
        self.gamepausesignal.connect(event.gamePauseResult)

    def run(self) -> None:
        self.gamepausesignal.emit(event.eventhandler.gamePause(self.account, self.platform))


class getDetailThread(QThread):
    detailsignal = pyqtSignal(dict)
    def __init__(self, account, platform):
        super().__init__()
        self.account = account
        self.platform = platform
        self.detailsignal.connect(event.addDetail)

    def run(self) -> None:
        data = event.eventhandler.getDetail(self.account, self.platform)
        config = event.eventhandler.getConfig(self.account, self.platform)
        data['account'] = self.account
        data['platform'] = self.platform
        data['config'] = config
        self.detailsignal.emit(data)
