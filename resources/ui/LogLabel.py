from PyQt5 import QtWidgets

from resources.ui import UI_LogLabel


class Widget(QtWidgets.QWidget, UI_LogLabel.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(parent)
