# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from menu import Ui_MainWindow

app = QApplication(sys.argv)
mainWindow = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(mainWindow)

mainWindow.setWindowTitle('菜单和工具栏')
mainWindow.show()

sys.exit(app.exec_())
