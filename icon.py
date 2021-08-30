#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例2  带图标窗口
ZetCode PyQt5 tutorial 

This example shows an icon
in the titlebar of the window.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        #使用initUI()方法创建一个GUI(图形用户界面 Graphical User Interface)。


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('icon.png'))   
        '''
        三个方法都继承自QWidget类。
        setGeometry()有两个作用：
        把窗口放到屏幕上并且设置窗口大小。参数分别代表屏幕坐标的x、y和窗口大小的宽、高。
        也就是说这个方法是resize()和move()的合体。
        setWindowTitle('Icon')为窗口添加了一个在标题栏展示文字'Icon'的标题
        最后一个方法是添加了图标。先创建一个QIcon对象，然后接受一个路径作为参数显示图标。
        '''     

        self.show()
        #让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。


if __name__ == '__main__':

    MyApplication = QApplication(sys.argv) #创建应用对象，名称无所谓，后续操作相同即可
    ex = Example()
    sys.exit(MyApplication.exec_())         #销毁主控件