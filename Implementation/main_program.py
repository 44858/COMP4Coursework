#MAIN PROGRAM
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from main_menu import *
from add_widget import *
from view_widget import *
from edit_widget import *

class MainWindow(QMainWindow):
        """"Creates MainWindow"""
        def __init__(self):
         super().__init__()
         self.setWindowTitle("Stock Database")
         self.main_menu = MenuWidget()
         self.add_widget = AddWidget()
         self.view_widget = ViewWidget()
         self.edit_widget = EditWidget()
         self.setCentralWidget(self.main_menu)
         ##Create Stacked Layout
         self.stack = QStackedLayout()
         self.stack.addWidget(self.main_menu)
         self.stack.addWidget(self.add_widget)
         self.stack.addWidget(self.view_widget)
         self.stack.addWidget(self.edit_widget)
         self.widget = QWidget()
         self.widget.setLayout(self.stack)
         self.setCentralWidget(self.widget)
         ##button presses
         self.add_widget.BackPushed1.connect(self.back_pressed1)
         self.main_menu.ViewPushed.connect(self.view_pressed)
         self.main_menu.EditPushed.connect(self.edit_pressed)
         self.main_menu.AddPushed.connect(self.add_pressed)
         self.main_menu.ExitPushed.connect(self.exit_pressed)
         self.view_widget.BackPushed2.connect(self.back_pushed2)
         self.edit_widget.BackPushed3.connect(self.back_pushed3)

        def add_pressed(self):
                self.stack.setCurrentIndex(1)
        def view_pressed(self):
                self.view_widget.populateTable()#calls the populate table function from view_widget
                self.stack.setCurrentIndex(2)
        def back_pressed1(self):
                self.stack.setCurrentIndex(0)
        def edit_pressed(self):
                self.stack.setCurrentIndex(3)
        def back_pushed2(self):
                self.stack.setCurrentIndex(0)
        def back_pushed3(self):
                self.stack.setCurrentIndex(0)
        def exit_pressed(self):
                self.close() #closes the program

        