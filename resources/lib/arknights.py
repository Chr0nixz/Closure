import json
import os

import requests

from . import event, router

url = "https://api.arknights.host/"
respath = './resources/json/'


class MainController():
    def __init__(self):
        self.token = None
        self.items, self.stage = self.readJsons(respath)

    def readJsons(self, path) -> (dict, dict):
        with open(respath + 'Items.json', 'r', encoding='utf-8') as fp:
            items = json.load(fp)
        with open(respath + 'Stage.json', 'r', encoding='utf-8') as fp:
            stage = json.load(fp)
        return items, stage

    def login(self, email, password) -> bool:
        data = router.get(url=url + 'Auth/' + email + '/' + password)
        if data:
            self.token = data['token']
            self.auth = {{'Authorization': self.token}}
            event.configAccount(email, password)
            return True
        else:
            return False

    def getGames(self) -> list:
        data = router.get(url=url + 'Game/', auth=self.auth)
        return data

    def getMapCode(self, id):
        if id == '':
            return ''
        else:
            return self.stage[id]['code']

    def getMapName(self, id):
        if id == '':
            return ''
        else:
            return self.stage[id]['name']

    def getAnnouncement(self):
        data = router.get(url=url + 'System/Announcement', auth=self.auth)
        return data

    def getDetail(self, account, platform):
        data = router.get(url=url + 'Game/' + account + '/' + platform, auth=self.auth)
        return data
        headers = {'Authorization': self.token}
        if data:
            return True
        else:
            return False

    def gameLogin(self, account, platform):
        body = {'account': account, 'platform': platform}
        data = router.get(url=url + 'Game/Login/', body=body)

