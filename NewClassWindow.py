import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel, QApplication
import newClass, dataStructures

class NewClassMenu(QtWidgets.QDialog):
    def __init__(self):
        super(NewClassMenu, self).__init__()
        self.ui = newClass.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Add Class')
        self.setFixedSize(400, 173)
        self.ui.ADD_BUTT.clicked.connect(self.add_class)

    def add_class(self):
        entry = self.ui.ENTER_CLASS.toPlainText()
        if entry.isspace() or not entry.isalpha():
            self.ui.ERROR_LABEL.setText("INVALID CLASS NAME")
            return
        elif entry in dataStructures.class_list:
            self.ui.ERROR_LABEL.setText("CLASS ALREADY EXISTS")
            return
        self.ui.ERROR_LABEL.setText(" ")
        dataStructures.class_list.append(entry)
        dataStructures.save_data()
        wanted_path = os.path.join(dataStructures.find_path(),'Classes\\' + entry + ".txt")
        f = open(wanted_path, 'x')
