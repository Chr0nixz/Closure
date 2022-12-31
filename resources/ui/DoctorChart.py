from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome as qta
import time

from . import UI_DoctorChart
from ..lib import event


class Widget(QtWidgets.QWidget, UI_DoctorChart.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(parent)

    def addContent(self, data):
        self.NickName.setText('Dr.' + data['nickName'])
        now = time.time()
        lastAPtime = data['lastApAddTime']
        maxAP = data['maxAp']
        AP = int((now - lastAPtime) / 360)
        if data['ap'] + AP > maxAP:
            currentAP = maxAP
        else:
            currentAP = data['ap'] + AP
        APtime = (maxAP - data['ap']) * 360 + lastAPtime
        APtimeStr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(APtime))
        value = int(currentAP / maxAP * 100)
        self.CurrentAP.setText(str(currentAP))
        self.maxAP.setText(str(maxAP))
        self.APBar.setValue(value)
        self.APTime.setText(APtimeStr)
        if value in range(0, 75):
            self.APDescription.setText('理智还有一段时间才恢复满呢~')
