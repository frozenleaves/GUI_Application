# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolTip, QVBoxLayout, QWidget
from PyQt5.QtGui import QPalette  # 调色板
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap  # 放置图片
from PyQt5.QtGui import QFont  # 设置提示信息需要设置字体


class LabelWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=#FF0000>这是一个标签</font>')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(palette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>置顶</a>")
        label2.setAlignment(Qt.AlignCenter)

        label4.setText("<a href='http://shiwen.frozenleaves.cn'>主页</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setOpenExternalLinks(True)

        label3.setPixmap(QPixmap('./images/01.jpg'))
        label3.setAlignment(Qt.AlignCenter)

        QToolTip.setFont(QFont('Monospaced', 12))
        label4.setToolTip('诗文主页')
        label3.setToolTip('图片')

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.label4 = label4
        self.label3.linkHovered.connect(self.linkHovered)
        self.label2.linkActivated.connect(self.linkActivated)

    def linkHovered(self):
        print('鼠标滑过')

    def linkActivated(self):
        print('单击标签')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LabelWindow()
    window.show()
    sys.exit(app.exec_())
