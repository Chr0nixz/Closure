import os
import sys
import ctypes

from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet

from resources.lib.arknights import MainController
from resources.lib.windows import WindowController
from resources.lib import event, config, gamedata, cache, constant, update
from resources.style import style

if __name__ == '__main__':

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Chr0nix.Closure.Helper.v1.3")

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_amber.xml', extra=style.extra)
    stylesheet = app.styleSheet()
    app.setStyleSheet(stylesheet + style.stylesheet)

    controller = MainController()
    controller.setCache(cache.Cache(os.getcwd()))
    configs = config.Config(os.path.join(os.getcwd(), 'Config.json'))
    windows = WindowController(controller, os.path.dirname(__file__))
    event.init(controller, windows, configs)
    updates = update.Update(os.getcwd(), windows)
    gamedata.init(os.path.join(os.path.dirname(__file__), 'resources', 'json'))
    constant.init(os.getcwd())

    updates.start()
    sys.exit(app.exec_())
