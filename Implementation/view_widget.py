#VIEW WIDGET
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class ViewWidget(QWidget):
	BackPushed2 = pyqtSignal()
	def __init__(self):
		super().__init__()
		self.viewProducts = QTableView()
		self.back2 = QPushButton("Back To Menu")

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.viewProducts)
		self.layout.addWidget(self.back2)
		self.setLayout(self.layout)

		self.back2.clicked.connect(self.back2_pushed)
	def back2_pushed(self):
		self.BackPushed2.emit()
