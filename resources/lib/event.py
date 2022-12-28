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


def login(email, password):
    th = LoginThread(email, password)
    th.start()
    th.exec()


def loginResult(result):
    if result:
        windows.loginOK()
    else:
        windows.loginFailed()


def configAccount(email, password):
    configs.addAccount(email, password)


def getDefaultAccount():
    return configs.config.get('account')


def getAnnouncement():
    return eventhandler.getAnnouncement()


def refreshGames():
    windows.refreshGames(eventhandler.getGames())



def getDetail():
    windows.openDetail()


def gameCardFlex(width):
    windows.gameCardFlex(width)
