import sys, os, random
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QPushButton, QLabel, QApplication
import practice, dataStructures

class Practice(QtWidgets.QDialog):
    def __init__(self):
        super(Practice, self).__init__()
        self.ui = practice.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(724, 465)
        self.setWindowTitle('Practice')
        self.setWindowIcon(QtGui.QIcon('logoflash.png'))
        self.fill_flash_list()
        self.ui.HINT_LABEL.setGeometry(300, 400, 0, 0)
        self.ui.HINT_BUTT.clicked.connect(self.show_hint)
        self.ui.NEXT_BUTT.clicked.connect(self.next_card)
        self.ui.PREV_BUTT.clicked.connect(self.prev_card)
        self.ui.FLIP_BUTT.clicked.connect(self.flip)
        self.cur_card_index = 0
        self.cur_side = 0
        self.front_first = dataStructures.front_first
        self.display_card()
    
    def flip(self):
        print("flip")
        if self.cur_side == 0:
            print("here")
            self.cur_side = 1
        else:
            print("there")
            self.cur_side = 0
        print("flipped to " + str(self.cur_side))
        self.display_card()
    
    def show_hint(self):
        print("show hint")
        self.ui.HINT_LABEL.setGeometry(200, 380, 321, 71)
        self.ui.HINT_LABEL.setText(self.hint_list[self.cur_card_index])
    
    def next_card(self):
        print("next card")
        self.ui.HINT_LABEL.setGeometry(300, 400, 0, 0)
        if self.cur_card_index >= len(self.front_list):
            return
        self.cur_card_index = self.cur_card_index + 1
        self.cur_side == 0
        self.display_card()

    def prev_card(self):
        print("prev card")
        self.ui.HINT_LABEL.setGeometry(300, 400, 0, 0)
        if self.cur_card_index <= 0:
            return
        self.cur_card_index = self.cur_card_index - 1
        self.cur_side == 0
        self.display_card()

    def display_card(self):
        if self.cur_side == 0:
            print("cur_side 0")
            self.ui.MAIN_LABEL.setText(self.front_list[self.cur_card_index])
        else:
            print("cur_side 1")
            self.ui.MAIN_LABEL.setText(self.back_list[self.cur_card_index])

    def fill_flash_list(self):
        print("fill flash")
        wanted_path = os.path.join(dataStructures.find_path(), 'Classes\\' + dataStructures.cur_class +".txt")
        with open(wanted_path) as info_file:
            index = 0
            self.front_list = []
            self.back_list = []
            self.hint_list = []
            for line in info_file:
                card_list = line.split() 
                for i in card_list:
                    if index % 3 == 0:
                        self.front_list.append(i)
                    elif index % 3 == 1:
                        self.back_list.append(i)
                    else:
                        self.hint_list.append(i)
                    index = index + 1
                if dataStructures.shuffle == 1:
                    temp = list(zip(self.front_list, self.back_list, self.hint_list))
                    random.shuffle(temp)
                    res1, res2, res3 = zip(*temp)
                    self.front_list, self.back_list, self.hint_list = list(res1), list(res2), list(res3)   
                print(self.hint_list) 
            info_file.close()
