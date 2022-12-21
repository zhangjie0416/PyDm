# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : loginView.py
# Time       ：2022/3/2 19:53
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：登陆界面View
"""
from Resource.ui.login import LoginUI
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal


class LoginView(LoginUI, QWidget):
    def __init__(self):
        super(LoginView, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
