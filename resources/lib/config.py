import os
import json


class Config():
    def __init__(self, path):
        self.path = path
        print(path)
        if not os.path.isfile(path):
            with open(self.path, 'w', encoding='utf-8') as file:
                default = {"configs": {"theme": "default"}}
                json.dump(default, file, ensure_ascii=False, indent=4)
        with open(self.path, 'r', encoding='utf-8') as file:
            self.config = json.load(file)

    def addAccount(self, email, password):
        with open(self.path, 'w+', encoding='utf-8') as file:
            self.config["account"] = {"email": email, "password": password}
            json.dump(self.config, file, indent=4)

    def addConfig(self, name:str, value):
        """
        将某项设置加入config.json
        :param name:格式：a.b.c
        :param value: 值
        :return: bool
        """
        name = list(name.split('.'))
        for i in name:
            cur = self.config[i]
        cur = value


