import sys, os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QPushButton, QLabel, QApplication
import start, PracticeWindow, NewClassWindow, NewCardWindow, CustomWindow, dataStructures

class StartMenu(QtWidgets.QDialog):
    def __init__(self):
        super(StartMenu, self).__init__()
        self.ui = start.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Flash Cards')
        self.setWindowIcon(QtGui.QIcon('logoflash.png'))
        self.ui.SHUFFLE_BUTT.clicked.connect(self.button_push)
        self.ui.ADD_CLASS_BUTT.clicked.connect(self.button_push)
        self.ui.ADD_CARD_BUTT.clicked.connect(self.button_push)
        self.ui.CUSTOM_BUTT.clicked.connect(self.button_push)
        self.ui.START_BUTT.clicked.connect(self.button_push)
        dataStructures.fill_data_structures()
        self.classes = dataStructures.class_list
        self.display_classes()

    def display_classes(self):
        self.ui.SCROLL_AREA = QtWidgets.QScrollArea(self)
        self.vbox = QtWidgets.QGridLayout(self.ui.SCROLL_WIDGET)
        self.ui.SCROLL_AREA.setWidget(self.ui.SCROLL_WIDGET)

        for classes in self.classes:
            button = QPushButton(classes)
            button.clicked.connect(self.set_class)
            self.SCROLL_AREA.addWidget(button)
                
        self.ui.SCROLL_WIDGET.setLayout(self.vbox)

        self.ui.SCROLL_AREA.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ui.SCROLL_AREA.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ui.SCROLL_AREA.setWidgetResizable(True)
        self.ui.SCROLL_AREA.setGeometry(10, 70, 241, 241)

    def set_class(self):
        self.cur_class = self.sender().text()

    def button_push(self):
        name = self.sender()
        if name.text() == "New Card":
            print("New Card")
            NewCardWindow.NewCardMenu()

        elif name.text() == "New Class":
            print("New Class")
            NewClassWindow.NewClassMenu()

        elif name.text() == "Shuffle List":
            print("Shuffle")

        elif name.text() == "Start Practice!":
            print("Start")
            PracticeWindow.Practice()

        else:
            print("Custom List")
            CustomWindow.CustomizeListMenu()

    
def window():
    app = QApplication(sys.argv)
    win = StartMenu()
    win.show()
    sys.exit(app.exec_())

window()