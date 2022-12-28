from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFrame, QWidget
from . import UI_GameWindow, GameCard
from ..lib import event


class MainWindow(QMainWindow, UI_GameWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.build = False
        self.setupUi(self)
        self.gameframes = []
        self.gamecards = []
        self.label_2.setProperty('class', 'closure_label')

    def addFrame(self):
        frame = QFrame(self.scrollAreaWidgetContents)
        frame.resize(345, 255)
        frame.setFrameShape(QFrame.Box)
        frame.setStyleSheet('border-color: #ffd740;')
        print(frame.pos())
        self.gameframes.append(frame)

    def addCard(self, data):
        widget = QWidget(self.scrollAreaWidgetContents)
        card = GameCard.Widget(widget, data)
        self.gamecards.append(card)

    def addAnnouncement(self, text):
        self.label.setText(text)

    def resizeEvent(self, change) -> None:
        event.gameCardFlex(self.width(), self.height())
        self.build = True
