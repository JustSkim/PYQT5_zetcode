#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：splitter 分束器————窗口分隔
ZetCode PyQt5 tutorial 

This example shows
how to use QSplitter widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
QSplitter组件能让用户通过 拖拽分割线 的方式改变子窗口大小的组件。本例中我们展示用两个分割线隔开的三个QFrame组件。
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
                             QSplitter, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        '''
        为了更清楚的看到分割线，我们使用了设置好的子窗口样式。
        QFrame的相关值与表现形式可见 http://allstack.net/wordpress/post-918.html
        注意这里是 StyledPanel 而不是style!
        '''

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        '''
        创建一个QSplitter组件，并在里面添加了两个框架
        '''

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        '''
        在分割线里面再进行分割
        '''
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


    def onChanged(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())