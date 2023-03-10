import re

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import qtawesome as qta

from . import UI_LoginWindow
from ..lib import event
from .ToggleSwitch import SliderButton


class MainWindow(QMainWindow, UI_LoginWindow.Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(450, 600)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.Label_closure.setProperty('class', 'closure_label')
        self.LoginButton.setIcon(qta.icon('mdi.login', options=[{'scale_factor': 1, 'color': '#ffd740'}]))
        self.LoginButton.clicked.connect(self.login)
        default = event.getDefaultAccount()
        if default:
            self.email_input.setText(default.get('email'))
            self.password_input.setText(default.get('password'))

    def login(self):
        print(re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', self.email_input.text()))
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',
                        self.email_input.text()) or self.password_input.text() == '':
            QMessageBox.warning(self, 'Warning!', '请输入正确的邮箱和密码', QMessageBox.Ok)
        else:
            self.statusbar.showMessage('准备登陆')
            self.email_input.setEnabled(False)
            self.password_input.setEnabled(False)
            self.LoginButton.setEnabled(False)
            event.process('login', [self.email_input.text(), self.password_input.text()], self.loginResult)

    def loginFailed(self):
        QMessageBox.critical(self, 'Wrong!', '邮箱或密码错误', QMessageBox.Ok)
        self.email_input.setEnabled(True)
        self.password_input.setEnabled(True)
        self.LoginButton.setEnabled(True)
        self.statusBar().showMessage('登陆失败')

    def serverMaintain(self):
        QMessageBox.critical(self, '维护中', '服务器维护中，请稍后再试！', QMessageBox.Ok)
        self.email_input.setEnabled(True)
        self.password_input.setEnabled(True)
        self.LoginButton.setEnabled(True)
        self.statusBar().showMessage('服务器维护中')

    def loginResult(self, result):
        if result[0]:
            self.statusbar.showMessage('登陆成功，正在跳转...')
            event.process('get_games', )
        else:
            if result[1] == 0:
                self.serverMaintain()
            else:
                self.loginFailed()
