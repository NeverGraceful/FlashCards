import sys, os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QPushButton, QLabel, QApplication
import start, PracticeWindow, NewClassWindow, CardWindow, CustomWindow, dataStructures

class StartMenu(QtWidgets.QDialog):
    def __init__(self):
        super(StartMenu, self).__init__()
        self.ui = start.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(539, 397)
        self.setWindowTitle('Flash Cards')
        self.setWindowIcon(QtGui.QIcon('logoflash.png'))
        self.ui.SHUFFLE_BUTT.clicked.connect(self.button_push)
        self.ui.ADD_CLASS_BUTT.clicked.connect(self.button_push)
        self.ui.ADD_CARD_BUTT.clicked.connect(self.button_push)
        self.ui.REMOVE_CARD_BUTT.clicked.connect(self.button_push)
        self.ui.CUSTOM_BUTT.clicked.connect(self.button_push)
        self.ui.START_BUTT.clicked.connect(self.button_push)
        self.ui.FRONT_FIRST.clicked.connect(self.button_push)
        self.ui.BACK_FIRST.clicked.connect(self.button_push)
        self.ui.FRONT_FIRST.setStyleSheet("background-color : #d1d1d1")
        dataStructures.fill_data_structures()
        self.classes = dataStructures.class_list
        self.cur_class = ""
        self.display_classes()

    def display_classes(self):
        self.ui.SCROLL_AREA = QtWidgets.QScrollArea(self)
        self.vbox = self.ui.SCROLL_WIDGET.layout()
        self.ui.SCROLL_AREA.setWidget(self.ui.SCROLL_WIDGET)
        for classes in self.classes:
            button = QPushButton(classes)
            button.setStyleSheet("background-color : white")
            button.clicked.connect(self.set_class)
            self.vbox.addWidget(button)
                
        self.ui.SCROLL_WIDGET.setLayout(self.vbox)

        self.ui.SCROLL_AREA.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ui.SCROLL_AREA.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ui.SCROLL_AREA.setWidgetResizable(True)
        self.ui.SCROLL_AREA.setGeometry(10, 70, 241, 241)

    def set_class(self):
        self.cur_class = self.sender().text()
        dataStructures.cur_class = self.sender().text()

    def button_push(self):
        name = self.sender()
        if name.text() == "New Card":
            print("New Card")
            win = CardWindow.NewCardMenu()
            win.exec_()
        
        elif name.text() == "Remove Card":
            print("Remove Card")
            win = CardWindow.RemoveCardMenu()
            win.exec_()

        elif name.text() == "New Class":
            print("New Class")
            win = NewClassWindow.NewClassMenu()
            win.exec_()

        elif name.text() == "Shuffle List":
            print("Shuffle")
            dataStructures.shuffle = 1

        elif name.text() == "Start Practice!":
            print("Start")
            if self.cur_class == "":
                self.ui.ERROR_LABEL.setText("Please select a class")
                return
            win = PracticeWindow.Practice()
            win.exec_()

        elif name.text() == "Front First":
            print("Front first")
            dataStructures.front_first = 1
            self.ui.FRONT_FIRST.setStyleSheet("background-color : white")
            self.ui.BACK_FIRST.setStyleSheet("background-color : #d1d1d1")

        elif name.text() == "Back First":
            print("Back first")
            dataStructures.front_first = 0
            self.ui.BACK_FIRST.setStyleSheet("background-color : white")
            self.ui.FRONT_FIRST.setStyleSheet("background-color : #d1d1d1")

        else:
            print("Custom List")
            win = CustomWindow.CustomizeListMenu()
            win.exec_()
    
        


    
def window():
    app = QApplication(sys.argv)
    win = StartMenu()
    win.show()
    sys.exit(app.exec_())

window()