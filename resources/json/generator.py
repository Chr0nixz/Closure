import json


char = {}
with open('./gamedata/character_table.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)
    for i in data:
        char[i] = {'name': data[i]['name']}
with open('Chars.json', 'w', encoding='utf-8') as fp:
    json.dump(char, fp, indent=4, ensure_ascii=False)
