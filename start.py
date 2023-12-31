# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(539, 397)
        Dialog.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.SHUFFLE_BUTT = QtWidgets.QPushButton(Dialog)
        self.SHUFFLE_BUTT.setGeometry(QtCore.QRect(330, 80, 121, 31))
        self.SHUFFLE_BUTT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SHUFFLE_BUTT.setObjectName("SHUFFLE_BUTT")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.SCROLL_WIDGET = QtWidgets.QWidget(Dialog)
        self.SCROLL_WIDGET.setGeometry(QtCore.QRect(10, 70, 241, 241))
        self.SCROLL_WIDGET.setStyleSheet("\n"
"background-color: rgb(223, 223, 223);")
        self.SCROLL_WIDGET.setObjectName("SCROLL_WIDGET")
        self.gridLayout = QtWidgets.QGridLayout(self.SCROLL_WIDGET)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.SCROLL_AREA = QtWidgets.QWidget(self.SCROLL_WIDGET)
        self.SCROLL_AREA.setObjectName("SCROLL_AREA")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.SCROLL_AREA)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addWidget(self.SCROLL_AREA, 0, 0, 1, 1)
        self.CUSTOM_BUTT = QtWidgets.QPushButton(Dialog)
        self.CUSTOM_BUTT.setGeometry(QtCore.QRect(330, 120, 121, 31))
        self.CUSTOM_BUTT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CUSTOM_BUTT.setObjectName("CUSTOM_BUTT")
        self.START_BUTT = QtWidgets.QPushButton(Dialog)
        self.START_BUTT.setGeometry(QtCore.QRect(310, 180, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.START_BUTT.setFont(font)
        self.START_BUTT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.START_BUTT.setObjectName("START_BUTT")
        self.ADD_CLASS_BUTT = QtWidgets.QPushButton(Dialog)
        self.ADD_CLASS_BUTT.setGeometry(QtCore.QRect(20, 320, 91, 31))
        self.ADD_CLASS_BUTT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ADD_CLASS_BUTT.setObjectName("ADD_CLASS_BUTT")
        self.ADD_CARD_BUTT = QtWidgets.QPushButton(Dialog)
        self.ADD_CARD_BUTT.setGeometry(QtCore.QRect(150, 320, 91, 31))
        self.ADD_CARD_BUTT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ADD_CARD_BUTT.setObjectName("ADD_CARD_BUTT")
        self.FRONT_FIRST = QtWidgets.QPushButton(Dialog)
        self.FRONT_FIRST.setGeometry(QtCore.QRect(280, 290, 101, 51))
        self.FRONT_FIRST.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FRONT_FIRST.setObjectName("FRONT_FIRST")
        self.BACK_FIRST = QtWidgets.QPushButton(Dialog)
        self.BACK_FIRST.setGeometry(QtCore.QRect(390, 290, 101, 51))
        self.BACK_FIRST.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BACK_FIRST.setObjectName("BACK_FIRST")
        self.ERROR_LABEL = QtWidgets.QLabel(Dialog)
        self.ERROR_LABEL.setGeometry(QtCore.QRect(310, 240, 161, 20))
        self.ERROR_LABEL.setText("")
        self.ERROR_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.ERROR_LABEL.setObjectName("ERROR_LABEL")
        self.REMOVE_CARD_BUTT = QtWidgets.QPushButton(Dialog)
        self.REMOVE_CARD_BUTT.setGeometry(QtCore.QRect(150, 360, 91, 31))
        self.REMOVE_CARD_BUTT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.REMOVE_CARD_BUTT.setObjectName("REMOVE_CARD_BUTT")
        self.REMOVE_CLASS_BUTT = QtWidgets.QPushButton(Dialog)
        self.REMOVE_CLASS_BUTT.setGeometry(QtCore.QRect(20, 360, 91, 31))
        self.REMOVE_CLASS_BUTT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.REMOVE_CLASS_BUTT.setObjectName("REMOVE_CLASS_BUTT")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SHUFFLE_BUTT.setText(_translate("Dialog", "Shuffle List"))
        self.label.setText(_translate("Dialog", "Select class:"))
        self.CUSTOM_BUTT.setText(_translate("Dialog", "Customize List"))
        self.START_BUTT.setText(_translate("Dialog", "Start Practice!"))
        self.ADD_CLASS_BUTT.setText(_translate("Dialog", "New Class"))
        self.ADD_CARD_BUTT.setText(_translate("Dialog", "New Card"))
        self.FRONT_FIRST.setText(_translate("Dialog", "Front First"))
        self.BACK_FIRST.setText(_translate("Dialog", "Back First"))
        self.REMOVE_CARD_BUTT.setText(_translate("Dialog", "Remove Card"))
        self.REMOVE_CLASS_BUTT.setText(_translate("Dialog", "Remove Class"))
