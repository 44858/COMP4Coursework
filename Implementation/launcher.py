#Launcher

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from main_program import *

if __name__ == "__main__":
    stock_window = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    stock_window.exec_()
