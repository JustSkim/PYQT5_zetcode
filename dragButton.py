#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：拖放按钮组件  注意是右键拖拽！！！
ZetCode PyQt5 tutorial

In this program, we can press on a button with a left mouse
click or drag and drop the button with  the right mouse click. 

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017

例子中，窗口上有一个QPushButton组件。
左键点击按钮，控制台就会输出press。右键可以点击然后拖动按钮。
"""

from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys

class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)
    '''
    从QPushButton继承一个Button类，然后重构QPushButton的两个方法: mouseMoveEvent()和mousePressEvent().
    mouseMoveEvent()是拖拽开始的事件。
    mousePressEvent()是鼠标给予压力的事件，分鼠标左键、右键、滚轮、前进键、后退键（不包含dpi键）
    '''

    def mouseMoveEvent(self, e):
        #这里只劫持按钮的右键事件（Qt.RightButton），左键的操作还是默认行为
        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        '''
        创建一个QDrag对象，用来传输MIME-based数据。
        '''
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)


    def mousePressEvent(self, e):

        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('press')
        
        print(e.button())
        '''
        左键点击按钮，会在控制台输出“press”。注意，我们在父级上也调用了mousePressEvent()方法，
        不然的话，我们是看不到按钮按下的效果的。
        mousePressEvent()是鼠标给予压力的事件，各个键有对应的int值（e.button()）
        分鼠标左键（Qt.leftButton = 1）、右键（2）、滚轮（4）、前进键（16）、后退键（8） （不包含dpi键）
        '''


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)


    def dragEnterEvent(self, e):

        e.accept()


    def dropEvent(self, e):

        position = e.pos()
        self.button.move(position)
        '''
        在dropEvent()方法里，我们定义了按钮按下后和释放后的行为，获得鼠标移动的位置，然后把按钮放到这个地方
        '''

        e.setDropAction(Qt.MoveAction)
        '''
        指定放下的动作类型为moveAction
        '''


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()