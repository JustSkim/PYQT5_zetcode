#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：图片处理
ZetCode PyQt5 tutorial 

In this example, we dispay an image
on the window. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("exit.png")
        #创建一个QPixmap对象，接收一个文件作为参数。
        '''
        QPixmap类用于绘图设备的图像显示，它可以作为一个QPainterDevice对象，也可以加载到一个控件中，通常是标签或者按钮，用于在标签或按钮上显示图像
QPixmap可以读取的图像文件类型有BMP，GIF，JPG等
        '''

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        '''
        把QPixmap实例放到QLabel组件里。
        注意，组件大小 必须大于等于 QPixmap这个控件大小（也即图片大小）
        PySide2.QtWidgets.QLabel.setPixmap(arg__1)¶
        Parameters
        arg__1 – PySide2.QtGui.QPixmap
        This property holds the label’s pixmap..
        Previously, Qt provided a version of pixmap() which returned the pixmap by-pointer. That version is now deprecated. To maintain compatibility with old code, you can explicitly differentiate between the by-pointer function and the by-value function:
        '''

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())