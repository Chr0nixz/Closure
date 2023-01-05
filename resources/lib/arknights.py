from . import event, router

url = "https://api.arknights.host/"
respath = './resources/json/'


class MainController():
    def __init__(self):
        self.token = None
        self.lastgames = None

    def getStatus(self) -> bool:
        data = router.getJson('https://ak.dzp.me/ann.json')
        if not data['isMaintain']:
            self.announcement = data['announcement']
            return True
        else:
            return False

    def login(self, email, password) -> int:
        if self.getStatus():
            data = router.get(url=url + 'Auth/' + email + '/' + password)
            if data:
                self.token = data['token']
                event.configAccount(email, password)
                return 1
            else:
                return 0
        else:
            return -1

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
