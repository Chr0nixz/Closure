from PyQt5.QtWidgets import QMainWindow, QWidget

from resources.ui import UI_DetailWindow, DoctorChart, SettingChart, ScreenshotChart, ExtensionPanel, AboutBanner, LogPanel
from resources.ui.CircleImage import CircleImage
from resources.lib import event, constant


class MainWindow(QMainWindow, UI_DetailWindow.Ui_MainWindow):
    def __init__(self, data):
        super().__init__()
        self.setupUi(self)
        self.data = data
        self.widgets = []
        self.account = data['account']
        self.platform = data['platform']
        if self.platform == 1:
            self.title = '可露希尔' + self.account + '（官服）'
        else:
            self.title = '可露希尔' + self.account + '（B服）'
        self.setWindowTitle(self.title)
        self.addChart()
        self.addAssistantPic(constant.chars_path + self.data['status']['secretary'] + '.png')
        self.addWidgets()
        self.getData()

    def addAssistantPic(self, img):
        self.charPic = CircleImage(self.centralwidget, 0, 0, 150, 150)
        self.charPic.setImage(img)
        self.charPic.setFixedSize(150, 150)
        self.doctorChart.CharLayout.addWidget(self.charPic)

    def addChart(self):
        widget = QWidget(self.centralwidget)
        self.doctorChart = DoctorChart.Widget(widget, self.data)
        self.doctorLayout.addWidget(widget, 1, 1)

    def addWidgets(self):
        self.settingChart = SettingChart.Widget(self.generateWidget(), self.data)
        self.screenShot = ScreenshotChart.Widget(self.generateWidget(), self.data)
        self.exChart = ExtensionPanel.Widget(self.generateWidget())
        self.logChart = LogPanel.Widget(self.generateWidget())
        self.aboutBanner = AboutBanner.Widget(self.generateWidget())
        self.gridLayout_3.addWidget(self.settingChart.parent(), 1, 1, 4, 4)
        self.gridLayout_3.addWidget(self.screenShot.parent(), 1, 5, 3, 5)
        self.gridLayout_3.addWidget(self.exChart.parent(), 5, 1, 3, 4)
        self.gridLayout_3.addWidget(self.logChart.parent(), 4, 5, 4, 5)
        self.gridLayout_3.addWidget(self.aboutBanner.parent(), 8, 1, 1, 9)
        self.gridLayout_3.setRowStretch(1, 2)
        self.gridLayout_3.setRowStretch(2, 2)
        self.gridLayout_3.setRowStretch(3, 2)
        self.gridLayout_3.setRowStretch(4, 2)
        self.gridLayout_3.setRowStretch(5, 2)
        self.gridLayout_3.setRowStretch(6, 2)
        self.gridLayout_3.setRowStretch(7, 2)
        self.gridLayout_3.setRowStretch(8, 1)
        print(self.gridLayout_3.rowCount())

    def generateWidget(self):
        widget = QWidget(self)
        self.widgets.append(widget)
        return widget

    def getData(self):
        event.process('log', [self.account, self.platform], self.logChart.addContent)

    def resizeEvent(self, event) -> None:
        if hasattr(self, 'screenShot'):
            self.screenShot.repix()
