from . import event, router

url = "https://api.arknights.host/"
respath = './resources/json/'


class MainController():
    """
    后台主要控制器
    """

    def __init__(self):
        self.token = None
        self.lastGames = None
        self.cache = None

    def setCache(self, cache=None) -> None:
        """
        设置缓存对象
        :param cache: Cache Object
        :return: None
        """
        self.cache = cache

    def getStatus(self) -> bool:
        """
        获取服务器状态
        :return: None
        """
        data = router.getJson('https://ak.dzp.me/ann.json')
        if data:
            if not data['isMaintain']:
                self.announcement = data['announcement']
                return [True, 1]
            else:
                return [True, 0]
        else:
            return [False, '获取服务器状态失败！']

    def login(self, args: list) -> list:
        """
        可露希尔账号登录
        :param args: [email, password]
        :return: [bool, data]
        """
        email = args[0]
        password = args[1]
        if self.getStatus():
            data = router.get(url=url + 'Auth/' + email + '/' + password)
            if data:
                self.token = data['token']
                event.configAccount(email, password)
                return [True]
            else:
                return [False, 1]
        else:
            return [False, 0]

    def getGames(self) -> list:
        """
        获取所有游戏
        :return: [bool, data] or []
        """
        data = router.get(url=url + 'Game/', auth=self.token)
        if data == self.lastGames:
            return []
        else:
            self.lastGames = data
            return data

    def getAnnouncement(self):
        data = router.get(url=url + 'System/Announcement', auth=self.token)
        return data

    def getDetail(self, account, platform):
        data = router.get(url=url + 'Game/' + account + '/' + str(platform), auth=self.token)
        return data

    def gameLogin(self, account, platform):
        body = {'account': account, 'platform': platform}
        data = router.post(url=url + 'Game/Login/', auth=self.token, body=body)
        if data:
            if data['code'] == 1:
                return True
        else:
            return False

    def gamePause(self, account, platform):
        config = self.getConfig(account, platform)
        config['isStopped'] = True
        data = router.post(url=url + 'Game/Config/' + account + '/' + str(platform), auth=self.token, body=config)
        if data:
            if data['code'] == 1:
                return True
        else:
            return False

    def getConfig(self, account, platform):
        data = router.get(url=url + 'Game/Config/' + account + '/' + str(platform), auth=self.token)
        return data

    def postConfig(self, account, platform, config):
        data = router.post(url=url + 'Game/Config/' + account + '/' + str(platform), auth=self.token, body=config)
        if data:
            if data['code'] == 1:
                return [account, True]
        else:
            return [account, False]

    def getScreenshots(self, account, platform):
        data = router.get(url=url + 'Game/Screenshots/' + account + '/' + str(platform), auth=self.token)
        if data:
            screenshots = self.cache.cache_screenshot(account, platform, data[0])
            print(screenshots)
            return screenshots
        else:
            return []

    def getLogs(self, args):
        account = args[0]
        platform = args[1]
        data = router.get(url=url + 'Game/Log/' + account + '/' + str(platform) + '/0', auth=self.token)
        if data:
            return [True, data]
        else:
            return [False]
