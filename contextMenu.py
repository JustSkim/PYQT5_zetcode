#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例5：右键菜单
ZetCode PyQt5 tutorial 

This program creates a context menu.
context有内容、上下文的意思，context menu意为右键菜单（上下文菜单）

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):         

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context menu')    
        self.show()

    '''
    利用右键菜单事件 QWidget::contextMenuEvent() 来处理右键事件，所以需要重写此函数
    '''
    def contextMenuEvent(self, event):
            '''
            The QMenu class provides a menu widget for use in menu bars, context menus, and other popup menus
            '''
            cmenu = QMenu('这里的文字不会显示，有无均可',self) #使用QMenu创建一个上下文菜单，即右键菜单

            newAct = cmenu.addAction("New")     #添加了一名为“New”的动作
            opnAct = cmenu.addAction("Open")
            quitAct = cmenu.addAction("Quit")
            action = cmenu.exec_(self.mapToGlobal(event.pos()))
            '''
            使用exec_()方法显示菜单。从鼠标右键事件对象中获得当前坐标。mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
            '''

            '''
            如果点击右键菜单中的Quit动作，则退出
            右键菜单里触发了事件，也就触发了退出事件，执行关闭菜单行为
            '''
            if action == quitAct:
                qApp.quit() 
            else:
                print("现在执行的动作不是quitAct")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())