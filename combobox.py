#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例子：组合下拉框
ZetCode PyQt5 tutorial 

This example shows how to use 
a QComboBox widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

'''
QComboBox组件能让用户在 多个选择项 中 选择 一个
combo 意为 组合的意思
combobox: 组合框；下拉列表框
'''
from PyQt5.QtWidgets import (QWidget, QLabel, 
    QComboBox, QApplication)
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.lbl = QLabel("Ubuntu", self)

        combo = QComboBox(self)
        combo.addItem("Ubuntu")  #添加选项
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")
        combo.addItems(["CentOS","Alibaba linux"])
        '''
        addItem()	添加一个下拉选项
        addItems()	从列表中添加下拉选项
        Clear()	删除下拉选项集合中的所有选项
        count()	返回下拉选项集合中的数目
        currentText()	返回选中选项的文本
        itemText(i)	获取索引为i的item的选项文本
        currentIndex()	返回选中项的索引
        setItemText(int index,text)	改变序列号为index的文本
        原文链接：https://blog.csdn.net/jia666666/article/details/81534260
        '''

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)        

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()


    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()  


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())