#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例1：状态栏
ZetCode PyQt5 tutorial 

This program creates a statusbar.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

#状态栏由QMainWindow创建
class Example(QMainWindow):

    def __init__(self):
        #super() 函数是用于调用父类(超类)的一个方法。super ().__init__ ()，就是继承父类的init方法
        super().__init__()

        self.initUI()


    def initUI(self):               

        self.statusBar().showMessage('Ready')
        '''
        调用QtGui.QMainWindow类的statusBar()方法，创建状态栏。
        第一次调用会创建一个状态栏，而再次调用会返回一个状态栏对象。showMessage()方法在状态栏上显示一条信息。
        '''
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())