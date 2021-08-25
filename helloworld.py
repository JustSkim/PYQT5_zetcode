#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
例1 helloworld.py
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    #引入了PyQt5.QtWidgets模块，这个模块包含了基本的组件。
    app = QApplication(sys.argv)
    '''
    QApplication管理GUI程序的控制流和主要设置。
    QApplication包含窗口系统和其他来源处理过和发送过的主事件循环。它也处理应用程序的初始化和收尾工作，并提供对话管理。
    QApplication可以对系统和应用的大部分设置项进行设置。
    对于用Qt写的任何一个GUI应用，不管这个应用有没有窗口或多少个窗口，有且只有一个QApplication对象。
    sys.argv是一组命令行参数的列表。Python可以在shell里运行，这个参数提供对脚本控制的功能
    每一个PyQt5项目都需要创建一个 QApplication 对象。 sys.argv 则提供了命令行的一些参数，这样 Python 脚本就能从 Shell 运行，这是我们控制脚本开始运行的方式。
    
    每个PyQt5应用都必须创建一个应用对象。sys.argv是一组命令行参数的列表。
    Python可以在shell里运行，这个参数提供对脚本控制的功能。

    至于为什么需要sys.argv，可以看这一个回答：https://stackoverflow.com/questions/27940378/why-do-i-need-sys-argv-to-start-a-qapplication-in-pyqt
    This calls the constructor of the C++ class QApplication. 
    It uses sys.argv (argc and argv in C++) to initialize the QT application. 
    There are a bunch of arguments that you can pass to QT, like styles, debugging stuff and so on.
    以及官方文档：https://doc.qt.io/qt-5/qapplication.html#QApplication
    '''



    '''
    PyQt5类中有多种模板：MainWindow, QWidget以及Dialog等，
    QWidget类是所有用户界面对象的基类，从窗口系统接收鼠标、键盘和其它事件，并且在屏幕上绘制自己的表现，
    每一个窗口部件都是矩形，并按Z轴顺序排列的。
    一个窗口部件可以被它的父级窗口部件或者它前面的窗口部件盖住一部分。
    '''
    w = QWidget()

    #窗口大小，单位px
    w.resize(250, 150)
    
    #窗口在显示屏中的位置
    w.move(1200, 300)

    #为窗口添加了一个在标题栏展示的标题
    w.setWindowTitle('Simple')

    #show()能让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。
    w.show()

    sys.exit(app.exec_())
    #当调用exit()方法或直接销毁主控件时，主循环就会结束。sys.exit()方法能确保主循环安全退出。外部环境会收到主控件如何结束的信息。
    #exec_()之所以有个下划线，是因为exec是一个Python的关键字。