from PyQt5 import QtWidgets
import webbrowser
import qtawesome as qta

from resources.ui import UI_AboutBanner


class Widget(QtWidgets.QWidget, UI_AboutBanner.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(parent)
        self.pushButton.setIcon(qta.icon('mdi.web', options=[{'scale_factor': 1, 'color': '#ffd740'}]))
        self.pushButton_2.setIcon(qta.icon('mdi.github', options=[{'scale_factor': 1, 'color': '#ffd740'}]))

    def openClosure(self):
        webbrowser.open(url='https://arknights.host')

    def openGithub(self):
        webbrowser.open(url='https://github.com/Chr0nixz/Closure')
