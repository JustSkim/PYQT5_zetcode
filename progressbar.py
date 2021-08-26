#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：进度条
ZetCode PyQt5 tutorial 

This example shows a QProgressBar widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.pbar = QProgressBar(self)
        #新建一个QProgressBar构造器。

        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)#点击绑定一个用来控制开始和停止的方法

        self.timer = QBasicTimer()
        '''
        用时间控制进度条。
        QBasicTimer类为对象提供计时器事件。这是Qt内部使用的一个快速，轻量级和低级别的类。
        注意这个定时器是一个重复的定时器，除非调用stop()函数，否则它将发送后续的定时器事件。
        当定时器超时时，它将向QObject子类发送一个timer事件。
        '''
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()


    def timerEvent(self, e):
        '''
        每个QObject和又它继承而来的对象都有一个timerEvent()事件处理函数。
        为了触发事件，我们重载（≠重写）了这个方法。
        '''
        if self.step >= 100:
            self.timer.stop()
            '''
            PySide2.QtCore.QBasicTimer.stop()¶
                No parameters.
                Stops the timer.
            '''
            self.btn.setText('Finished') #改变按钮控件的text值
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)#设置值


    def doAction(self):
        
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            '''
            调用start()方法加载时间事件，这个方法有两个参数：过期时间（单位：毫秒）和事件接收者
            start(int, QObject)
            '''
            self.btn.setText('Stop')#按钮文字改为“Stop”


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())