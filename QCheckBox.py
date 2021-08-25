#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, a QCheckBox widget
is used to toggle the title of a window.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        cb = QCheckBox('Show title', self)
        #QCheckBox的构造器，QCheckBox组件有两个状态：开和关
        '''
        QCheckBox构造一个三态复选框
        名称                值       含义
        Qt.Checked	        2	 组件没有被选中（默认）
        Qt.PartiallyChecked	1 	 组件被半选中
        Qt.Unchecked	    0    组件被选中
        '''

        cb.move(20, 20)
        print('cb.toggle = ',cb.toggle())
        '''
        检查单选框的状态。默认情况下，窗口没有标题，单选框未选中
        PySide2.QtWidgets.QAbstractButton.toggled(checked)¶
        Parameters
        checked – bool
        '''

        cb.stateChanged.connect(self.changeTitle)
        '''
        PySide2.QtWidgets.QCheckBox.stateChanged(arg__1)¶
        Parameters
        arg__1 – int
        '''

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()


    def changeTitle(self, state):
        print("state = ",state)
        '''
        Qt.Checked为int类型，值为2，代表组件没有被选中
        '''
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())