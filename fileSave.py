#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：文件保存
ZetCode PyQt5 tutorial 

In this example, we select a file with a
QFileDialog and display its contents
in a QTextEdit.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):
    '''
    设置了一个文本编辑框，文本编辑框是基于QMainWindow组件的。

    本例中有一个菜单栏，一个置中的文本编辑框，一个状态栏。点击菜单栏选项会弹出一个QtGui.QFileDialog对话框，
    在这个对话框里，你能选择文件，然后文件的内容就会显示在文本编辑框里。
    '''
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        '''
        弹出QFileDialog窗口。getOpenFileName()方法的第一个参数是说明文字，
        第二个参数是默认打开的文件夹路径。默认情况下显示所有类型的文件。
        '''

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)    
        '''
        读取选中的文件，并显示在文本编辑框内
        注意只能读取二进制文件，如txt，html等
        （但是打开HTML文件时，是渲染后的结果）
        打开pdf,png格式图片时候，会报错如下：
        UnicodeDecodeError: 'gbk' codec can't decode byte 0x89 in position 24: illegal multibyte sequence
        '''    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())