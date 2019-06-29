# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)
window = QWidget()

window.resize(600, 300)

window.show()

sys.exit(app.exec_())