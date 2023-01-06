from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import qtawesome as qta

from resources.ui import UI_ScreenshotChart
from resources.lib import event


class Widget(QtWidgets.QWidget, UI_ScreenshotChart.Ui_Form):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.setupUi(parent)
        self.account = data['account']
        self.platform = data['platform']
        self.screenpixs = []
        self.currentpix = 0
        event.pullScreenshots(self, self.account, self.platform)
        self.label.setText('正在加载图片...')
        self.pushButton.setIcon(qta.icon('mdi.menu-left', options=[{'scale_factor': 1.5, 'color': '#ffd740'}]))
        self.pushButton_2.setIcon(qta.icon('mdi.menu-right', options=[{'scale_factor': 1.5, 'color': '#ffd740'}]))
        self.pushButton.clicked.connect(self.left)
        self.pushButton_2.clicked.connect(self.right)
        self.pushButton.setEnabled(False)

    def addScreenshots(self, screenshots):
        self.screenshots = screenshots
        for i in self.screenshots:
            pix = QPixmap(i)
            self.screenpixs.append(pix)
        self.maxpix = len(self.screenpixs) - 1
        self.label.setPixmap(self.screenpixs[self.currentpix].scaled(self.label.size()))

    def repix(self):
        if not self.screenpixs == []:
            self.label.setPixmap(self.screenpixs[self.currentpix].scaled(self.label.size()))

    def left(self):
        if self.currentpix > 0:
            if self.currentpix == self.maxpix:
                self.pushButton_2.setEnabled(True)
            self.currentpix -= 1
            self.label.setPixmap(self.screenpixs[self.currentpix].scaled(self.label.size()))
            if self.currentpix == 0:
                self.pushButton.setEnabled(False)

    def right(self):
        if self.currentpix < self.maxpix:
            if self.currentpix == 0:
                self.pushButton.setEnabled(True)
            self.currentpix += 1
            self.label.setPixmap(self.screenpixs[self.currentpix].scaled(self.label.size()))
            if self.currentpix == self.maxpix:
                self.pushButton_2.setEnabled(False)
