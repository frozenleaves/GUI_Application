# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.init()

    def init(self):
        # 设置窗口标题
        self.setWindowTitle('设置窗口图标')

        # 设置窗口大小
        self.resize(800, 600)

        self.setWindowIcon(QIcon('./images/枫叶.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 设置应用图标
    # app.setWindowIcon(QIcon('./images/枫叶.png'))

    window = MainWindow()

    window.show()

    sys.exit(app.exec_())