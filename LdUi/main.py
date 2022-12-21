# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : main.py
# Time       ：2022/3/2 11:03
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：程序入口
"""
import sys
from PyQt5.QtWidgets import QApplication
from Application.Controller.mainController import MainController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_ui = MainController()
    sys.exit(app.exec_())

