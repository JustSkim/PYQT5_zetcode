#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：主窗口
ZetCode PyQt5 tutorial 

This program creates a skeleton of
a classic GUI application with a menubar,
toolbar, statusbar, and a central widget. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        '''
        创建了一个文本编辑区域，并把它放在QMainWindow的中间区域，这个组件会占满所有剩余的区域。
        '''

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        #当鼠标移至工具栏中的该图标时，会显示这里的文字‘Exit’

        exitAct.setShortcut('Ctrl+Q')       #设置该动作的相关快捷键
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()    #创建一个状态栏

        menubar = self.menuBar()    #创建一个菜单栏
        fileMenu = menubar.addMenu('&File') #这里的符号'&'不会在菜单栏选项中显示出来
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')  #addToolBar()创建工具栏
        toolbar.addAction(exitAct)         #工具栏添加一个选项

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())