# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from signal_slot import Ui_MainWindow

app = QApplication(sys.argv)
mainWindow = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(mainWindow)

mainWindow.setWindowTitle('信号与槽')
mainWindow.show()

sys.exit(app.exec_())
