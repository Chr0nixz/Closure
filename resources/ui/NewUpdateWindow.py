from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
import qtawesome as qta

from resources.ui import UI_NewUpdateWindow


class MainWindow(QMainWindow, UI_NewUpdateWindow.Ui_MainWindow):
    def __init__(self, icon, handler):
        super().__init__()
        self.setupUi(self)
        self.handler = handler
        self.setWindowIcon(icon)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.pushButton.setIcon(qta.icon('fa.remove', options=[{'scale_factor': 1, 'color': '#dc3545'}]))
        self.pushButton.setProperty('class', 'danger')
        self.pushButton_2.setIcon(qta.icon('mdi.update', options=[{'scale_factor': 1, 'color': '#1BC4A0'}]))
        self.pushButton_2.setProperty('class', 'success')

    def addText(self, text):
        pass
