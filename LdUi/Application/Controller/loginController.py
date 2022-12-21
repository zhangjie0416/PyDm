# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : loginController.py
# Time       ：2022/3/2 20:22
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：登陆 控制层
"""

from Application.View.loginView import LoginView


class LoginController:
    def __init__(self):
        self.loginView = LoginView()
        self.init()

    def init(self):
        self.loginView.show()
