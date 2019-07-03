# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from 控件关联 import Ui_MainWindow as kmw


app = QApplication(sys.argv)
window = QMainWindow()
ui = kmw()

ui.setupUi(window)

window.setWindowTitle('控件关联')
window.resize(int(1920*0.6), int(1080*0.6))

window.show()

sys.exit(app.exec_())