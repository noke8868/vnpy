# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(332, 103)
        self.startButton = QtGui.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(20, 30, 84, 32))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.stopButton = QtGui.QPushButton(Dialog)
        self.stopButton.setGeometry(QtCore.QRect(120, 30, 84, 32))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.JustButton = QtGui.QPushButton(Dialog)
        self.JustButton.setGeometry(QtCore.QRect(220, 30, 84, 32))
        self.JustButton.setObjectName(_fromUtf8("JustButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "定时器", None))
        self.startButton.setText(_translate("Dialog", "开始", None))
        self.stopButton.setText(_translate("Dialog", "停止", None))
        self.JustButton.setText(_translate("Dialog", "立即载入", None))

