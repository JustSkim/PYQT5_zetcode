#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
# 例3 提示框
ZetCode PyQt5 tutorial 

This example shows a tooltip on 
a window and a button.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)
    #引用相关模块
from PyQt5.QtGui import QFont    


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        #为应用创建了一个提示框，10px的SansSerif字体
        QToolTip.setFont(QFont('SansSerif', 10))
        #QToolTip.setFont(QFont('SansSerif', 10,QFont.Bold,italic=True))
        #函数QFont具体使用见 https://doc.qt.io/qtforpython/PySide6/QtGui/QFont.html
        #参数：字体类型，大小（px），粗细，斜体...

        btn = QPushButton(text='Button',parent=self)
        '''
        创建一个继承自QPushButton的按钮。第一个参数text参数是想要显示的按钮名称，
        第二个参数parent是按钮的父级组件，这个例子中，self所指的父级组件，就是我们创建的继承自Qwidget的Example类。
        应用中的组件都是一层一层（继承而来的？）的，在这个层里，大部分的组件都有自己的父级，
        没有父级的组件（parent=None,没有parent的QWidget类），是顶级的窗口，即被认为是最上层的窗体（通常是MainWindow）。
        '''

        #创建一个按钮，当鼠标悬浮于按钮时，提示'This is a QPushButton widget'
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        #调用setTooltip()创建提示框可以使用富文本格式的内容

        #当鼠标悬浮于窗口中时，提示'This is a QWidget widget'
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn.resize(btn.sizeHint())#sizeHint()会自动给定一个合适的尺寸
        btn.move(50, 50)       

        self.setGeometry(300, 300, 300, 200)
        #setGeometry()把窗口放到屏幕上并且设置窗口大小，4个参数分别代表屏幕坐标的x、y和窗口大小的宽、高。

        self.setWindowTitle('Tooltips')    #设置标题
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())