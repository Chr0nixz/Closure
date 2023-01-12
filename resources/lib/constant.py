# TODO:路径管理
import os


items_path = ''
chars_path = ''
def init(path):
    global items_path, chars_path
    items_path = os.path.join(path, 'resources', 'items') + '\\'
    chars_path = os.path.join(path, 'resources', 'chars') + '\\'
    print(items_path, chars_path)
