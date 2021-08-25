#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：输入文字
ZetCode PyQt5 tutorial 

In this example, we receive data from
a QInputDialog dialog. 

Aauthor: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
    QInputDialog, QApplication)
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialog(self):
        print("the type of return is : ",type(QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')))
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        '''
        显示一个输入框的代码。第一个参数是输入框的标题，第二个参数是输入框的占位符。
        对话框返回输入内容和一个布尔值，如果点击的是OK按钮，布尔值就返回True

        python的解构语法（逗号在左，与封装语法相反）
        把线性结构(列表，元组，字符串，bytes，baitarry)的元素解开，并顺序的赋给其他变量；
        左边接纳的变量数要和右边解开的元素个数一致；

        static PySide2.QtWidgets.QInputDialog.getText(parent, title, label[, echo=QLineEdit.Normal[, text=""[, flags=Qt.WindowFlags()[, inputMethodHints=Qt.ImhNone]]]])¶
        Parameters
        parent – PySide2.QtWidgets.QWidget
        title – str
        label – str
        echo – EchoMode
        text – str
        flags – WindowFlags
        inputMethodHints – InputMethodHints
        Return type：(str,bool)

(QString, bool ok) QInputDialog.getText (QWidget parent, QString title, QString label, QLineEdit.EchoMode mode = QLineEdit.Normal, QString text = '', Qt.WindowFlags flags = 0)

        '''

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())