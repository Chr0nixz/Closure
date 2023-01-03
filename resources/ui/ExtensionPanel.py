from PyQt5 import QtWidgets

from resources.ui import UI_ExtensionPanel


class Widget(QtWidgets.QWidget, UI_ExtensionPanel.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(parent)