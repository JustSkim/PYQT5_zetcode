#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例3：子菜单
ZetCode PyQt5 tutorial 

This program creates a submenu.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):         
        self.setWindowIcon(QIcon('icon.png'))  #设置图标
        menubar = self.menuBar()
        
        #菜单栏上一个没有子级菜单的纯粹选项（动作）
        GoAction = menubar.addAction("GOOOOOOOOoo")

        '''
        主菜单栏第一项为File，其下添加两个动作（addAction(impAct)）New和Save，
        添加两个子级菜单(addMenu(impMenu))Import和Import2
        '''
        fileMenu = menubar.addMenu('File')
        
        impMenu = QMenu('Import', self) #定义一个子菜单 Import
        impAct = QAction('Import mail', self) #在子菜单Import下的子级菜单 Import mail
        impMenu.addAction(impAct) #用addAction()关联事件————悬浮在Import时会出现Import mail。
        
        impMenu2 = QMenu('Import2', self)
        impAct2 = QAction('Import mail2', self)
        impMenu2.addAction(impAct2)
        
        newAct = QAction('New一个', self)        
        save = QAction('Save保存文件',self)

        fileMenu.addAction(newAct)#添加了菜单下的一个动作（也就是可直接进行的选项而非子级菜单）
        fileMenu.addAction(save) #添加了动作“Save保存文件”，注意顺序在new之后
        fileMenu.addMenu(impMenu)#添加了子菜单，注意函数addMenu是和添加主菜单一样的
        fileMenu.addMenu(impMenu2)

        #定义菜单栏的选项edit
        editMenu = menubar.addMenu("Edit")
        
        impMenu_edit = QMenu("write in Chinese",self)
        editMenu.addMenu(impMenu_edit)

        impAct_edit = QAction("give up",self)
        editMenu.addAction(impAct_edit)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())