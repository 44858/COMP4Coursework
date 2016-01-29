#VIEW WIDGET
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from database_skeleton import *

class ViewWidget(QWidget):
	BackPushed2 = pyqtSignal()
	def __init__(self):
		super().__init__()
		##Creating Widgets
		self.viewProducts = QTableWidget()
		self.back2 = QPushButton("Back To Menu")
		#creating Layout
		self.layout = QVBoxLayout()
		##adding widgets to layout
		self.layout.addWidget(self.viewProducts)
		self.layout.addWidget(self.back2)
		self.setLayout(self.layout)
		##button presses
		self.back2.clicked.connect(self.back2_pushed)
	def back2_pushed(self):
		self.BackPushed2.emit()

	def populateTable(self):
		products = g_database.GetAllProducts()
		self.viewProducts.clear() #clears table of all current items
		self.viewProducts.setRowCount(len(products))
		self.viewProducts.setColumnCount(6)
		for row in range(len(products)):
			for column in range(len(products[row])):
				 self.viewProducts.setItem(row, column, QTableWidgetItem(str(products[row][column])))