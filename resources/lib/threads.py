from PyQt5.QtCore import QThread, pyqtSignal

from resources.lib import event


class getGamesThread(QThread):
    getgamessignal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.getgamessignal.connect(event.loginOK)

    def run(self) -> None:
        self.getgamessignal.emit(event.eventhandler.getGames())
        event.ths.remove(self)
        self.quit()


class refreshGamesThread(QThread):
    refreshsignal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.refreshsignal.connect(event.refreshResult)

    def run(self) -> None:
        self.refreshsignal.emit(event.eventhandler.getGames())
        event.ths.remove(self)
        self.quit()


class gameLoginThread(QThread):
    gameloginsignal = pyqtSignal(bool)

    def __init__(self, account, platform):
        super().__init__()
        self.account = account
        self.platform = platform
        self.gameloginsignal.connect(event.gameLoginResult)

    def run(self) -> None:
        self.gameloginsignal.emit(event.eventhandler.gameLogin(self.account, self.platform))
        event.ths.remove(self)
        self.quit()


class gamePauseThread(QThread):
    gamepausesignal = pyqtSignal(bool)

    def __init__(self, account, platform):
        super().__init__()
        self.account = account
        self.platform = platform
        self.gamepausesignal.connect(event.gamePauseResult)

    def run(self) -> None:
        self.gamepausesignal.emit(event.eventhandler.gamePause(self.account, self.platform))
        event.ths.remove(self)
        self.quit()


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
        event.ths.remove(self)
        self.quit()


class postConfigThread(QThread):
    postsignal = pyqtSignal(list)

    def __init__(self, account, platform, config):
        super().__init__()
        self.account = account
        self.platform = platform
        self.config = config
        self.postsignal.connect(event.postConfigResult)

    def run(self) -> None:
        self.postsignal.emit(event.eventhandler.postConfig(self.account, self.platform, self.config))
        event.ths.remove(self)
        self.quit()


class pullScreenshotsThread(QThread):
    pullsignal = pyqtSignal(dict)

    def __init__(self, sender, account, platform):
        super().__init__()
        self.sender = sender
        self.account = account
        self.platform = platform
        self.pullsignal.connect(event.showScreenshots)

    def run(self) -> None:
        result = event.eventhandler.getScreenshots(self.account, self.platform)
        res = {'sender': self.sender, 'data': result}
        self.pullsignal.emit(res)
        print(event.ths)
        event.ths.remove(self)
        self.quit()
        print('ok')


class ProcessThread(QThread):
    processSignal = pyqtSignal(list)

    def __init__(self, method, args, handler):
        super().__init__()
        self.method = method
        self.args = args
        self.handler = handler
        self.processSignal.connect(self.handler)

    def run(self) -> None:
        if self.args:
            self.processSignal.emit(self.method(self.args))
        else:
            self.processSignal.emit(self.method())
        event.ths.remove(self)
        self.quit()

