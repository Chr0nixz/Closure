from resources.lib import threads

eventhandler = None
windows = None
configs = None
ths = []
methods = {}


def init(handler, window, config):
    global eventhandler, windows, configs, methods
    eventhandler = handler
    windows = window
    configs = config
    methods = {
        'log': eventhandler.getLogs,
        'login': eventhandler.login,
        'get_games': eventhandler.getGames,
        'get_games_handler': windows.loginOK,
        'refresh_games': eventhandler.getGames,
        'game_login': eventhandler.gameLogin,
        'game_pause': eventhandler.gamePause
    }


def addHandler(handler):
    global eventhandler
    eventhandler = handler



def configAccount(email, password):
    configs.addAccount(email, password)


def getDefaultAccount():
    return configs.config.get('account')


def getAnnouncement():
    return eventhandler.announcement


def refreshGames():
    th = threads.refreshGamesThread()
    th.start()
    ths.append(th)


def refreshResult(data):
    if not data == []:
        refreshGames(data)


def getDetail(account, platform):
    th = threads.getDetailThread(account, platform)
    th.start()
    ths.append(th)


def addDetail(data):
    windows.openDetail(data)


def gameLogin(account, platform):
    th = threads.gameLoginThread(account, platform)
    th.start()
    ths.append(th)


def gameLoginResult(result):
    if result:
        windows.gamewindow.statusbar.showMessage('提交登录请求成功！')
        refreshGames()


def gamePause(account, platform):
    th = threads.gamePauseThread(account, platform)
    th.start()
    ths.append(th)


def gamePauseResult(result):
    if result:
        windows.gamewindow.statusbar.showMessage('提交暂停请求成功！')
        refreshGames()


def postConfig(account, platform, config):
    th = threads.postConfigThread(account, platform, config)
    th.start()
    ths.append(th)


def postConfigResult(result):
    if result[1]:
        windows.detailMessage(result[0], 'success!', '提交成功！')


def pullScreenshots(sender, account, platform):
    th = threads.pullScreenshotsThread(sender, account, platform)
    th.start()
    ths.append(th)


def showScreenshots(screenshots):
    if screenshots['data'] == []:
        screenshots['sender'].noScreenshots()
    else:
        screenshots['sender'].addScreenshots(screenshots['data'])


def process(func: str, args=None, handler=None):
    method = methods[func]
    if not handler:
        handler = methods[func + '_handler']
    th = threads.ProcessThread(method, args, handler)
    th.start()
    ths.append(th)

def addConfig(name:str, value):
    pass
