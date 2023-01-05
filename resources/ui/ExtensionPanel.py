from PyQt5 import QtWidgets
import qtawesome as qta

from resources.ui import UI_ExtensionPanel


class Widget(QtWidgets.QWidget, UI_ExtensionPanel.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(parent)
        self.pushButton_2.setIcon(qta.icon('mdi.warehouse', options=[{'scale_factor': 1, 'color': '#ffd740'}]))
        self.pushButton_3.setIcon(qta.icon('ri.team-fill', options=[{'scale_factor': 1, 'color': '#ffd740'}]))
