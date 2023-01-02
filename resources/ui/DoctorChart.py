import time

from PyQt5 import QtWidgets

from . import UI_DoctorChart, TagLabel


class Widget(QtWidgets.QWidget, UI_DoctorChart.Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(parent)

    def addContent(self, data):
        self.NickName.setText('Dr.' + data['nickName'])
        self.levelTag = TagLabel.Tag(12)
        self.levelTag.setText(' Lv.' + str(data['level']))
        self.levelTag.setFixedSize(53, 24)
        self.horizontalLayout_3.addWidget(self.levelTag)
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
        if value in range(0, 50):
            self.APDescription.setText('理智还有一段时间才恢复满呢~')
        elif value in range(50, 75):
            self.APDescription.setText('理智好像有点多了呢~')
        elif value in range(75, 100):
            self.APDescription.setText('理智快满啦，可露希尔在努力刷关呢~')
            self.APBar.setProperty('class', 'danger')
        elif value == 100:
            self.APDescription.setText('理智都溢出啦！是不是出问题了？')
            self.APBar.setProperty('class', 'danger')
