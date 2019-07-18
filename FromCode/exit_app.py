# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget
from PyQt5 import QtCore


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('退出应用程序')
        self.resize(800, 600)

        # 添加一个按钮
        self.button1 = QPushButton('quit')

        # 按钮关联自定义的槽
        self.button1.clicked.connect(self.onClickButton)

        # 添加水平布局
        layout = QHBoxLayout()

        # 放置按钮组件
        layout.addWidget(self.button1)

        # 添加组件主框架
        mainFrame = QWidget()

        # 将布局设置在主框架上
        mainFrame.setLayout(layout)

        # 将注框架放置在屏幕上
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
