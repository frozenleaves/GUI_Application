# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import MainWindow

# 窗口比例
scale = 0.5
size = (int(1920 * scale), int(1080 * scale))
app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = MainWindow.Ui_MainWindow()

ui.setupUi(mainWindow)
mainWindow.setWindowTitle('设计窗口UI')
mainWindow.resize(*size)

mainWindow.show()
sys.exit(app.exec_())
