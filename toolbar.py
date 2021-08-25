#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：工具栏
ZetCode PyQt5 tutorial 

This program creates a toolbar.
The toolbar has one action, which
terminates the application, if triggered.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        exitAct = QAction(icon=QIcon('exit24.png'), text='Exittttt', parent=self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        #行为被触发的时候，会调用QtGui.QMainWindow的quit方法退出应用

        self.toolbar = self.addToolBar('Exit')#addToolBar()创建工具栏
        #‘Exit’不会显示在工具栏中，当鼠标移至该图标时，会显示文字‘Exittttt’而非‘Exit’

        self.toolbar.addAction(exitAct) #将动作添加到工具栏
        

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())