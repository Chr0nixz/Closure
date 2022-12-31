import json
import os
import sys

from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet

from resources.lib.arknights import MainController
from resources.lib.windows import WindowController
from resources.lib import event, config

if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('./resources/style/extra.json', encoding='utf-8') as file:
        extra = json.load(file)
    apply_stylesheet(app, theme='dark_amber.xml', extra=extra)
    stylesheet = app.styleSheet()
    with open("resources/style/login.qss", encoding='utf-8') as file:
        app.setStyleSheet(stylesheet + file.read().format(**os.environ))
        print(file.read().format(**os.environ))
    controller = MainController()
    configs = config.Config(os.path.join(os.getcwd(), 'Config.json'))
    event.addHandler(controller)
    event.addConfig(configs)
    windows = WindowController(controller)
    event.addWindows(windows)
    sys.exit(app.exec_())
