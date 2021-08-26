#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create three toggle buttons.
They will control the background color of a 
QFrame. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QFrame, QApplication)
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.col = QColor(0, 0, 0)       

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)
        #每一种颜色都与这一个设置色彩（RGB三项分别）的函数点击关联

        self.square = QFrame(self)
        '''
        容器中的Frame为一个矩形的框架对象，对应类QFrame，
        QFrame类是PyQt中带框架部件的所有类的基类，如菜单、进度条、Label标签
        '''

        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()


    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else: val = 0

        if source.text() == "Red":
            self.col.setRed(val)   
            #将RGB模式中红色值调为val=255             
        elif source.text() == "Green":
            self.col.setGreen(val)             
        else:
            self.col.setBlue(val) 

        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())  
        '''
        使用样式表（就是CSS的SS）改变背景色
        此处self.square是一个QFrame类
        PySide2.QtWidgets.QWidget.setStyleSheet(styleSheet)¶
        Parameters： styleSheet – str
        This property holds the widget’s style sheet.
        The style sheet contains a textual description of customizations to the widget’s style, as described in the Qt Style Sheets document.
        该函数可以设置样式（包括颜色、字体、边框等，类比于html中style属性）
        '''


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())