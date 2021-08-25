#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例6：窗口居中
ZetCode PyQt5 tutorial 

This program centers a window 
on the screen. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')    
        self.show()


    def center(self):

        qr = self.frameGeometry()

        #这一句获得主窗口所在的框架，其中QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小。
        cp = QDesktopWidget().availableGeometry().center()


        #获取显示器的分辨率，然后得到屏幕中间点的位置。
        qr.moveCenter(cp)

        #通过move函数把主窗口的左上角移动到其框架的左上角，实现窗口居中
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())