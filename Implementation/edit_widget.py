#EDIT PRODUCTS
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class EditWidget(QWidget):
	def __init__(self):
		super().__init__()
		#create widgets
		self.title = QLabel("Please choose a product to edit: ")
		self.chooseProduct = QComboBox()
		

