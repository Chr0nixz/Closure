from resources.lib import threads

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


def login(email, password):
    th = threads.LoginThread(email, password)
    th.start()
    th.exec()


def loginResult(result):
    match result:
        case -1:
            windows.serverMaintain()
        case 0:
            windows.loginFailed()
        case 1:
            windows.loginwindow.statusbar.showMessage('登陆成功，正在跳转...')
            getGames()


def getGames():
    th = threads.getGamesThread()
    th.start()
    th.exec()


def loginOK(accounts):
    windows.loginOK(accounts)


def configAccount(email, password):
    configs.addAccount(email, password)


def getDefaultAccount():
    return configs.config.get('account')


def getAnnouncement():
    return eventhandler.announcement


def refreshGames():
    windows.refreshGames(eventhandler.getGames())


def getDetail(account, platform):
    th = threads.getDetailThread(account, platform)
    th.start()
    th.exec()


def addDetail(data):
    windows.openDetail(data)


def gameCardFlex(width):
    windows.gameCardFlex(width)


def gameLogin(account, platform):
    th = threads.gameLoginThread()
    th.start()
    th.exec()


def gameLoginResult(result):
    pass
