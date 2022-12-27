from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from . import UI_GameCard
from ..lib import event


class Widget(QWidget, UI_GameCard.Ui_Form):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.setupUi(parent)
        self.setFixedSize(320, 240)
        self.statusButton.clicked.connect(self.cli)
        self.detailButton.clicked.connect(self.cli)
        self.setStyleSheet('background-color: #000000;')
        self.addGames(data)
        self.show()

    def addGames(self, data):
        _translate = QtCore.QCoreApplication.translate
        self.Account_label.setText(_translate("Form", '账号：' + data['config']['account']))
        if data['config']['isPause']:
            self.Status_label.setText(_translate("Form", '暂停中'))
        else:
            self.Status_label.setText(_translate("Form", data['status']['text']))
        self.Map_label.setText(
            _translate("Form", data['game_config']['mapId']['code'] + ' ' + data['game_config']['mapId']['name']))
        self.AP_label.setText(_translate("Form", str(data['game_config']['keepingAP'])))
        self.statusButton.setProperty('class', 'success')

    def cli(self):
        event.refreshGames()


