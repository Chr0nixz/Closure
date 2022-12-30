from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome as qta

from . import UI_GameCard
from ..lib import event


class Widget(QtWidgets.QWidget, UI_GameCard.Ui_Form):
    def __init__(self, parent, data, num):
        super().__init__(parent)
        self.setupUi(parent)
        self.setFixedSize(320, 240)
        self.num = num
        self.account = data['config']['account']
        self.platform = data['config']['platform']
        #self.detailButton.setEnabled(False)
        self.addGames(data)

    def addGames(self, data):
        self.addContent(data)
        self.detailButton.clicked.connect(self.openDetail)

    def refresh(self, data):
        self.statusButton.hide()
        self.statusButton.deleteLater()
        self.detailButton.hide()
        self.detailButton.deleteLater()
        self.statusButton = self.addStatusButton()
        self.detailButton = self.addDetailButton()
        self.addContent(data)
        self.statusButton.show()
        self.detailButton.show()

    def addStatusButton(self):
        statusButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        statusButton.setMinimumSize(QtCore.QSize(0, 35))
        statusButton.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        statusButton.setFont(font)
        statusButton.setObjectName("statusButton")
        statusButton.setText(' 开 始')
        self.horizontalLayout.addWidget(statusButton)
        return statusButton

    def addDetailButton(self):
        detailButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        detailButton.setMinimumSize(QtCore.QSize(0, 35))
        detailButton.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        detailButton.setFont(font)
        detailButton.setObjectName("detailButton")
        detailButton.setText(' 详 情')
        detailButton.setIconSize(QtCore.QSize(20, 20))
        detailButton.setEnabled(False)
        self.horizontalLayout.addWidget(detailButton)
        return detailButton

    def addContent(self, data):
        _translate = QtCore.QCoreApplication.translate
        if self.platform == 1:
            self.Account_label.setText(_translate("Form", '账号：' + self.account + '（官服）'))
        else:
            self.Account_label.setText(_translate("Form", '账号：' + self.account + '（B服）'))
        if data['config']['isPause']:
            self.Status_label.setText(_translate("Form", '暂停中'))
            self.setLoginButton()
        else:
            self.Status_label.setText(_translate("Form", data['status']['text']))
            match data['status']['code']:
                case -1:
                    self.setLoginButton()
                case 0:
                    self.setLoginButton()
                case 1:
                    self.statusButton.setEnabled(False)
                case 2:
                    self.setPauseButton()
                    self.detailButton.setEnabled(True)
                case 3:
                    self.setLoginButton()
        self.Map_label.setText(
            _translate("Form", data['game_config']['mapId']['code'] + ' ' + data['game_config']['mapId']['name']))
        self.AP_label.setText(_translate("Form", str(data['game_config']['keepingAP'])))
        self.setDetailButton()

    def setLoginButton(self):
        self.statusButton.setText(' 开 始')
        self.statusButton.setProperty('class', 'success')
        self.statusButton.setIcon(qta.icon('mdi.power', options=[{'scale_factor': 1.4, 'color': 'green'}]))

    def setPauseButton(self):
        self.statusButton.setText(' 暂 停')
        self.statusButton.setProperty('class', 'danger')
        self.statusButton.setIcon(qta.icon('mdi.power', options=[{'scale_factor': 1.4, 'color': 'red'}]))

    def setDetailButton(self):
        self.detailButton.setIcon(qta.icon('mdi.card-account-details-star', options=[{'scale_factor': 1, 'color': '#ffd740'}]))

    def openDetail(self):
        event.getDetail(self.account, self.platform)

