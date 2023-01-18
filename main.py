import sys
import time

from ctypes import windll
from os import getcwd, path
from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet

from resources.lib.arknights import MainController
from resources.lib.windows import WindowController
from resources.lib import event, config, gamedata, cache, constant, update
from resources.style import style

if __name__ == '__main__':
    start = time.process_time()
    windll.shell32.SetCurrentProcessExplicitAppUserModelID("Chr0nix.Closure.Helper.v1.3")

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_amber.xml', extra=style.extra)
    stylesheet = app.styleSheet()
    app.setStyleSheet(stylesheet + style.stylesheet)

    controller = MainController()
    controller.setCache(cache.Cache(getcwd()))
    configs = config.Config(path.join(getcwd(), 'Config.json'))
    windows = WindowController(controller, path.dirname(__file__))
    event.init(controller, windows, configs)
    updates = update.Update(getcwd(), windows)
    gamedata.init(path.join(path.dirname(__file__), 'resources', 'json'))
    constant.init(getcwd())

    end = time.process_time()
    print(end-start)

    updates.start()
    sys.exit(app.exec_())
