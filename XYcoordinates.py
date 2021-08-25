#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：事件对象
ZetCode PyQt5 tutorial 

In this example, we display the x and y 
coordinates of a mouse pointer in a label widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)
        #在一个组件里显示鼠标的X和Y坐标。

        self.label = QLabel('self.text', self)
        '''
        PySide2.QtWidgets.QLabel(text[, parent=None[, f=Qt.WindowFlags()]])
        QLabel用于显示文本或图像。没有提供用户交互功能
        Constructs a label that displays the text.
        The parent and widget flag f , arguments are passed to the QFrame constructor.
        构建一个显示文本的标签，参数中父级和控件标志f会被传递给QFrame构造函数
        '''
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)
        #事件追踪默认没有开启，当开启后才会追踪鼠标的点击事件

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()


    def mouseMoveEvent(self, e):
        '''
        官方文档中的解释仅一句：Override this to handle mouse move events. 覆盖此操作以处理鼠标移动事件
        这里的参数e为事件对象。里面有我们触发事件（鼠标移动）的事件对象。
        下面的x()和y()方法可以得到鼠标在窗口中此刻的x和y坐标点，然后拼成字符串输出到QLabel组件里
        '''
        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)

        self.label.setText(text)
        '''
        注意qtcy中以很多个setText函数，这里是：PySide2.QtWidgets.QLabel.setText(arg__1)
        Parameters: arg__1 – str
        
        '''


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())