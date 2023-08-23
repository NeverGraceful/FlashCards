import sys, os, re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel, QApplication
import newCard, removeCard, dataStructures

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
            hint = self.ui.ENTER_HINT.toPlainText()
            if len(hint) <= 0:
                hint = "N/A"
            info_file.write(self.ui.ENTER_FRONT.toPlainText() + ":" + self.ui.ENTER_BACK.toPlainText() + ":" + hint +":")
            info_file.close()

class RemoveCardMenu(QtWidgets.QDialog):
    def __init__(self):
        super(RemoveCardMenu, self).__init__()
        self.ui = removeCard.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Remove Card')
        self.setFixedSize(400, 129)
        self.ui.CLASS_COMBO.addItems(dataStructures.class_list)
        self.ui.SELECT_CLASS_BUTT.clicked.connect(self.select_class)
        self.ui.SUBMIT_BUTT.clicked.connect(self.submitted)

    def select_class(self):
        dataStructures.cur_class = self.ui.CLASS_COMBO.currentText()
        dataStructures.fill_flash_list()
        self.ui.CARD_COMBO.addItems(dataStructures.front_list)
    
    def submitted(self):
        print("remove card")
        index = dataStructures.front_list.index(self.ui.CARD_COMBO.currentText())
        dataStructures.front_list.pop(index)
        dataStructures.back_list.pop(index)
        dataStructures.hint_list.pop(index)

