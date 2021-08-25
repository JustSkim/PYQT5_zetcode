#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例4：关闭窗口
ZetCode PyQt5 tutorial 

This program creates a quit
button. When we press the button,
the application terminates. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
#程序需要QtCore对象


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        qbtn = QPushButton(text='Quit', parent=self)
        #创建一个继承自QPushButton的按钮。第一个参数text参数是想要显示的按钮名称，第二个参数parent是按钮的父级组件
        
        #创建了一个点击之后就退出窗口的按钮。
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        '''
        事件传递系统在PyQt5内建的single（信号）和slot（槽）机制里面。
        点击按钮之后，信号会被捕捉并给出既定的反应。
        QCoreApplication包含了事件的主循环，它能添加和删除所有的事件，instance()创建了一个它的实例。
        QCoreApplication是在QApplication里创建的。 点击事件和能终止进程并退出应用的quit函数绑定在了一起。
        在发送者和接受者之间建立了通讯，发送者就是按钮，接受者就是应用对象。
        QpushButton常用的三种响应有pressed，released和clicked

        在Qt中，控件中的clicked（）信号和clicked（bool）信号是两个不同的信号，区别在于：
        映射槽函数时，clicked（）信号映射到的槽函数是不带参的，clicked（bool）信号映射到的槽函数是带参数的。
        '''
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())