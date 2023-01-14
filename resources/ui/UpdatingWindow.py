from PyQt5.QtWidgets import QMainWindow

from resources.ui import UI_UpdatingWindow


class MainWindow(QMainWindow, UI_UpdatingWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
