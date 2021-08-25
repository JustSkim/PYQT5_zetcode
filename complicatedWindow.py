#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：能反馈信息的布局
ZetCode PyQt5 tutorial 

In this example, we create a more 
complicated window layout using
the QGridLayout manager. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QGridLayout, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        '''
        用QGridLayout模块制作两个行编辑窗口和一个文本编辑窗口
        '''

        grid = QGridLayout()
        #一个QGridLayout类
        #QGridLayout(parent)，在构建新网格布局时必须将其插入父布局，没有则为self。

        grid.setSpacing(10)
        #各个控件之间的间距（包括上下左右）设置为10px

        '''
        在组件的排列中，行列均从0开始，
        行缺失则后面的填上位置，所以从0或1开始无所谓，
        但网格化布局中，列必须从0而不是1开始，也不能缺失
        '''
        grid.addWidget(title, 0, 0)     #将该组件添加至第0行第0列
        grid.addWidget(titleEdit, 0, 1) #将该组件添加至第0行第1列

        grid.addWidget(author, 1, 0)
        grid.addWidget(authorEdit, 1, 1)

        grid.addWidget(review, 2, 0)
        grid.addWidget(reviewEdit, 2, 1, 5, 1)
        '''
        PySide2.QtWidgets.QGridLayout.addWidget(arg__1, row, column, rowSpan, columnSpan[, alignment=Qt.Alignment()])
        row:行位置
        column：列位置
        rowSpan：跨行数、行跨距（一般用于QTextEdit()文本输入组件）
        columnSpan：列跨距
        alignment；对齐方式
        这里文本编辑窗口跨5行，仍然只占一列
        '''

        self.setLayout(grid) 
        #设置布局管理器，一个QWidget控件中只能设置一个

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())