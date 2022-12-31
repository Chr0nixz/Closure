import os
import sys

from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet

from resources.lib.arknights import MainController
from resources.lib.windows import WindowController
from resources.lib import event, config
from resources.style import style

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_amber.xml', extra=style.extra)
    stylesheet = app.styleSheet()
    app.setStyleSheet(stylesheet + style.stylesheet)
    controller = MainController()
    configs = config.Config(os.path.join(os.getcwd(), 'Config.json'))
    event.addHandler(controller)
    event.addConfig(configs)
    windows = WindowController(controller)
    event.addWindows(windows)
    sys.exit(app.exec_())
