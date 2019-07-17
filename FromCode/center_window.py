# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # 设置窗口标题
        self.setWindowTitle('第一个主窗口')

        # 设置窗口大小
        self.resize(800, 600)

    def center(self):
        """设置窗口居中"""

        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()

        # 获取窗口坐标
        size = self.geometry()

        new_width = (screen.width() - size.width()) / 2
        new_height = (screen.height() - size.height()) / 2

        self.move(new_width, new_height)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec_())
