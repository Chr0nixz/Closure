import os
import io
import json
from typing import Tuple, Any

import requests
import time

from PIL import Image
from PyQt5.QtCore import QThread, pyqtSignal

from resources.ui import CheckUpdateWindow


def check_version(path) -> int:
    version_path = os.path.join(path, 'resources', 'json', 'version.txt')
    if os.path.isfile(version_path):
        current_version = requests.get(
            'https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/data_version.txt').text
        with open(version_path, 'r', encoding='utf-8') as fp:
            if fp.read() == current_version:
                print('1')
                return True
            else:
                return False
    else:
        current_version = requests.get(
            'https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/data_version.txt').text
        with open(version_path, 'w', encoding='utf-8') as fp:
            fp.write(current_version)
        return False


def get_jsons(path) -> tuple[Any, Any]:
    items = json.loads(requests.get('https://arknights.host/data/Items.json').text)
    stage = json.loads(requests.get('https://arknights.host/data/Stage.json').text)
    with open(os.path.join(path, 'json', 'Items.json'), 'w', encoding='utf-8') as fp:
        json.dump(items, fp, ensure_ascii=False, indent=4)
    with open(os.path.join(path, 'json', 'Stage.json'), 'w', encoding='utf-8') as fp:
        json.dump(stage, fp, ensure_ascii=False, indent=4)
    return items, stage


def get_item(img_path, img_name) -> str:
    url = 'https://ak.dzp.me/dst/items/' + img_name + '.webp'
    content = requests.get(url).content
    try:
        image = Image.open(io.BytesIO(content))
        image.save(img_path)
    except Exception:
        print(img_name)


def get_char(img_path, img_name) -> None:
    url = 'https://ak.dzp.me/dst/avatar/ASSISTANT/' + img_name + '.webp'
    content = requests.get(url).content
    if not '<html>' in content:
        image = Image.open(io.BytesIO(content))
        image.save(img_path)


def update(path):
    items, stage = get_jsons(path)
    print()
    for i in items:
        img_path = os.path.join(path, 'items', items[i]['icon'] + '.png')
        if not os.path.isfile(img_path):
            get_item(img_path, items[i]['icon'])
            print(img_path)
    for i in items:
        img_path = os.path.join(path, 'items', stage[i]['icon'] + '.png')
        if not os.path.isfile(img_path):
            get_item(img_path, stage[i]['icon'])


class Update():

    def __init__(self, path, window):
        self.path = path
        self.windows = window
        self.check_window = CheckUpdateWindow.MainWindow(self.windows.icon)

    def start(self):
        self.check_window.show()
        self.checkUpdateThread = CheckUpdateThread(self.path, self.isUpdated)
        self.checkUpdateThread.start()

    def isUpdated(self, updated):
        if updated:
            self.check_window.updated()
            self.windows.start()
            self.check_window.hide()


class CheckUpdateThread(QThread):
    update_signal = pyqtSignal(bool)

    def __init__(self, path, call):
        super().__init__()
        self.path = path
        self.update_signal.connect(call)

    def run(self) -> None:
        res = check_version(self.path)
        self.update_signal.emit(res)


class UpdateThread(QThread):
    update_signal = pyqtSignal(str)
    finish_signal = pyqtSignal(bool)

    def __init__(self, path, call):
        super().__init__()
        self.path = path
        self.call = call


class DownloadThread(QThread):
    def __init__(self):
        super().__init__()
    
    
