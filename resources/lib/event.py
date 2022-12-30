from PyQt5.QtCore import Qt, QThread, pyqtSignal

eventhandler = None
windows = None
configs = None


def addHandler(handler):
    global eventhandler
    eventhandler = handler


def addWindows(app):
    global windows
    windows = app


def addConfig(config):
    global configs
    configs = config


class LoginThread(QThread):
    loginsignal = pyqtSignal(bool)
    def __init__(self, email, password):
        super().__init__()
        self.email = email
        self.password = password
        self.loginsignal.connect(loginResult)

    def run(self) -> None:
        self.loginsignal.emit(eventhandler.login(self.email, self.password))
        self.quit()


def login(email, password):
    th = LoginThread(email, password)
    th.start()
    th.exec()


def loginResult(result):
    if result:
        windows.loginwindow.statusbar.showMessage('登陆成功，正在跳转...')
        getGames()
    else:
        windows.loginFailed()


class getGamesThread(QThread):
    getgamessignal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.getgamessignal.connect(loginOK)

    def run(self) -> None:
        self.getgamessignal.emit(eventhandler.getGames())


def getGames():
    th = getGamesThread()
    th.start()
    th.exec()


def loginOK(accounts):
    windows.loginOK(accounts)


def configAccount(email, password):
    configs.addAccount(email, password)


def getDefaultAccount():
    return configs.config.get('account')



def getAnnouncement():
    return eventhandler.getAnnouncement()


def refreshGames():
    windows.refreshGames(eventhandler.getGames())


def getDetail(account, platform):
    windows.openDetail()


def gameCardFlex(width):
    windows.gameCardFlex(width)


class gameLoginThread(QThread):
    gameloginsignal = pyqtSignal(bool)
    def __init__(self, account, platform):
        super().__init__()
        self.account = account
        self.platform = platform
        self.gameloginsignal.connect(gameLoginResult)

    def run(self) -> None:
        self.gameloginsignal.emit(eventhandler.gameLogin(self.account, self.platform))


def gameLogin(account, platform):
    th = gameLoginThread()
    th.start()
    th.exec()

def gameLoginResult(result):
    pass
