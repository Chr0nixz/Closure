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
    th = threads.refreshGamesThread()
    th.start()
    th.exec()


def refreshResult(data):
    if not data == []:
        windows.refreshGames(data)


def getDetail(account, platform):
    th = threads.getDetailThread(account, platform)
    th.start()
    th.exec()


def addDetail(data):
    windows.openDetail(data)


def gameCardFlex(width):
    windows.gameCardFlex(width)


def gameLogin(account, platform):
    th = threads.gameLoginThread(account, platform)
    th.start()
    th.exec()


def gameLoginResult(result):
    if result:
        windows.gamewindow.statusbar.showMessage('提交登录请求成功！')
        refreshGames()


def gamePause(account, platform):
    th = threads.gamePauseThread(account, platform)
    th.start()
    th.exec()


def gamePauseResult(result):
    if result:
        windows.gamewindow.statusbar.showMessage('提交暂停请求成功！')
        refreshGames()
