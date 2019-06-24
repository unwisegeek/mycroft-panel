# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Config(object):
    def setupUi(self, Config):
        Config.setObjectName("Config")
        Config.setMinimumSize(QtCore.QSize(0, 0))
        Config.setSizeGripEnabled(False)
        self.label = QtWidgets.QLabel(Config)
        self.label.setGeometry(QtCore.QRect(10, 10, 461, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineURI = QtWidgets.QLineEdit(Config)
        self.lineURI.setGeometry(QtCore.QRect(10, 30, 451, 26))
        self.lineURI.setObjectName("lineURI")
        self.label_2 = QtWidgets.QLabel(Config)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 461, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.button1Name = QtWidgets.QLineEdit(Config)
        self.button1Name.setGeometry(QtCore.QRect(10, 100, 113, 26))
        self.button1Name.setObjectName("button1Name")
        self.button1Command = QtWidgets.QLineEdit(Config)
        self.button1Command.setGeometry(QtCore.QRect(130, 100, 331, 26))
        self.button1Command.setObjectName("button1Command")
        self.button2Command = QtWidgets.QLineEdit(Config)
        self.button2Command.setGeometry(QtCore.QRect(130, 130, 331, 26))
        self.button2Command.setObjectName("button2Command")
        self.button2Name = QtWidgets.QLineEdit(Config)
        self.button2Name.setGeometry(QtCore.QRect(10, 130, 113, 26))
        self.button2Name.setObjectName("button2Name")
        self.button3Command = QtWidgets.QLineEdit(Config)
        self.button3Command.setGeometry(QtCore.QRect(130, 160, 331, 26))
        self.button3Command.setObjectName("button3Command")
        self.button3Name = QtWidgets.QLineEdit(Config)
        self.button3Name.setGeometry(QtCore.QRect(10, 160, 113, 26))
        self.button3Name.setObjectName("button3Name")
        self.button4Command = QtWidgets.QLineEdit(Config)
        self.button4Command.setGeometry(QtCore.QRect(130, 190, 331, 26))
        self.button4Command.setObjectName("button4Command")
        self.button4Name = QtWidgets.QLineEdit(Config)
        self.button4Name.setGeometry(QtCore.QRect(10, 190, 113, 26))
        self.button4Name.setObjectName("button4Name")
        self.button5Command = QtWidgets.QLineEdit(Config)
        self.button5Command.setGeometry(QtCore.QRect(130, 220, 331, 26))
        self.button5Command.setObjectName("button5Command")
        self.button5Name = QtWidgets.QLineEdit(Config)
        self.button5Name.setGeometry(QtCore.QRect(10, 220, 113, 26))
        self.button5Name.setObjectName("button5Name")
        self.button6Command = QtWidgets.QLineEdit(Config)
        self.button6Command.setGeometry(QtCore.QRect(130, 250, 331, 26))
        self.button6Command.setObjectName("button6Command")
        self.button6Name = QtWidgets.QLineEdit(Config)
        self.button6Name.setGeometry(QtCore.QRect(10, 250, 113, 26))
        self.button6Name.setObjectName("button6Name")
        self.okButton = QtWidgets.QPushButton(Config)
        self.okButton.setGeometry(QtCore.QRect(370, 280, 86, 26))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(Config)
        self.cancelButton.setGeometry(QtCore.QRect(280, 280, 86, 26))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(Config)
        QtCore.QMetaObject.connectSlotsByName(Config)

    def retranslateUi(self, Config):
        _translate = QtCore.QCoreApplication.translate
        Config.setWindowTitle(_translate("Config", "Dialog"))
        self.label.setText(_translate("Config", "Mycoft URI (Default: localhost:8181)"))
        self.label_2.setText(_translate("Config", "Custom Buttons"))
        self.okButton.setText(_translate("Config", "Ok"))
        self.cancelButton.setText(_translate("Config", "Cancel"))


