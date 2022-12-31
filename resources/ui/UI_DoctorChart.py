# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_DoctorChart.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(341, 800)
        Form.setMinimumSize(QtCore.QSize(250, 0))
        Form.setMaximumSize(QtCore.QSize(400, 16777215))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CharLayout = QtWidgets.QHBoxLayout()
        self.CharLayout.setObjectName("CharLayout")
        self.verticalLayout_2.addLayout(self.CharLayout)
        self.NickName = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.NickName.setFont(font)
        self.NickName.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.NickName.setObjectName("NickName")
        self.verticalLayout_2.addWidget(self.NickName)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.APLabel = QtWidgets.QLabel(Form)
        self.APLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.APLabel.setFont(font)
        self.APLabel.setStyleSheet("color: #ffd740")
        self.APLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.APLabel.setObjectName("APLabel")
        self.verticalLayout_2.addWidget(self.APLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CurrentAP = QtWidgets.QLabel(Form)
        self.CurrentAP.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CurrentAP.setFont(font)
        self.CurrentAP.setStyleSheet("color: #ffd740")
        self.CurrentAP.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CurrentAP.setObjectName("CurrentAP")
        self.horizontalLayout.addWidget(self.CurrentAP)
        self.midLabel = QtWidgets.QLabel(Form)
        self.midLabel.setMaximumSize(QtCore.QSize(23, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.midLabel.setFont(font)
        self.midLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.midLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.midLabel.setObjectName("midLabel")
        self.horizontalLayout.addWidget(self.midLabel)
        self.maxAP = QtWidgets.QLabel(Form)
        self.maxAP.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.maxAP.setFont(font)
        self.maxAP.setObjectName("maxAP")
        self.horizontalLayout.addWidget(self.maxAP)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.APBar = QtWidgets.QProgressBar(Form)
        self.APBar.setMaximumSize(QtCore.QSize(16777215, 15))
        self.APBar.setProperty("value", 24)
        self.APBar.setObjectName("APBar")
        self.verticalLayout_2.addWidget(self.APBar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #ffd740")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.APTime = QtWidgets.QLabel(Form)
        self.APTime.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.APTime.setFont(font)
        self.APTime.setAlignment(QtCore.Qt.AlignCenter)
        self.APTime.setObjectName("APTime")
        self.verticalLayout_2.addWidget(self.APTime)
        self.APDescription = QtWidgets.QLabel(Form)
        self.APDescription.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.APDescription.setFont(font)
        self.APDescription.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.APDescription.setObjectName("APDescription")
        self.verticalLayout_2.addWidget(self.APDescription)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #ffd740")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setMinimumSize(QtCore.QSize(0, 40))
        self.startButton.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_5.addWidget(self.startButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(15, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pauseButton = QtWidgets.QPushButton(Form)
        self.pauseButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pauseButton.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pauseButton.setFont(font)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_6.addWidget(self.pauseButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setMinimumSize(QtCore.QSize(0, 40))
        self.deleteButton.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteButton.setFont(font)
        self.deleteButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_4.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.refreshButton = QtWidgets.QPushButton(Form)
        self.refreshButton.setMinimumSize(QtCore.QSize(0, 40))
        self.refreshButton.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.refreshButton.setFont(font)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_7.addWidget(self.refreshButton)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.NickName.setText(_translate("Form", "Dr.Name"))
        self.APLabel.setText(_translate("Form", "理智"))
        self.CurrentAP.setText(_translate("Form", "120"))
        self.midLabel.setText(_translate("Form", "/"))
        self.maxAP.setText(_translate("Form", "135"))
        self.label_2.setText(_translate("Form", "理智溢出时间"))
        self.APTime.setText(_translate("Form", "APTime"))
        self.APDescription.setText(_translate("Form", "APDescription"))
        self.label.setText(_translate("Form", "操作"))
        self.startButton.setText(_translate("Form", " 开 始"))
        self.pauseButton.setText(_translate("Form", " 暂 停"))
        self.deleteButton.setText(_translate("Form", " 删 除"))
        self.refreshButton.setText(_translate("Form", " 刷 新"))