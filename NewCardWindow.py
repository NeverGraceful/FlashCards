import sys, os, re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel, QApplication
import newCard, dataStructures

class NewCardMenu(QtWidgets.QDialog):
    def __init__(self):
        super(NewCardMenu, self).__init__()
        self.ui = newCard.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Add Card')
        self.setFixedSize(400, 387)
        self.ui.CLASS_COMBO.addItems(dataStructures.class_list)
        self.ui.SUBMIT_BUTT.clicked.connect(self.submitted)
    
    def submitted(self):
        print("save new card")
        wanted_path = os.path.join(dataStructures.find_path(),'Classes\\' + self.ui.CLASS_COMBO.currentText() + ".txt")
        with open(wanted_path, 'a') as info_file:
            info_file.write(self.ui.ENTER_FRONT.toPlainText() + " " + self.ui.ENTER_BACK.toPlainText() + " ")
            info_file.close()

    def find_path():
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
           application_path = os.path.dirname(os.path.abspath(__file__))

        return application_path