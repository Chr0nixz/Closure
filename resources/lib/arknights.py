from . import event, router

url = "https://api.arknights.host/"
respath = './resources/json/'


class MainController():
    def __init__(self):
        self.token = None
        self.lastgames = None
        self.cache = None

    def setCache(self, cache):
        self.cache = cache

    def getStatus(self) -> bool:
        data = router.getJson('https://ak.dzp.me/ann.json')
        if not data['isMaintain']:
            self.announcement = data['announcement']
            return True
        else:
            return False

    def login(self, args: list) -> list:
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

        data = router.get(url=url + 'Game/', auth=self.token)
        if data == self.lastgames:
            return []
        else:
            self.lastgames = data
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
