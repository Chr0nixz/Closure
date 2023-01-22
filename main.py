import os
import sys
import ctypes

from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet

from resources.lib.arknights import MainController
from resources.lib.windows import WindowController
from resources.lib.update import Update
from resources.lib.cache import Cache
from resources.lib.config import Config
from resources.lib import event, gamedata, constant
from resources.style import style

if __name__ == '__main__':

    # 设置AppID （保证任务栏图标正确）
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Chr0nix.Closure.Helper.v1.3")

    # 实例化主应用
    app = QApplication(sys.argv)

    # 应用qt-material样式表
    apply_stylesheet(app, theme='dark_amber.xml', extra=style.extra)
    stylesheet = app.styleSheet()
    app.setStyleSheet(stylesheet + style.stylesheet)

    # 实例化控制器类
    controller = MainController()    # 主控制器
    controller.setCache(Cache(os.getcwd()))    # 设置缓存
    config = Config(os.path.join(os.getcwd(), 'Config.json'))    # 设置控制器
    windows = WindowController(controller, os.path.dirname(__file__))    # 窗体控制器
    event.init(controller, windows, config)    # 事件初始化
    update = Update(os.getcwd(), windows)    # 数据更新控制器
    gamedata.init(os.path.join(os.path.dirname(__file__), 'resources', 'json'))    # 游戏数据常量
    constant.init(os.getcwd())    # 常量

    # 开始更新
    update.start()

    # 主循环
    sys.exit(app.exec())
