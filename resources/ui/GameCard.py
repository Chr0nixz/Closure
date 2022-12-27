from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget

from . import UI_GameCard
from ..lib import event


class Widget(QWidget, UI_GameCard.Ui_Form):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.setupUi(parent)
        self.setFixedSize(320, 240)
        self.setStyleSheet('background-color: #000000;')
        self.addGames(data)
        self.show()

    def addGames(self, data):
        _translate = QtCore.QCoreApplication.translate
        if data['config']['platform'] == 1:
            self.Account_label.setText(_translate("Form", '账号：' + data['config']['account'] + '（官服）'))
        else:
            self.Account_label.setText(_translate("Form", '账号：' + data['config']['account'] + '（B服）'))
        if data['config']['isPause']:
            self.Status_label.setText(_translate("Form", '暂停中'))
            self.statusButton.setProperty('class', 'success')
        else:
            self.Status_label.setText(_translate("Form", data['status']['text']))
            match data['status']['code']:
                case -1: self.setLoginButton()
                case 0: self.setLoginButton()
                case 1: self.statusButton.setEnabled(False)
                case 2: self.setPauseButton()
                case 3: self.setLoginButton()
        self.Map_label.setText(
            _translate("Form", data['game_config']['mapId']['code'] + ' ' + data['game_config']['mapId']['name']))
        self.AP_label.setText(_translate("Form", str(data['game_config']['keepingAP'])))

    def setLoginButton(self):
        self.statusButton.setProperty('class', 'success')

    def setPauseButton(self):
        self.statusButton.setText('暂 停')
        self.statusButton.setProperty('class', 'danger')

