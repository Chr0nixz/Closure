import os
import io
import json
import requests

from PIL import Image

def check_version(path) -> int:
    version_path = os.path.join(path, 'json', 'version.txt')
    if os.path.isfile(version_path):
        current_version = requests.get('https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/data_version.txt').text
        with open(version_path, 'w+', encoding='utf-8') as fp:
            if fp.read() == current_version:
                return 1
            else:
                return 0
    else:
        return -1


def get_item(img_name, path) -> str:
    url = 'https://ak.dzp.me/dst/items/' + img_name + '.webp'
    content = requests.get(url).content
    image = Image.open(io.BytesIO(content))
    img_path = os.path.join(path, 'items', img_name, '.png')
    image.save(img_path)
    return img_name


def get_char(img_name, path) -> None:
    url = 'https://ak.dzp.me/dst/avatar/ASSISTANT/' + img_name + '.webp'
    content = requests.get(url).content
    image = Image.open(io.BytesIO(content))
    img_path = os.path.join(path, 'chars', img_name + '.png')
    image.save(img_path)

def get_jsons(path) -> None:
    items = json.loads(requests.get('https://arknights.host/data/Items.json').text)
    stage = json.loads(requests.get('https://arknights.host/data/Stage.json').text)
    with open(os.path.join(path, 'json', 'Items.json')):
        pass

