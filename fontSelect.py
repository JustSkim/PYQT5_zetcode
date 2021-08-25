#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：选择字体
ZetCode PyQt5 tutorial 

In this example, we select a font name
and change the font of a label. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
    QSizePolicy, QLabel, QFontDialog, QApplication)
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        vbox = QVBoxLayout()
        '''
        QHBoxLayout和QVBoxLayout类继承自QBoxLayout，采用QBOXLayout类可以在水平和垂直方向上排列控件，
        本案例采用QHBoxLayout类，按照从左到右的顺序来添加控件，
        详见博客https://blog.csdn.net/jia666666/article/details/81699900
        '''

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self) 
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)          

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()


    def showDialog(self):

        font, ok = QFontDialog.getFont()
        '''
        创建了一个有一个按钮和一个标签的QFontDialog的对话框，我们可以使用这个功能修改字体样式.
        getFont()方法返回一个字体名称和状态信息。状态信息有OK和其他两种。
        static PySide2.QtWidgets.QFontDialog.getFont([parent=None])¶
        Parameters
        parent – PySide2.QtWidgets.QWidget
        Return type
        PyTuple
        '''
        if ok:
            #如果点击OK，标签的字体就会随之更改
            self.lbl.setFont(font)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())