#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例5  消息盒子
ZetCode PyQt5 tutorial 

This program shows a confirmation 
message box when we click on the close
button of the application window. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Message box')    
        self.show()

    '''
    QWidget在程序窗口关闭时会触发 closeEvent() 事件
    因此我们这里药重写窗口方法closeEvent,添加关闭窗口触发的事件
    '''
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        '''
        创建了一个消息框，上面有俩按钮：Yes和No.第一个字符串显示在消息框的标题栏，第二个字符串显示在对话框，第三个参数是消息框的俩按钮，最后一个参数是默认按钮，这个按钮是默认选中的。返回值在变量reply里。
        '''

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()     
        '''
        关闭QWidget，就会产生一个QCloseEvent，并且把它传入到closeEvent函数的event参数中。
        改变控件的默认行为，就是替换掉默认的事件处理。
        '''
               


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())