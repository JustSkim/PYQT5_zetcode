#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：拖放
ZetCode PyQt5 tutorial

This is a simple drag and
drop example. 

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QPushButton, QWidget, 
    QLineEdit, QApplication)
import sys

class Button(QPushButton):
    #用QPushButton上构造一个按钮实例
    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)
        '''
        激活组件的拖拽事件
        '''


    def dragEnterEvent(self, e):
        '''
        重构了dragEnterEvent()方法。设定好接受拖拽的数据类型（plain text）
        '''
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore() 

    def dropEvent(self, e):
        #重构dropEvent()方法，更改按钮接受鼠标的释放事件的默认行为。
        self.setText(e.mimeData().text()) 


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        edit = QLineEdit('line-edit', self)
        '''
        QLineEdit默认支持拖拽操作，所以我们只要调用setDragEnabled()方法使用就行了。
        '''
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()