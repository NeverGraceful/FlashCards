import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel, QApplication

class CustomizeListMenu(QtWidgets.QDialog):
    def __init__(self):
        super(CustomizeListMenu, self).__init__()
        # self.ui = custom.Ui_Dialog()
        # self.ui.setupUi(self)
        # self.setWindowTitle('Customize Practice')