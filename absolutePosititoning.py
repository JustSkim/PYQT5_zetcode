#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：绝对定位
ZetCode PyQt5 tutorial 

This example shows three labels on a window
using absolute positioning. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        '''
        QLabel小部件提供文本或图像显示，没有交互功能！
        '''
        lbl1 = QLabel(text='Zetcode', parent=self)
        lbl1.move(15, 10)       #使用move方法定位元素(也就是这个label部件)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)        

        self.setGeometry(400, 400, 500, 250)
        '''
        setGeometry()有两个作用：
        把窗口放到屏幕上；设置窗口大小。
        四个参数分别代表屏幕坐标的x、y和窗口大小的宽、高。
        这个方法是resize()和move()的合体。
        '''

        self.setWindowTitle('Absolute') #为窗口添加了一个在标题栏展示的标题   
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())