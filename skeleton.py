#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：栅格化布局
ZetCode PyQt5 tutorial 

In this example, we create a skeleton
of a calculator using a QGridLayout.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, 
    QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout(self)
        '''
        QGridLayout（网格布局）是将窗口分割成行和列的网格来进行排列，
        通常可以使用函数addWidget（）将被管理的控件（Widget）添加到窗口中，或者使用addLayout（）函数将布局（layout）添加到窗口中，
        也可以通过addWIdget（）函数对所添加的控件设置行数与列数的跨越，最后实现网格占据多个窗格。
        QGridLayout类中有以下三个常用方法：
        
        addWidget(QWidget Widget,int row,int col,int alignment=0)  
        给网格布局添加部件，设置指定的行和列，起始位置的默认值为（0,0）

        addWidget(QWidget widget,int fromRow,int fromColulmn,int rowSpan,int columnSpan,Qt.Alignment alignment=0)
        setSpacing(int spacing)
        所添加的的控件跨越很多行或者列的时候，使用这个函数

        setSpacing(int spacing)
        设置软件在水平和垂直方向的间隔

        详见https://blog.csdn.net/jia666666/article/details/81701176
        '''


        self.setLayout(grid)
        #创建一个QGridLayout实例，并把它放到程序窗口里
        '''
        有些控件或者布局有addLayout和addWidget的函数,但是有些就没有,
        比如QWidget这个控件就没有addLayout和addWidget这个函数,取而代之的是一个setLayout函数,
        在addLayout函数中,我们可以多次使用addLayout来依次添加布局,addWidget亦是如此,
        但是setlayout只能set一次

        官方文档中对此的解释：
        Sets the layout manager for this widget to layout .
        If there already is a layout manager installed on this widget, QWidget won’t let you install another. You must first delete the existing layout manager (returned by layout() ) before you can call with the new layout.
        If layout is the layout manager on a different widget, will reparent the layout and make it the layout manager for this widget.
        翻译过来就是：
        为此小组件设置布局管理器以布局。
        若您已经在此窗口小部件上安装了一个布局管理器，则QWidget这个控件不会允许您安装另一个布局管理器，除非删除现有的布局管理器（在使用新布局调用之前删除PlayOut（））。
        如果布局是在不同的另一个窗口小部件上的布局管理器，那么将重新定义布局并使其成为此小部件的布局管理器。
        '''
        

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        #定义一个列表，存储将要使用的按钮的名称

        positions = [(i,j) for i in range(5) for j in range(4)]
        #生成位置坐标，五行(i)四列(j)

        for position, name in zip(positions, names):
            #依次创建按钮位置列表
            if name == '':
                continue
            #为空的话，原本控件的位置会空出来，不会被后面的挤占

            button = QPushButton(name)
            '''
            www.zetcode.com的解释
            QPushButton is a widget which executes an action when a user clicks on it. A QPushButton can display text and icons.
            '''

            grid.addWidget(button, *position)
            '''
            QGridLayout::addWidget ( QWidget * widget, int row, int column, Qt::Alignment alignment = 0 )
            python中，*参数收集所有未匹配的位置参数组成一个tuple对象（元组），局部变量args指向此tuple对象
            '''
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())