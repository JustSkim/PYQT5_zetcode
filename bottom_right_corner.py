#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：盒布局
ZetCode PyQt5 tutorial 

In this example, we position two push
buttons in the bottom-right corner 
of the window. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        okButton = QPushButton("OK")
        #创建一个继承自QPushButton的按钮(自然就是一个控件)。第一个参数text参数是想要显示的按钮名称，第二个参数parent是按钮的父级组件
        
        cancelButton = QPushButton("Cancel")

        '''
        下面十行代码创建一个水平布局，并增加弹性空间和两个按钮。
        addStretch函数的作用就是平分布局，它所带的参数就是所占的比例，这里为1占据了全部
        '''

        hbox = QHBoxLayout()
        '''
        QHBoxLayout和QVBoxLayout类继承自QBoxLayout，采用QBOXLayout类可以在水平和垂直方向上排列控件，
        本案例采用QHBoxLayout类，按照从左到右的顺序来添加控件，
        详见博客https://blog.csdn.net/jia666666/article/details/81699900
        '''

        hbox.addStretch(1)
        hbox.addWidget(okButton)    
        '''
        PySide2.QtWidgets.QGridLayout.addWidget(arg__1, row, column, rowSpan, columnSpan[, alignment=Qt.Alignment()])
        row:行位置
        column：列位置
        rowSpan：跨行数、行跨距（一般用于QTextEdit()文本输入组件）
        columnSpan：列跨距
        alignment；对齐方式

        if rowSpan and/or columnSpan is -1, then the widget will extend to the bottom and/or right edge, respectively.
        如果这两项设置为-1，该小组件会分别沿两个方向延伸到底部/右边缘

        这里增加了一个按钮
        addwidget()方法用于向布局中添加控件（这里是按钮okButton）
        '''

        hbox.addWidget(cancelButton)


        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        '''
        为了布局需要，我们把这个水平布局放到了一个垂直布局盒里面。弹性元素会把水平布局挤到窗口的下边。
        '''

        self.setLayout(vbox)    

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())