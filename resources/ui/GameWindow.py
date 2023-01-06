from PyQt5.QtWidgets import QMainWindow, QFrame, QWidget
import qtawesome as qta

from . import UI_GameWindow, GameCard
from ..lib import event


class MainWindow(QMainWindow, UI_GameWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.build = False
        self.setupUi(self)
        self.gameframes = []
        self.gamecards = []
        self.cardwidgets = []
        self.label_2.setProperty('class', 'closure_label')
        self.refreshButton.setIcon(qta.icon('fa.refresh', options=[{'scale_factor': 1, 'color': '#ffd740'}]))
        self.refreshButton.clicked.connect(event.refreshGames)

    def addFrame(self):
        frame = QFrame(self.scrollAreaWidgetContents)
        frame.resize(345, 255)
        frame.setFrameShape(QFrame.Box)
        frame.setStyleSheet('border-color: #ffd740;')
        print(frame.pos())
        self.gameframes.append(frame)

    def addCard(self, data, num):
        card = GameCard.Widget(self.addCardWidget(), data, num)
        self.gamecards.append(card)

    def addCardWidget(self):
        widget = QWidget(self.scrollAreaWidgetContents)
        self.cardwidgets.append(widget)
        return widget

    def addAnnouncement(self, text):
        self.label.setText(text)

    def resizeEvent(self, change) -> None:
        col = self.width() // 380
        space = (self.width() - col * 400) / col / 2
        maxheight = 0
        num = 0
        for i in self.gameframes:
            num += 1
            frameheight = (((num + col - 1) // col) - 1) * 275
            i.move(int(((num + col - 1) % col) * (400 + 2 * space) + space) + 15, (((num + col - 1) // col) - 1) * 275)
            if frameheight + 260 > maxheight:
                maxheight = frameheight + 260
        num = 0
        for i in self.gamecards:
            num += 1
            i.parent().move(int(((num + col - 1) % col) * (400 + 2 * space) + space) + 30,
                            (((num + col - 1) // col) - 1) * 275 + 5)
        self.scrollAreaWidgetContents.setGeometry(0, 0, self.width(), maxheight)