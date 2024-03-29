# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import 混合布局 as hb

scale = 0.6
size = (int(1920 * scale), int(1080 * scale))

app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = hb.Ui_MainWindow()

ui.setupUi(mainWindow)
mainWindow.resize(*size)
mainWindow.setWindowTitle('混合布局')

mainWindow.show()
sys.exit(app.exec_())
