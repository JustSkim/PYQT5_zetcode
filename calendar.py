#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：日历
ZetCode PyQt5 tutorial 

This example shows a QCalendarWidget widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QCalendarWidget, 
    QLabel, QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        vbox = QVBoxLayout(self)
        '''
        QHBoxLayout和QVBoxLayout类继承自QBoxLayout，采用QBOXLayout类可以在水平和垂直方向上排列控件，
        本案例采用QHBoxLayout类，按照从左到右的顺序来添加控件，
        详见博客https://blog.csdn.net/jia666666/article/details/81699900
        '''

        cal = QCalendarWidget(self)
        '''
        创建一个QCalendarWidge
        '''
        cal.setGridVisible(False)
        #setGridVisible(bool)方法可以设置是否在日历上显示网格

        cal.clicked[QDate].connect(self.showDate)
        '''
        选择一个日期时，QDate的点击信号就触发了，把这个信号和我们自己定义的showDate()方法关联起来
        '''

        vbox.addWidget(cal)

        self.lbl = QLabel(self)

        date = cal.selectedDate()
        '''
        selectedDate()方法获取日历控件选中的日期(格式为一个QDate日期对象)
        PySide2.QtWidgets.QCalendarWidget.selectedDate()¶
        Return type
        PySide2.QtCore.QDate
        This property holds the currently selected date..
        The selected date must be within the date range specified by the minimumDate and maximumDate properties. By default, the selected date is the current date.
        '''

        self.lbl.setText(date.toString())#将该日期对象转换为字符串

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()


    def showDate(self, date):     

        self.lbl.setText(date.toString())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())