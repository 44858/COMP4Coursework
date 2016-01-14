# MAIN MENU
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MenuWidget(QWidget):
	AddPushed = pyqtSignal()
	EditPushed = pyqtSignal()
	ViewPushed = pyqtSignal()
	ExitPushed = pyqtSignal()
	def __init__(self):
		super().__init__()
		self.addProduct = QPushButton("Add New Product")
		self.editProduct = QPushButton("Edit Products")
		self.viewProduct = QPushButton("View all Products")
		self.exit = QPushButton("Exit Program")
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.addProduct)
		self.layout.addWidget(self.editProduct)
		self.layout.addWidget(self.viewProduct)
		self.layout.addWidget(self.exit)
		self.setLayout(self.layout)
		self.exit.clicked.connect(self.exit_pushed)
		self.addProduct.clicked.connect(self.add_pushed)
		self.viewProduct.clicked.connect(self.view_products)
		self.editProduct.clicked.connect(self.edit_products)
	
	def add_pushed(self):
		self.AddPushed.emit()

	def exit_pushed(self):
		self.ExitPushed.emit()

	def edit_products(self):
		self.EditPushed
	def view_products(self):
		self.ViewPushed.emit()