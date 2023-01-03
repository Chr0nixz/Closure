import qtawesome as qta
from PyQt5 import QtCore, QtGui, QtWidgets

from . import UI_GameCard, TagLabel
from ..lib import event


class Widget(QtWidgets.QWidget, UI_GameCard.Ui_Form):
    def __init__(self, parent, data, num):
        super().__init__(parent)
        self.setupUi(parent)
        self.setFixedSize(320, 240)
        self.num = num
        self.account = data['config']['account']
        self.platform = data['config']['platform']
        self.detailButton.setEnabled(False)
        self.serverTag = TagLabel.Tag(12)
        self.horizontalLayout_5.addWidget(self.serverTag)
        self.addContent(data)


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
        self.Account_label.setText(_translate("Form", '账号：' + self.account))
        if self.platform == 1:
            self.serverTag.setText(' 官服')
            self.serverTag.setFixedSize(43, 24)
        else:
            self.serverTag.setText(' B服')
            self.serverTag.setFixedSize(42, 24)
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
                    self.setLoginButton()
                    self.statusButton.setEnabled(False)
                case 2:
                    self.setPauseButton()
                    self.detailButton.setEnabled(True)
                case 3:
                    self.setLoginButton()
                case 4:
                    self.setLoginButton()
                case 5:
                    self.setLoginButton()
                case 999:
                    self.setLoginButton()
                    self.statusButton.setEnabled(False)
        self.Map_label.setText(
            _translate("Form", data['game_config']['mapId']['code'] + ' ' + data['game_config']['mapId']['name']))
        self.AP_label.setText(_translate("Form", str(data['game_config']['keepingAP'])))
        self.setDetailButton()
        self.detailButton.clicked.connect(self.openDetail)

    def setLoginButton(self):
        self.statusButton.setText(' 开 始')
        self.statusButton.setProperty('class', 'success')
        self.statusButton.setIcon(qta.icon('mdi.power', options=[{'scale_factor': 1.4, 'color': 'green'}]))
        self.statusButton.clicked.connect(self.gameLogin)

    def setPauseButton(self):
        self.statusButton.setText(' 暂 停')
        self.statusButton.setProperty('class', 'danger')
        self.statusButton.setIcon(qta.icon('mdi.power', options=[{'scale_factor': 1.4, 'color': 'red'}]))

    def setDetailButton(self):
        self.detailButton.setIcon(qta.icon('mdi.card-account-details-star', options=[{'scale_factor': 1, 'color': '#ffd740'}]))

    def openDetail(self):
        event.getDetail(self.account, self.platform)

    def gameLogin(self):
        self.statusButton.setText('登陆中')
        self.statusButton.setEnabled(False)
        event.gameLogin(self.account, self.platform)
