#EDIT PRODUCTS
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from database_skeleton import *
class EditWidget(QWidget):
	BackPushed3 = pyqtSignal()
	def __init__(self):
		super().__init__()
		#create widgets
		self.title = QLabel("Please choose a product to edit: ")
		self.chooseProduct = QComboBox()
		self.GetProducts()
		##Creating Line edits and labels and button
		self.product_name = QLineEdit()
		self.label1 = QLabel("Product Name: ")
		self.brand = QLineEdit()
		self.label3 = QLabel("Brand: ")
		self.model = QLineEdit()
		self.label4 = QLabel("Model: ")
		self.quantity = QLineEdit()
		self.label5 = QLabel("Quantity: ")
		self.price = QLineEdit()
		self.label6 = QLabel("Price: ")
		self.submit = QPushButton("Submit Product")
		self.back = QPushButton("Back To Menu")
		#creating layout
		self.layout = QVBoxLayout()
		##Adding widgets to layout
		self.layout.addWidget(self.title)
		self.layout.addWidget(self.chooseProduct)
		self.layout.addWidget(self.label1)
		self.layout.addWidget(self.product_name)
		self.layout.addWidget(self.label3)
		self.layout.addWidget(self.brand)
		self.layout.addWidget(self.label4)
		self.layout.addWidget(self.model)
		self.layout.addWidget(self.label5)
		self.layout.addWidget(self.quantity)
		self.layout.addWidget(self.label6)
		self.layout.addWidget(self.price)
		self.layout.addWidget(self.submit)
		self.layout.addWidget(self.back)
		self.setLayout(self.layout)
		self.back.clicked.connect(self.BackPressed3)
		self.submit.clicked.connect(self.SubmitPressed)

	def GetProducts(self):
		self.chooseProduct.clear()
		database = Database()
		products = database.GetProductList()
		for product in products:
			self.chooseProduct.addItem(product[0])

	def BackPressed3(self):
		self.BackPushed3.emit()
	def SubmitPressed(self):
		g_database.EditProduct(self.product_name.text(), self.brand.text(), self.model.text(), self.quantity.text(), self.price.text())
		self.BackPushed3.emit()