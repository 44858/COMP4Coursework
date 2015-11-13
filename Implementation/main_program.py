#MAIN PROGRAM
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from main_menu import *

class MainWindow(QMainWindow):
	""""Creates MainWindow"""
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Main Menu")
		self.main_menu = MenuWidget()
		self.setCentralWidget(self.main_menu)
		


def main():
	stock_window = QApplication(sys.argv)
	main_window = MainWindow()
	main_window.show()
	main_window.raise_()
	stock_window.exec_()

if __name__ == "__main__":
	main()
