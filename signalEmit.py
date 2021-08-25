#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：信号发送
ZetCode PyQt5 tutorial 

In this example, we show how to 
emit（发射，发送） a custom signal. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    #创建了一个叫closeApp的信号，这个信号会在鼠标按下的时候触发，事件与QMainWindow绑定。
    closeApp = pyqtSignal() 


class Example(QMainWindow):
    '''
    class PySide2.QtWidgets.QMainWindow([parent=None[, flags=Qt.WindowFlags()]])¶
    param parent
    PySide2.QtWidgets.QWidget

    param flags
    WindowFlags

    Constructs a QMainWindow with the given parent and the specified widget flags .

    QMainWindow sets the Window flag itself, and will hence always be created as a top-level widget.
    '''
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):      
        self.c = Communicate()  
        '''
        Communicate类创建了一个pyqtSignal()属性的信号。
        '''

        self.c.closeApp.connect(self.close)     
        '''
        PySide2.QtGui.QWindow.close()¶
        Return type
        bool
        功能只有一个Close the window.
        '''  

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        event.gg = 'gg'
        print("event: ",event.__dict__) #打印对象的全部属性
        self.c.closeApp.emit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())