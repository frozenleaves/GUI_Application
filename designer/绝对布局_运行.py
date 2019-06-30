# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import 绝对布局 as jb

scale = 0.6
size = (int(1920 * scale), int(1080 * scale))

app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = jb.Ui_MainWindow()

ui.setupUi(mainWindow)
mainWindow.resize(*size)
mainWindow.setWindowTitle('绝对布局')

mainWindow.show()
sys.exit(app.exec_())
