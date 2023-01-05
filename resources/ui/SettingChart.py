from PyQt5 import QtWidgets
import qtawesome as qta

from resources.ui import UI_SettingChart, TagLabel, ToggleSwitch
from resources.lib import gamedata

class Widget(QtWidgets.QWidget, UI_SettingChart.Ui_Form):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.setupUi(parent)
        self.account = data['account']
        self.platform = data['platform']
        self.maxAP = data['status']['maxAp']
        self.config = data['config']
        self.maps = self.config['battleMaps']
        self.addContent()
        self.pushButton.setIcon(qta.icon('fa5s.save', options=[{'scale_factor': 1, 'color': '#ffd740'}]))
        self.pushButton.clicked.connect(self.saveConfig)

    def addContent(self):
        self.Account.setText('账号：' + self.account)
        self.serverTag = TagLabel.Tag(12)
        self.horizontalLayout.addWidget(self.serverTag)
        if self.platform == 1:
            self.serverTag.setText(' 官服')
            self.serverTag.setFixedSize(43, 24)
        else:
            self.serverTag.setText(' B服')
            self.serverTag.setFixedSize(42, 24)
        self.APBox.setMaximum(self.maxAP)
        self.APBox.setValue(self.config['keepingAP'])
        self.RecuritBox.setValue(self.config['recruitReserve'])
        self.isArrange = ToggleSwitch.SliderButton(checked=self.config['enableBuildingArrange'], size=(40, 20))
        self.horizontalLayout_5.addWidget(self.isArrange)
        self.isAutoBattle = ToggleSwitch.SliderButton(checked=self.config['isAutoBattle'], size=(40, 20))
        self.horizontalLayout_6.addWidget(self.isAutoBattle)
        self.isRecuritIgnore = ToggleSwitch.SliderButton(checked=self.config['recruitIgnoreRobot'], size=(40, 20))
        self.horizontalLayout_7.addWidget(self.isRecuritIgnore)
        mapstr = ''
        for i in self.config['battleMaps']:
            mapstr = mapstr + gamedata.getMapCode(i)
        self.label_8.setText(mapstr)

    def saveConfig(self):
        self.config['isAutoBattle'] = self.isAutoBattle.checked
        self.config['battleMaps'] = self.maps
        self.config['keepingAP'] = self.APBox.value()
        self.config['recruitReserve'] = self.RecuritBox.value()
        self.config['recruitIgnoreRobot'] = self.isRecuritIgnore.checked
        self.config['enableBuildingArrange'] = self.isArrange.checked
