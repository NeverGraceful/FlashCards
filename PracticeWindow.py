import sys, os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QPushButton, QLabel, QApplication
import practice

class Practice(QtWidgets.QDialog):
    def __init__(self):
        super(Practice, self).__init__()
        self.ui = practice.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(724, 465)
        self.setWindowTitle('Practice')
        self.setWindowIcon(QtGui.QIcon('logoflash.png'))
        self.ui.HINT_LABEL.setGeometry(300, 400, 0, 0)
        self.ui.HINT_BUTT.clicked.connect(self.show_hint)
        self.ui.NEXT_BUTT.clicked.connect(self.next_card)
    
    def show_hint(self):
        print("show hint")
        self.ui.HINT_LABEL.setGeometry(200, 380, 321, 71)
    
    def next_card(self):
        print("next card")
        self.ui.HINT_LABEL.setGeometry(300, 400, 0, 0)