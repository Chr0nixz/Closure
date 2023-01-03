from PyQt5 import QtWidgets

from resources.ui import UI_ScreenshotChart


class Widget(QtWidgets.QWidget, UI_ScreenshotChart.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(parent)

