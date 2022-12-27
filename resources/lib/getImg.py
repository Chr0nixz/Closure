import os
import json
import requests
from PIL import Image, ImageOps

def getItems():
    with open("../json/Items.json", 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    for i in data:
        j = data[i]['icon']
        path = os.path.abspath(os.path.join(os.getcwd(), "../")) + '\\items\\' + j + '.webp'
        if not os.path.isfile(path):
            res = requests.get('https://ak.dzp.me/dst/items/'+j+'.webp')
            if res.status_code == 200:
                open(path, 'wb').write(res.content)
                webp2png(path)


def webp2png(path):
    image = Image.open(path)
    image = ImageOps.exif_transpose(image)
    dstimage = os.path.splitext(path)[0] + '.png'
    image.save(dstimage)
    print('%s ---> %s' %(path, dstimage))


getItems()