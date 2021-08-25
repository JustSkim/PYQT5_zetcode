#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：选择颜色
ZetCode PyQt5 tutorial 

In this example, we select a color value
from the QColorDialog and change the background
color of a QFrame widget. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, 
    QColorDialog, QApplication)
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        col = QColor(222, 222, 0) 
        '''
        这里通过rgb三项来设置默认的背景颜色为黄色，下面可以使用QColorDialog改变背景颜色
        '''

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)   #点击事件绑定函数

        self.frm = QFrame(self)
        '''
        容器中的Frame为一个矩形的框架对象，对应类QFrame，
        QFrame类是PyQt中带框架部件的所有类的基类，如菜单、进度条、Label标签
        '''

        self.frm.setStyleSheet("QWidget { background-color: %s }" 
            % col.name())
        self.frm.setGeometry(130, 22, 100, 100)            

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()


    def showDialog(self):

        col = QColorDialog.getColor()
        '''
        弹出一个QColorDialog对话框
        Pops up a modal color dialog with the given window title (or “Select Color” if none is specified), lets the user choose a color, and returns that color. The color is initially set to initial . The dialog is a child of parent . 
        It returns an invalid (see isValid() ) color if the user cancels the dialog.
        The options argument allows you to customize the dialog.

        调出一个调色板窗口，用户选定颜色后，该函数会用name ()方法返回颜色值
        Return type: PySide2.QtGui.QColor  返回一个class类型
        '''
        for item in dir(col):
            print('--  ',item,'  --')
            #打印该class中的属性、方法名称

        if col.isValid():
            #PySide2.QtGui.QColor.isValid()¶  Returns true if the color is valid; otherwise returns false .
            
            print("RGB: ",col.name())
            #Returns the name of the color in the format “#RRGGBB”; i.e. a “#” character followed by three two-digit hexadecimal numbers.

            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())