#MAIN PROGRAM
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from main_menu import *
from add_widget import *

class MainWindow(QMainWindow):
        """"Creates MainWindow"""
        def __init__(self):
         super().__init__()
         self.setWindowTitle("Stock Database")
         self.main_menu = MenuWidget()
         self.add_widget = AddWidget()
         self.setCentralWidget(self.main_menu)
         self.main_menu.AddPushed.connect(self.add_pressed)
         ##Create Stacked Layout
         self.stack = QStackedLayout()
         self.stack.addWidget(self.main_menu)
         self.stack.addWidget(self.add_widget)
         self.widget = QWidget()
         self.widget.setLayout(self.stack)
         self.setCentralWidget(self.widget)
                
        def add_pressed(self):
                self.stack.setCurrentIndex(1)
                
        


       

if __name__ == "__main__":
        main()
