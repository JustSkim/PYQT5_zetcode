#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：行编辑
让标签的文本与输入文本相同
ZetCode PyQt5 tutorial 

This example shows text which 
is entered in a QLineEdit
in a QLabel widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
例子中展示了一个编辑组件和一个标签，我们在输入框里键入的文本，会立即在标签里显示出来
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, 
    QLineEdit, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.lbl = QLabel(self)

        qle = QLineEdit(self)
        #创建一个QLineEdit对象。

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)
        '''
        输入框的值有变化时调用我们自己创建的一个方法。
        QLineEdit类中的常用信号textChanged：当修改文本内容时，这个信号就会发射
        '''

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()


    def onChanged(self, text):
        #把文本框里的值赋值给了标签组件，然后调用adjustSize()方法让标签自适应文本内容
        self.lbl.setText(text)  #改变标签的文本
        self.lbl.adjustSize()   #adjustSize() 根据内容自适应大小


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())