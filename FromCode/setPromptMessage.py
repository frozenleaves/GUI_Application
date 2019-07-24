# -*- coding: utf-8 -*-

import time
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton,QHBoxLayout, QMainWindow
from PyQt5.QtWidgets import QToolTip    # 设置提示信息的模块
from PyQt5.QtGui import QFont           # 设置提示信息需要设置字体


class MessageWindow(QMainWindow):

    def __init__(self):
        super(MessageWindow, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Monospaced', 12))
        self.setToolTip('<b>现在是%s</b>' % time.ctime())

        self.setWindowTitle('设置提示信息')

        self.resize(800, 600)

        self.button = QPushButton('close')

        layout = QHBoxLayout()
        layout.addWidget(self.button)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

        self.button.setToolTip('<b><font color=red>关闭应用程序</font></b>')

        self.button.clicked.connect(self.closed)

    def closed(self):
        sender = self.sender()
        print(sender.text())
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MessageWindow()
    window.show()
    sys.exit(app.exec_())