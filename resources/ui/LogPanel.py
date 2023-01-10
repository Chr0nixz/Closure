from PyQt5.QtWidgets import QLabel, QWidget, QMessageBox
import time

from resources.ui import UI_LogPanel, LogLabel


class Widget(QWidget, UI_LogPanel.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(parent)
        self.widgets = []
        self.labels = []

    def addContent(self, res):
        if res[0]:
            data = res[1]
            data.reverse()
            for i in data:
                label = LogLabel.Widget(self.generateWidget())
                timeStr = time.strftime('%Y-%m-%d\n%H:%M:%S', time.localtime(int(i['ts'])))
                label.label.setText(timeStr)
                label.label_2.setText(i['info'])
        else:
            QMessageBox.warning(self.parent(), 'NetworkError', '获取日志失败！', QMessageBox.Ok)

    def generateWidget(self):
        widget = QWidget()
        self.verticalLayout_4.addWidget(widget)
        self.widgets.append(widget)
        return widget
