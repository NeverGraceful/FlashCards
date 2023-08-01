import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel, QApplication

class NewClassMenu(QtWidgets.QDialog):
    def __init__(self):
        super(NewClassMenu, self).__init__()
        # self.ui = newClass.Ui_Dialog()
        # self.ui.setupUi(self)
        # self.setWindowTitle('Add Class')