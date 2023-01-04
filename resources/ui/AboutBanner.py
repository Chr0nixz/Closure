from PyQt5 import QtWidgets
import webbrowser

from resources.ui import UI_AboutBanner


class Widget(QtWidgets.QWidget, UI_AboutBanner.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(parent)

    def openClosure(self):
        webbrowser.open(url='https://arknights.host')

    def openGithub(self):
        webbrowser.open(url='https://github.com/Chr0nixz/Closure')
