import json
import os

import requests

from . import event

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
        try:
            res = requests.get(url + 'Auth/' + email + '/' + password)
            if res.status_code == 200:
                data = json.loads(res.text)
            if data['code'] == 1:
                token = data['data']['token']
                print(data['message'])
                self.token = token
                event.configAccount(email, password)
                return True
            else:
                return False
        except Exception:
            event.loginTimeout()
            return False


    def getGames(self) -> list:
        try:
            headers = {'Authorization': self.token}
            res = requests.get(url=url + 'Game/', headers=headers)
            if res.status_code == 200:
                data = json.loads(res.text)
                print(data['message'])
                return data['data']
        except Exception:
            return None

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
        headers = {'Authorization': self.token}
        res = requests.get(url + 'System/Announcement', headers=headers)
        if res.status_code == 200:
            data = json.loads(res.text)
            if data['code'] == 1:
                return data['data']

    def getDetail(self, account, platform):
        headers = {'Authorization': self.token}
        try:
            res = requests.get(url + 'Game/' + account + '/' + platform, headers=headers)
            if res.status_code == 200:
                data = json.loads(res.text)
                if data['code'] == 1:
                    return data['data']
        except Exception:
            pass

    def gameLogin(self, account, platform):
        body = {'account': account, 'platform': platform}
        try:
            res = requests.get(url + 'Game/Login/', data=json.dumps(body))
            if res.status_code == 200:
                data = json.loads(res.text)
                if data['code'] == 1:
                    print()
                    return True
                else:
                    return False
        except Exception:
            pass

