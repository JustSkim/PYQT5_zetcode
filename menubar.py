#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例2：菜单栏
ZetCode PyQt5 tutorial 

This program creates a menubar. The
menubar has one menu with an exit action.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: January 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        '''
        QAction是菜单栏、工具栏或者快捷键的动作的组合。
        上面三行中，前两行创建了一个图标、一个exit的标签和一个快捷键组合，都执行了一个动作；
        第三行，创建了一个状态栏，当鼠标悬停在菜单栏的时候，能显示当前状态。
        '''

        exitAct.triggered.connect(qApp.quit)
        #当执行这个指定的动作时，就触发了一个事件。这个事件跟QApplication的quit()行为相关联，所以这个动作就能终止这个应用。

        self.statusBar()

        menubar = self.menuBar()    #创建一个菜单栏（位于顶部固定位置）
        '''
        QMenu和QMenuBar是Qt中的菜单类(也就是右键菜单)和菜单栏类，其中，菜单QMenu挂载在菜单栏QMenuBar上
        '''


        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        '''
        menuBar()创建菜单栏。这里创建了一个菜单栏，并用addMenu()在上面添加了一个file菜单，
        用addAction()关联了点击退出应用的事件/动作（也就是可直接进行的选项而非子级菜单）。
        '''

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())