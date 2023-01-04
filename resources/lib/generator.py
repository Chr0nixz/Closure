import json


char = {}
with open('../json/gamedata/character_table.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)
    for i in data:
        char[i] = {'name': data[i]['name']}
with open('../json/Chars.json', 'w', encoding='utf-8') as fp:
    json.dump(char, fp, indent=4, ensure_ascii=False)
