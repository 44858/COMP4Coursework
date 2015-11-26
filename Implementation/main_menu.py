# MAIN MENU
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MenuWidget(QWidget):
	AddPushed = pyqtSignal()
	def __init__(self):
		super().__init__()
		self.addProduct = QPushButton("Add New Product")
		self.deleteProduct = QPushButton("Delete Product")
		self.viewProduct = QPushButton("View all Products")
		self.exit = QPushButton("Exit Program")
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.addProduct)
		self.layout.addWidget(self.deleteProduct)
		self.layout.addWidget(self.viewProduct)
		self.layout.addWidget(self.exit)
		self.setLayout(self.layout)
		
		self.addProduct.clicked.connect(self.add_pushed)
	
	def add_pushed(self):
		self.AddPushed.emit()