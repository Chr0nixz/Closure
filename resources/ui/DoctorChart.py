import time

from PyQt5 import QtWidgets

from . import UI_DoctorChart, TagLabel


class Widget(QtWidgets.QWidget, UI_DoctorChart.Ui_Form):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.setupUi(parent)
        self.account = data['account']
        self.platform = data['platform']
        self.data = data['status']
        self.addContent()

    def addContent(self):
        self.NickName.setText('Dr.' + self.data['nickName'])
        self.levelTag = TagLabel.Tag(12)
        self.levelTag.setText(' Lv.' + str(self.data['level']))
        self.levelTag.setFixedSize(53, 24)
        self.horizontalLayout_3.addWidget(self.levelTag)
        now = time.time()
        lastAPtime = self.data['lastApAddTime']
        maxAP = self.data['maxAp']
        if self.data['ap'] > maxAP:
            currentAP = self.data['ap']
        else:
            AP = int((now - lastAPtime) / 360)
            if self.data['ap'] + AP > maxAP:
                currentAP = maxAP
            else:
                currentAP = self.data['ap'] + AP
            APtime = (maxAP - self.data['ap']) * 360 + lastAPtime
            APtimeStr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(APtime))
        value = int(currentAP / maxAP * 100)
        self.CurrentAP.setText(str(currentAP))
        self.maxAP.setText(str(maxAP))
        if value > 100:
            self.APBar.setValue(100)
        else:
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
        elif value > 100:
            self.APDescription.setText('这么多理智，可露希尔要累死啦！')
            self.APBar.setProperty('class', 'danger')
