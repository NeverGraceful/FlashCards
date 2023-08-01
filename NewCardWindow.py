import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel, QApplication

class NewCardMenu(QtWidgets.QDialog):
    def __init__(self):
        super(NewCardMenu, self).__init__()
        # self.ui = newCard.Ui_Dialog()
        # self.ui.setupUi(self)
        # self.setWindowTitle('Add Card')