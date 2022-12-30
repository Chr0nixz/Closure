from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome as qta

from . import UI_DoctorChart
from ..lib import event


class Widget(QtWidgets.QWidget, UI_DoctorChart.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(parent)


