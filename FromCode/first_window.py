# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # 设置窗口标题
        self.setWindowTitle('第一个主窗口')

        # 设置窗口大小
        self.resize(800, 600)

        # 获取状态栏
        self.status = self.statusBar()

        # 设置状态栏信息，显示5秒后关闭
        self.status.showMessage('消息显示五秒，之后消失', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 设置应用图标
    app.setWindowIcon(QIcon('./images/枫叶.png'))

    window = MainWindow()

    window.show()

    sys.exit(app.exec_())