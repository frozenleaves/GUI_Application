# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget
from PyQt5 import QtCore


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('退出应用程序')
        self.resize(800, 600)

        self.button1 = QPushButton('quit')
        # self.button1.setGeometry(QtCore.QRect(610, 470, 93, 28))
        self.button1.clicked.connect(self.onClickButton)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onClickButton(self):
        sender = self.sender()
        print(sender.text())
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec_())
