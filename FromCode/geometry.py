# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


def on_click():
    print('%s 被点击' % button.text())
    # 窗口横纵坐标
    print('window.x:', window.x(), 'window.y:', window.y())

    # 工作区宽高
    print('window.width: ', window.width(), 'window.height: ', window.height())

    # 工作区横纵坐标
    print('window.geometry.x: ', window.geometry().x(), 'window.geometry.y: ', window.geometry().y())

    # 工作区宽高
    print('window.geometry.width: ', window.geometry().width(), 'window.geometry.height: ', window.geometry().height())

    # 窗口横纵坐标
    print(window.frameGeometry().x(), window.frameGeometry().y())

    # 窗口宽高
    print(window.frameGeometry().width(), window.frameGeometry().y())


app = QApplication(sys.argv)
window = QWidget()
button = QPushButton(window)
button.clicked.connect(on_click)
button.setText('点击')
window.resize(800, 600)
window.setWindowTitle('窗体坐标系')

b_height = button.geometry().height()
b_width = button.geometry().width()
w_height = window.geometry().height()
w_width = window.geometry().width()

button.move((w_width - b_width) / 2, (w_height - b_height) / 2)

window.show()
sys.exit(app.exec_())
