import json

items = {}
stage = {}
chars = {}


def init(path):
    global items, stage, chars
    with open(path + '\\Items.json', 'r', encoding='utf-8') as fp:
        items = json.load(fp)
    with open(path + '\\Stage.json', 'r', encoding='utf-8') as fp:
        stage = json.load(fp)
    with open(path + '\\Chars.json', 'r', encoding='utf-8') as fp:
        chars = json.load(fp)


def getMapCode(id):
    if id:
        try:
            return stage[id]['code']
        except Exception:
            return '？'
    else:
        return ''


def getMapName(id):
    if id:
        try:
            return stage[id]['name']
        except Exception:
            return '未知关卡'
    else:
        return ''
