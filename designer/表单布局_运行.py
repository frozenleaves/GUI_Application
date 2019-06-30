# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import 表单布局 as bb

scale = 0.6
size = (int(1920 * scale), int(1080 * scale))

app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = bb.Ui_MainWindow()

ui.setupUi(mainWindow)
mainWindow.resize(*size)
mainWindow.setWindowTitle('表单布局')

mainWindow.show()
sys.exit(app.exec_())
