from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5.QtCore import Qt

from resources.ui import UI_DetailWindow
from resources.ui.CircleImage import CircleImage


class MainWindow(QMainWindow, UI_DetailWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addAssistantPic("C:/Users/czxxx/Desktop/Closure/resources/img/icon.png")

    def addAssistantPic(self, img):
        self.charPic = CircleImage(self.centralwidget, 200, 200)
        self.charPic.setImage(img)
        self.verticalLayout.addWidget(self.charPic)