#VIEW WIDGET
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from database_skeleton import *

class ViewWidget(QWidget):
	BackPushed2 = pyqtSignal()
	def __init__(self):
		super().__init__()
		self.viewProducts = QTableWidget()
		self.back2 = QPushButton("Back To Menu")

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.viewProducts)
		self.layout.addWidget(self.back2)
		self.setLayout(self.layout)

		self.back2.clicked.connect(self.back2_pushed)
		self.populateTable()
	def back2_pushed(self):
		self.BackPushed2.emit()

	def populateTable(self):
		self.viewProducts.setColumnCount(6)
		self.viewProducts.setRowCount(6)

		products = g_database.GetAllProducts()

		# self.viewProducts.setItem(0,0,QTableWidgetItem("Hello"))
		for row in range(len(products)):
			for column in range(len(products[row])):
				 self.viewProducts.setItem(row, column, QTableWidgetItem(str(products[row][column])))


		# model = QStandardItemModel()
		# row = 0
		# products = g_database.GetAllProducts()
		# print(products)
		# for product in products:
		# 	product_list = [] 
		# 	for column in range(2):
		# 		item = QStandardItem("{0},{1}".format(product, column))
		# 		product_list.append(item)
		# 		row+=1
		# 	model.appendRow(product_list)

		#model.setItem(5,5, QStandardItem)
		#self.viewProducts.setModel(model)
