from PyQt5 import QtWidgets

from resources.ui import UI_SettingChart

class Widget(QtWidgets.QWidget, UI_SettingChart.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(parent)

