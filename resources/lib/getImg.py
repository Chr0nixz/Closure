import os
import json
import requests

with open("../json/Items.json", 'r', encoding='utf-8') as fp:
    data = json.load(fp)
for i in data:
    j = data[i]['icon']
    res = requests.get('https://ak.dzp.me/dst/items/'+j+'.webp')
    if res.status_code == 200:
        open('./resources/items/'+j+'.webp', 'wb').write(res.content)

