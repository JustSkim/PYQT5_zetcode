#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例4：勾选菜单
ZetCode PyQt5 tutorial 

This program creates a optional menu.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from typing import ValuesView
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):         
        
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')   #状态栏显示

        menubar = self.menuBar()

        #本例创建了一个行为菜单。这个行为／动作能切换状态栏显示或者隐藏。

        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction(text='View statusbar', parent=self, checkable=True)
        #checkable选项为True，意味着所创建的这一个 动作（父级菜单的子项） 能被选中

        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)    #设置该动作的默认状态为选中状态
        
        viewStatAct.triggered.connect(self.toggleMenu)#绑定动作激活时的事件

        viewMenu.addAction(viewStatAct)
        

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')    
        self.show()

    def toggleMenu(self, state):
        #根据是否打钩来决定是否显示底部的状态栏
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())