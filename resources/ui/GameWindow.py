from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFrame
from . import UI_GameWindow, GameCard
from ..lib import event


class MainWindow(QMainWindow, UI_GameWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gameframes = []
        self.gamecards = []
        self.label_2.setProperty('class', 'closure_label')

    def addFrame(self, card):
        frame = QFrame(self.scrollAreaWidgetContents)
        frame.resize(330, 250)
        frame.move(card[0] - 5, card[1])
        frame.setFrameShape(QFrame.Box)
        frame.setStyleSheet('border-color: #ffd740;')
        print(frame.pos())
        self.gameframes.append(frame)

    def addCard(self, data, pos):
        card = GameCard.Widget(self.scrollAreaWidgetContents, data)
        card.horizontalLayoutWidget.move(pos[0], pos[1] + 5)
        card.move(pos[0], pos[1] + 5)
        card.setObjectName(data['config']['account'])
        self.scrollAreaWidgetContents.setGeometry(0, 0, 1200, pos[1] + 260)
        self.gamecards.append(card)

    def addAnnouncement(self, text):
        self.label.setText(text)
