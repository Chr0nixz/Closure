from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow
import qtawesome as qta

from resources.ui import UI_CheckUpdateWindow

class MainWindow(QMainWindow, UI_CheckUpdateWindow.Ui_MainWindow):
    def __init__(self, icon):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(icon)
        self.setWindowTitle('检查更新')
        self.setFixedSize(300, 400)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.loadingIcon = qta.IconWidget()
        self.loadingIcon.setFixedSize(100, 100)
        self.loadingIcon.setIconSize(QSize(100, 100))
        self.loadingIcon.setIcon(qta.icon('mdi.loading', color='#ffc107', animation=qta.Spin(self.loadingIcon)))
        self.gridLayout.addWidget(self.loadingIcon)

    def updated(self):
        self.loadingIcon.setIcon(qta.icon('fa5s.check', color='green'))
