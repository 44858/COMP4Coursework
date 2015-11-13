# MAIN MENU
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MenuWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.addProduct = QPushButton("Add New Product")
		self.deleteProduct = QPushButton("Delete Product")
		self.searchProduct = QPushButton("Search For Product")
		self.exit = QPushButton("Exit Program")
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.addProduct)
		self.layout.addWidget(self.deleteProduct)
		self.layout.addWidget(self.searchProduct)
		self.layout.addWidget(self.exit)
		self.setLayout(self.layout)