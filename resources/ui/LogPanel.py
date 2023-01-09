from PyQt5 import QtWidgets
import time

from resources.ui import UI_LogPanel, LogLabel


class Widget(QtWidgets.QWidget, UI_LogPanel.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(parent)
        self.widgets = []
        self.labels = []

    def addContent(self, res):
        data = res[1]
        for i in data:
            label = LogLabel.Widget(self.generateWidget())
            timeStr = time.strftime('%Y-%m-%d\n%H:%M:%S', time.localtime(int(i['ts'])))
            label.label.setText(timeStr)
            label.label_2.setText(i['info'])

    def generateWidget(self):
        widget = QtWidgets.QWidget()
        self.verticalLayout_4.addWidget(widget)
        self.widgets.append(widget)
        return widget
