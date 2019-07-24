# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *


class BuddyWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.setWindowTitle('伙伴关系')
        self.resize(400, 200)
        user_Label = QLabel('&user name', self)
        password_label = QLabel('&password', self)
        user_input = QLineEdit(self)
        password_input = QLineEdit(self)
        OKPushButton = QPushButton('&OK', self)
        CancelPushButton = QPushButton('&Cancel', self)

        user_Label.setBuddy(user_input)
        password_label.setBuddy(password_input)

        layout = QGridLayout(self)
        layout.addWidget(user_Label, 0, 0, 1, 2)
        layout.addWidget(user_input, 0, 1, 1, 3)
        layout.addWidget(password_label, 1, 0, 1, 2)
        layout.addWidget(password_input, 1, 1, 1, 3)
        layout.addWidget(OKPushButton, 2, 2)
        layout.addWidget(CancelPushButton, 2, 3)

        OKPushButton.clicked.connect(self.ok_event)
        CancelPushButton.clicked.connect(self.close_event)

    def ok_event(self):
        print('OK')

    def close_event(self):
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BuddyWindow()
    window.show()
    sys.exit(app.exec_())
