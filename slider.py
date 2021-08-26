#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：滑块
ZetCode PyQt5 tutorial 

This example shows a QSlider widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QSlider, 
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        sld = QSlider(Qt.Horizontal, self)
        '''
        创建一个水平的QSlider
        QSlider控件提供一个垂直或者水平的滑动条，滑动条是一个用于控制有界值典型的控件，
        它允许用户沿水平或者垂直方向在某一范围内移动滑块，并将滑块所在的位置转换为一个合法范围内的整数值，
        有时候这中方式比输入数字或者使用SpinBox（计数器·）更加自然，在槽函数中对滑块所在位置的处理相当于从整数之间的最小值和最高值进行取值
        原文链接：https://blog.csdn.net/jia666666/article/details/81534588
        '''

        sld.setFocusPolicy(Qt.NoFocus)
        '''
        setFocusPolicy(Policy)  设置焦点获取策略
            Qt.TabFocus() 通过Tab键获取焦点
            Qt.ClickFocus() 通过被单击获取焦点
            Qt.StrongFocus()    可以通过上面两种方式获取焦点
            Qt.NoFocus()    不能通过上面两种方式获取焦点
        '''
        sld.setGeometry(30, 40, 100, 300)
        '''
        setGeometry()有两个作用：
        把窗口放到屏幕上；设置窗口大小。
        四个参数分别代表屏幕坐标的x、y和窗口大小的宽、高。
        这个方法是resize()和move()的合体。
        '''
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        '''
        创建一个QLabel组件并给它设置一个静音图标(作为图标的默认设置)
        PySide2.QtWidgets.QLabel.setPixmap(arg__1)¶
        Parameters
        arg__1 – PySide2.QtGui.QPixmap
        This property holds the label’s pixmap..
        Previously, Qt provided a version of pixmap() which returned the pixmap by-pointer. That version is now deprecated. To maintain compatibility with old code, you can explicitly differentiate between the by-pointer function and the by-value function:
        
        QPixmap类用于绘图设备的图像显示，它可以作为一个QPainterDevice对象，也可以加载到一个控件中，通常是标签或者按钮，用于在标签或按钮上显示图像
        QPixmap可以读取的图像文件类型有BMP，GIF，JPG等
        
        '''
        self.label.setGeometry(160, 40, 1000, 800)

        self.setGeometry(100, 100, 2000, 1600)
        self.setWindowTitle('QSlider')
        self.show()


    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('med.png'))
        else:
            self.label.setPixmap(QPixmap('max.png'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())