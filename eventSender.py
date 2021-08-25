#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：事件发送
ZetCode PyQt5 tutorial 

In this example, we determine the event sender
object.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()


    def buttonClicked(self):

        sender = self.sender()
        '''
Returns a pointer to the object that sent the signal, if called in a slot activated by a signal; 
otherwise(否则) it returns None . The pointer is valid only during the execution(执行) of the slot that calls 
this function from this object’s thread context.The pointer returned by this function becomes invalid 
if the sender(发送人) is destroyed, or if the slot is disconnected from the sender’s signal.

sender()在QT里的原型是QObject::sender(),也就是对象，实例化的对象可以发送信号，返回发送信号的对象的指针，返回类型为QObject *
        '''

        self.statusBar().showMessage(sender.text() + ' was pressed')
        '''
        Returns the object that emitted the signal. 该函数没有参数，返回发送信号的那一个对象
        用调用sender()方法的方式决定了事件源。状态栏显示了被点击的按钮.
        '''


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())