from PyQt5.QtWidgets import QMainWindow, QWidget

from resources.ui import UI_DetailWindow, DoctorChart
from resources.ui.CircleImage import CircleImage


class MainWindow(QMainWindow, UI_DetailWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.addChart()
        self.addAssistantPic("C:/Users/czxxx/Desktop/Closure/resources/img/icon.png")

    def addAssistantPic(self, img):
        self.charPic = CircleImage(self.centralwidget, 0, 0, 150, 150)
        self.charPic.setImage(img)
        self.charPic.setFixedSize(150, 150)
        self.doctorChart.CharLayout.addWidget(self.charPic)

    def addChart(self):
        widget = QWidget(self.centralwidget)
        self.doctorChart = DoctorChart.Widget(widget)
        self.doctorLayout.addWidget(widget, 1, 1)
