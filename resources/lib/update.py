import io
import json
import os

import requests
from PIL import Image
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from resources.ui import CheckUpdateWindow, UpdatingWindow, NewUpdateWindow


def check_version(path) -> list:
    version_path = os.path.join(path, 'json', 'version.txt')
    try:
        current_version = requests.get(
            'https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/data_version.txt').text
    except requests.exceptions.ConnectionError:
        return [False, '访问 raw.githubusercontent.com 失败！']
    if os.path.isfile(version_path):
        with open(version_path, 'r', encoding='utf-8') as fp:
            if fp.read() == current_version:
                print('1')
                return [True, current_version]
            else:
                return [True, False]
    else:
        return [True, current_version]

def get_jsons(path):
    try:
        items = json.loads(requests.get('https://arknights.host/data/Items.json').text)
        stage = json.loads(requests.get('https://arknights.host/data/Stage.json').text)
    except requests.exceptions.ConnectionError:
        return False
    with open(os.path.join(path, 'json', 'Items.json'), 'w', encoding='utf-8') as fp:
        json.dump(items, fp, ensure_ascii=False, indent=4)
    with open(os.path.join(path, 'json', 'Stage.json'), 'w', encoding='utf-8') as fp:
        json.dump(stage, fp, ensure_ascii=False, indent=4)
    return items, stage


def get_item(img_path, img_name) -> str:
    url = 'https://ak.dzp.me/dst/items/' + img_name + '.webp'
    try:
        content = requests.get(url).content
        image = Image.open(io.BytesIO(content))
        image.save(img_path)
    except requests.exceptions.ConnectionError:
        return False
    except Exception:
        return False


def get_char(img_path, img_name) -> None:
    url = 'https://ak.dzp.me/dst/avatar/ASSISTANT/' + img_name + '.webp'
    content = requests.get(url).content
    try:
        image = Image.open(io.BytesIO(content))
        image.save(img_path)
    except Exception:
        print(img_name)


class Update():

    def __init__(self, path, window):
        self.path = os.path.join(path, 'resources')
        self.windows = window
        self.check_window = CheckUpdateWindow.MainWindow(self.windows.icon, self.check_cancel)
        self.threads = []
        self.canceled = False

    def start(self):
        self.check_window.show()
        checkUpdateThread = CheckUpdateThread(self.path, self.isUpdated)
        checkUpdateThread.start()
        self.threads.append(checkUpdateThread)

    def isUpdated(self, updated):
        if not self.canceled:
            if updated[0]:
                if not updated[1]:
                    self.check_window.updated()
                    self.finish()
                else:
                    self.version = updated[1]
                    self.check_window = NewUpdateWindow.MainWindow(self.windows.icon, self.update, self.finish)
                    self.check_window.addText(self.version)
                    self.check_window.show()
            else:
                self.exception(updated[1])


    def update(self):
        self.check_window = UpdatingWindow.MainWindow()
        self.check_window.show()
        self.updateThread = UpdateThread(self, self.path, None)
        self.updateThread.start()

    def exception(self, text):
        QMessageBox.critical(self.check_window, '错误', text, QMessageBox.Ok)
        self.check_window = None
        self.windows.start()

    def update_status(self, update):
        self.check_window.label_2.setText(update)

    def finish(self):
        with open(os.path.join(self.path, 'version.txt'), 'w', encoding='utf-8') as fp:
            fp.write(self.version)
        self.windows.start()
        self.check_window.hide()
        self.check_window = None
        del self

    def cancel(self):
        self.canceled = True
        for i in self.threads:
            i.quit()
        self.threads = None
        self.windows.start()
        self.check_window = None
        del self

    def check_cancel(self):
        self.check_window.hide()
        self.cancel()


class CheckUpdateThread(QThread):
    update_signal = pyqtSignal(list)

    def __init__(self, path, call):
        super().__init__()
        self.path = path
        self.update_signal.connect(call)

    def run(self) -> None:
        res = check_version(self.path)
        self.update_signal.emit(res)


class UpdateThread(QThread):
    update_signal = pyqtSignal(str)
    value_signal = pyqtSignal(int)
    finish_signal = pyqtSignal(bool)
    exception_signal = pyqtSignal(str)

    def __init__(self, parent, path, call):
        super().__init__()
        self.parent = parent
        self.path = path
        self.call = call
        self.update_signal.connect(self.parent.update_status)
        self.exception_signal.connect(self.parent.exception)

    def run(self) -> None:
        if n := get_jsons(self.path):
            items, stage = n
        else:
            self.exception_signal.emit('获取游戏数据文件时失败！\n请检查网络连接！')
            return
        items_queue = []
        self.workers = []
        if not os.path.isdir(n := os.path.join(self.path, 'items')):
            os.mkdir(n)
        for i in items:
            img_path = os.path.join(self.path, 'items', items[i]['icon'] + '.png')
            if not os.path.isfile(img_path):
                items_queue.append((img_path, items[i]['icon']))
        print(items_queue)
        for i in range(0, 20):
            self.workers.append(DownloadThread(0, items_queue, self.update_signal, self.exception_signal))
            for j in self.workers:
                j.start()


class DownloadThread(QThread):
    def __init__(self, type, queue, update_signal, exception_signal):
        super().__init__()
        self.type = type
        self.queue = queue
        self.update_signal = update_signal
        self.exception_signal = exception_signal

    def run(self) -> None:
        while not self.queue == []:
            if self.type == 0:
                item = self.queue.pop()
                if get_item(item[0], item[1]):
                    self.update_signal.emit('下载' + item[1] + '成功')
                else:
                    self.update_signal.emit('下载' + item[1] + '失败')
            else:
                get_char(self.queue.pop())
